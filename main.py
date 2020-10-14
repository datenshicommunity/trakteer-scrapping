import os
import time

import requests

from threading import Thread

from replit import db
from bs4 import BeautifulSoup
from flask import Flask, jsonify

app = Flask(__name__)

TEN_MINUTES_IN_SECONDS = 600
BASE_AMOUNT = 20000

CREATOR_NAME = os.getenv("CREATOR_NAME")
PAGE_URL = os.getenv("PAGE_URL")

def send_to_discord(supporter):
  payload = {
    "content": "Traktiran baru! Cek di " + PAGE_URL + "\nNama: **" + supporter["name"] + "**\nJumlah: **" + str(supporter["amount"]) + " IDR**\n"
  }

  requests.post(os.getenv("DISCORD_WEBHOOK"), json = payload)

  print("> Sending notification with id " + supporter["id"])

def process_data():
  db["app:is_processing"] = True

  req = requests.get(PAGE_URL)
  bs = BeautifulSoup(req.text, "html.parser")

  items = bs.findAll('div', { 'class' : 'item' })

  supporters = []

  for item in items:
    supporter = {}
    
    name = item.find('span', { 'class': 'name' }).get_text()
    avatar = item.find('div', { 'class': 'avatar'}).img['src']
    amount = item.find('span', { 'class': 'text-primary' }).get_text().split(' ')[0]

    if name == CREATOR_NAME:
      name = item.find('a', { 'class': 'name' }).get_text()
      avatar = item.find('div', {'class': 'avatar'}).img['data-src']

    supporter["id"] = item['id']
    supporter["name"] = name.strip()
    supporter["avatar"] = avatar
    supporter["amount"] = int(amount) * BASE_AMOUNT

    supporters.append(supporter)

  latest_supporter_id = db["trakteer:latest_supporter_id"]
  get_last_index=[i for i, _ in enumerate(supporters) if _['id'] == latest_supporter_id][0]

  # if get_last_index is not 0, it means we have new n supporter(s)
  # and we want to send it to our discord server!
  if get_last_index != 0:
    new_supporters = supporters[:get_last_index]
    for supporter in new_supporters:
      # to avoid rate-limit by discord. or should we use request's timeout instead?
      time.sleep(5)
      send_to_discord(supporter)

  next_check = time.time() + TEN_MINUTES_IN_SECONDS
  next_check_epoch = int(next_check) * 1000

  # save to "db"
  db["app:is_processing"] = False
  db["trakteer:next_check"] = next_check_epoch
  db["trakteer:latest_supporter_id"] = supporters[0]["id"]
  db["trakteer:cached_supporters"] = supporters

@app.route('/')
def index():
  try:
    now = int(time.time()) * 1000
    next_check = int(db["trakteer:next_check"])

    # check are we still processing the data?
    if db["app:is_processing"] == True:
      # just in case our thread is fucked up
      if now > next_check:
        db["app:is_processing"] = False

      # let's check are we have the cached data?
      cached_supporters = db["trakteer:cached_supporters"]

      return jsonify(data=cached_supporters, next_check=next_check, cache="HIT")

  except:
    # otherwise, just return empty data
    return jsonify(data=[], next_check=None, cache="MISS")

  # if not, let's determine should we render
  # the cached or the fresh one
  try:
    # this should be the cached one
    if now < next_check:
      try:
        cached_supporters = db["trakteer:cached_supporters"]

        return jsonify(data=cached_supporters, next_check=next_check, cache="HIT")
      except:
        pass

  except:
    pass

  # otherwise let's process the data
  thread = Thread(target=process_data)

  thread.daemon = True
  thread.start()

  # Let's return the data while we're invalidating the cache and processing the data
  try:
    cached_supporters = db["trakteer:cached_supporters"]
    cached_next_check = db["trakteer:next_check"]

    return jsonify(data=cached_supporters, next_check=cached_next_check, cache="GRACE")
  except:
    return jsonify(data=[], next_check=None, cache="MISS")

if __name__ == "__main__":
	app.run(
		host='0.0.0.0',
		port=3000
	)