import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

soal_anime = [
    {"soal": "Anime tentang ninja dari desa Konoha", "jawaban": ["naruto"]},
    {"soal": "Petarung Saiyan yang suka makan dan kuat banget", "jawaban": ["goku", "dragon ball"]},
    {"soal": "Detektif cilik hasil eksperimen APTX 4869", "jawaban": ["conan", "detective conan"]},
    {"soal": "Shinigami penggila apel dan buku kematian", "jawaban": ["death note", "light yagami", "ryuk"]},
    {"soal": "Bocah botak kuat dari satu pukulan", "jawaban": ["saitama", "one punch man"]},
]

jawaban_benar = ["Benar, Sugoi!", "Mantap jawabanmu benar!", "Wibu sejati nih! ✅", "TOP banget, lanjutkan!"]
jawaban_salah = ["Salah wibu palsu 😅", "Coba lagi, pasti bisa!", "Hampir bener, ulangi!", "Yah salah, next?"]

user_state = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("YUI SENPAII siap menebak anime! Gunakan /tebakanime")

async def tebakanime(update: Update, context: ContextTypes.DEFAULT_TYPE):
    soal = random.choice(soal_anime)
    user_state[update.effective_user.id] = {
        "mode": "anime",
        "jawaban": [j.lower() for j in soal["jawaban"]]
    }
    await update.message.reply_text(f"Tebak Anime:\n{soal['soal']}")

async def jawab(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id in user_state and user_state[user_id]["mode"] == "anime":
        if update.message.text.lower().strip() in user_state[user_id]["jawaban"]:
            await update.message.reply_text(random.choice(jawaban_benar))
            del user_state[user_id]
        else:
            await update.message.reply_text(random.choice(jawaban_salah))
    else:
        await update.message.reply_text("Ketik /tebakanime untuk mulai!")

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("tebakanime", tebakanime))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), jawab))
    print("Bot Anime siap...")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
