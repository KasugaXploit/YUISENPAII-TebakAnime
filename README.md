# Bot Telegram Tebak Anime - YUI SENPAII

🎌 Tebak karakter dan cerita anime langsung dari Telegram! Cocok buat kamu para wibu sejati!

## Fitur
- Soal acak seputar anime terkenal
- Jawaban benar/salah diberi balasan lucu
- Ringan & bisa dijalankan di Termux

## Instalasi via Termux

```bash
pkg update && pkg upgrade -y
pkg install python git -y
git clone https://github.com/KasugaXploit/YUISENPAII-TebakAnime.git
cd YUISENPAII-TebakAnime
pip install python-telegram-bot
nano bot_tebak_anime.py  # ganti BOT_TOKEN
python bot_tebak_anime.py

==============================
Cara Main
-Ketik /start
-Mulai dengan /tebakanime
-Jawab dengan nama karakter atau judul anime
==============================
