![logo](https://s3.edgyfn.app/faultable/misc/5f87602cd40b125b8f062264.png)

## Penjelasan sangat singkat:

Dapatkan 10 pendukung terakhir dari halaman [trakteer.id](https://trakteer.id) dalam format JSON

## Penjelasan singkat

1. Pertama kita akan scrapping halaman trakteer berdasarkan URL yang sudah disediakan di `PAGE_URL`
2. Nah diambil deh data-data seperti Nama pendukung, jumlahnya (berdasarkan dari jumlah * `BASE_AMOUNT`), dan avatar nya
3. Simpen di db nya repl.it
4. Klo ada data baru (diambil dari `data[:index_latest_supporter_id]`), kirim pemberitahuan ke discord
5. Setiap 10 menit, cek apakah data terbaru (plus didukung oleh cron nya GitHub Actions yang entah melanggar ToS nya apa kagak)
6. Tampilkan data dalam bentuk JSON
7. ???
8. aokwoakwoaoawkaokwoakwoakwoakw

## Penjelasan teknis singkat

- Pakai python 3
- Web Server pakai flask
- Scrapping pakai beautifulsoup4
- Request pakai requests
- Proses (scrapping + request) menggunakan lebih dari 1 thread
- DB pakai KV Storage nya repl.it
- Penjelasan terkait cache:
  - HIT: Data dari cache
  - MISS: Cache tidak ada
  - GRACE: Data dari cache tapi sambil perbarui cache
- Gak ada waktu buat nulis automated tests karena udah production ready since forever
- Cron dari GitHub Actions (hasil copas dari random code)

## Motivasi

Selain karena pusing lagi ngerjain kerjaan kantor malem2, terus iseng2 deh bikin ginian biar gw gak sering2 buka halaman trakteer
cuma biar tau apakah ada pendukung baru atau gak

Dan juga sekarang gw lagi aktif-aktifnya di Discord, jd yaudahlah ya daripada gw kirim ke telegram atau slack mending gw kirim
ke discord aja notifnya!

Tentu saja klo notif ke email pasti ada

## Demo

https://trakteer-scrapping.faultable.repl.co

## Development

I don't know like you know I just use repl.it because I'm boring

Maybe [you should too?](https://repl.it/upgrade/faultable)

## Production

Really?

## Traktir?

[You're welcome](https://trakteer.id/fariz)

## LICENSE

Harusnya MIT