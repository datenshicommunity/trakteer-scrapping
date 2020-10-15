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

## Usage

- Fork project ini di [repl.it](https://repl.it/@faultable/trakteer-scrapping)
- Ubah URL yang ada [disini](https://github.com/faultable/trakteer-scrapping/blob/master/.github/workflows/cek.yml) dengan URL project repl.it kamu
- Buat berkas .env (silahkan lihat berkas .env.example), lalu isi dengan format seperti ini (sebagai contoh)
  - `DISCORD_WEBHOOK=<discord_webhook>`, [pelajari disini](https://evlfctry.pro/o0101bsrc)
  - `CREATOR_NAME=<nama_creator>`, misal: `evilfactorylabs` atau `Fariz yang kamu kenal`, case-sensitive untuk sekarang
  - `PAGE_URL=<url_trakteer>`, misal: https://trakteer.id/evilfactorylabs
  - `BASE_AMOUNT=<unit traktrian>`, misal: di [evilfactorylabs](https://trakteer.id/evilfactorylabs) itu 20,000 (untuk bir), jadi isinya `20000`
- Push ke GitHub kamu project yang ada di repl.it tersebut
- Selesai!

Contoh lengkap dari berkas `.env`:

```
DISCORD_WEBHOOK=https://discord.com/api/webhooks/66631336696969/elb1cn1fn1
CREATOR_NAME=evilfactorylabs
PAGE_URL=https://trakteer.id/evilfactorylabs
BASE_AMOUNT=20000
```

Tangkapan layar untuk *log* ketika ada yang traktiran baru:

![Tangkapan layar untuk *log* ketika ada yang traktiran baru](https://s3.edgyfn.app/faultable/misc/Screen%20Shot%202020-10-15%20at%2010.09.42%20PM.png)

Dan ini di Discord nya:

![Tangkapan layar notifikasi di Discord](https://s3.edgyfn.app/faultable/misc/Screen%20Shot%202020-10-15%20at%2010.11.05%20PM.png)

Jika memiliki kendala, jangan sungkan untuk [kontak saya](https://faultable.dev/dm)

## Development

I don't know like you know I just use repl.it because I'm boring

Maybe [you should too?](https://repl.it/upgrade/faultable)

## Production

Really?

## Traktir?

[You're welcome](https://trakteer.id/fariz)

## LICENSE

Harusnya MIT
