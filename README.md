# UFORIA · Salah Kostum!

Mini game 15 detik untuk acara UFORIA (31 Desember 2026, Chase Plaza, Sudirman Jakarta). Pengunjung scan QR, tap **Mulai**, line-up performer muncul, pilih satu performer, lalu rapikan fotonya yang teracak. Kotak yang sudah benar jadi hijau dengan centang. Setelah selesai, muncul undangan "Welcome to UFORIA".

Line-up: RAN, Adrian Khalif, The Angels, DJ Throoper.

Situs statis murni (HTML, CSS, JS tanpa framework, tanpa build). Total sekitar 450 KB, aman untuk HP dengan sinyal venue.

## Isi repo

| Bagian | Isi |
|---|---|
| `public/index.html` | Seluruh game: layar mulai, line-up, puzzle, undangan. |
| `public/a/` | Aset webp (foto puzzle `pz-*`, kartu `card-*`, logo, aset retro), font `f/`. |
| `public/a/sfx/` | Tempat file suara ElevenLabs (lihat bagian Suara). Kalau kosong, game memakai bunyi synth bawaan. |
| `public/embed.js` | Script satu baris untuk memasang game di website lain. |
| `public/embed-demo.html` | Contoh halaman yang memasang game. |
| `public/_headers` | Header Cloudflare: game boleh di-iframe dari domain mana pun, aset di-cache. |
| `wrangler.jsonc` | Konfigurasi Cloudflare Workers (static assets saja). |
| `tools/qrposter.py` | Bikin QR polos dan poster QR retro untuk alamat game. |

## Deploy ke Cloudflare (sekali saja)

1. Dashboard Cloudflare, **Workers & Pages**, **Create**, **Import a repository**, pilih repo ini.
2. Build command dikosongkan, deploy command `npx wrangler deploy`.
3. Setelah jadi, alamatnya `https://uforia-salah-kostum.<akun>.workers.dev/`. Setiap push ke `main` otomatis deploy ulang.
4. Mau pakai domain sendiri (misalnya `main.uforia.id`): atur Custom Domain di pengaturan Worker.

Tes lokal tanpa Cloudflare: `cd public && python3 -m http.server 8080`, lalu buka `http://localhost:8080/`.

## Pasang di website orang lain

**Cara 1, satu baris script** (paling gampang, game muncul di posisi script):

```html
<script src="https://ALAMAT-GAME/embed.js" async></script>
```

Opsi: `data-max-width="440"`, `data-radius="18"`, `data-target="#id-elemen"`.

**Cara 2, iframe biasa** (untuk CMS yang melarang script, misalnya beberapa page builder):

```html
<div style="position:relative;width:100%;max-width:440px;margin:0 auto;aspect-ratio:9/16;min-height:560px;border-radius:18px;overflow:hidden">
  <iframe src="https://ALAMAT-GAME/?embed=1" title="UFORIA Salah Kostum"
    style="position:absolute;inset:0;width:100%;height:100%;border:0"
    allow="autoplay; fullscreen" loading="lazy"></iframe>
</div>
```

**Cara 3, link atau QR**: bagikan `https://ALAMAT-GAME/`.

Contoh hidup ada di `https://ALAMAT-GAME/embed-demo.html`.

## QR untuk alamat baru

```bash
pip install qrcode pillow fonttools brotli
python3 tools/qrposter.py https://ALAMAT-GAME/
```

Hasilnya `qr/UFORIA-QR.png` (polos, untuk cetak) dan `qr/UFORIA-QR-poster.png` (1080x1350, gaya retro). Scan sekali dengan HP sebelum dicetak.

## Suara

SFX dan voice dibuat di ElevenLabs, flow "UFORIA Salah Kostum - SFX". Unduh lalu taruh di `public/a/sfx/` dengan nama persis:

| File | Isi |
|---|---|
| `tap.mp3` | Tap kotak |
| `ok.mp3` | Kotak benar |
| `win.mp3` | Semua benar |
| `tick.mp3` | Hitung mundur dan 5 detik terakhir |
| `lose.mp3` | Waktu habis |
| `reveal.mp3` | Line-up muncul |
| `welcome.mp3` | Voice "Welcome to UFORIA!" di undangan |

File yang tidak ada otomatis diganti bunyi synth, jadi game tetap jalan.

## Mengganti performer

Daftar ada di `PERF` di `public/index.html`. Tiap performer butuh `a/pz-<id>.webp` (foto puzzle 600x761, rasio dijaga, crop bukan stretch) dan `a/card-<id>.webp` (potret 320 px). Logo opsional: kalau `logo` diisi `null`, nama ditulis dengan font Bungee. Pilih crop yang tiap barisnya punya kotak yang jelas beda, jangan sampai satu baris berisi dua kotak latar polos.

## Sebelum tayang publik

- Izin pakai foto dan logo semua performer dari manajemen masing-masing.
- Kostum DJ Throoper berbasis desain stormtrooper (milik Lucasfilm). Cek dulu dengan legal sebelum dipakai di materi promosi.
- Game tidak mengambil data pengunjung apa pun.
