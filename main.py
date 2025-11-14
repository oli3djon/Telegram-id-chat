# main.py
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os

# 🔒 Загружаем токен из .env файла
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("❌ Ошибка: BOT_TOKEN не найден в .env файле! Добавь его в .env")

# 📘 Команда: /get_chat_id — показывает ID текущего чата
async def get_chat_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    await update.message.reply_text(f"✅ Chat ID: `{chat.id}`", parse_mode="Markdown")
    print(f"[LOG] Chat ID: {chat.id} — Название: {chat.title or chat.first_name}")

# 👤 Команда: /get_my_id — показывает ID пользователя
async def get_my_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(f"👤 Ваш Telegram ID: `{user.id}`", parse_mode="Markdown")
    print(f"[LOG] User ID: {user.id} — Username: @{user.username}")

# 🚀 Команда: /start — приветствие и список доступных команд
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Привет, друг! 👋\n"
        "Я — твой надёжный помощник по ID в Telegram 😎\n\n"
        "Вот мои команды:\n"
        "🆔 /get_my_id — покажу твой Telegram ID\n"
        "💬 /get_chat_id — отправлю ID этого чата или группы\n"
        "📖 /help — расскажу, что ещё я умею\n\n"
        "🤖 Хочешь узнать ID своей группы?\n Просто добавь меня в группу, и я покажу её ID! @Oli3djonIDbot\n\n"
        
    )
    await update.message.reply_text(text)

# 🆘 Команда: /help — справка
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚙️ Мои команды:\n"
        "👋 /start — расскажу, кто я такой\n"
        "🆔 /get_my_id — покажу твой Telegram ID\n"
        "💬 /get_chat_id — отправлю ID этого чата или группы\n\n"
        "🤖 Хочешь узнать ID своей группы?\n Просто добавь меня в группу, и я покажу её ID! @Oli3djonIDbot\n\n"
    )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Регистрируем команды
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("get_my_id", get_my_id))
    app.add_handler(CommandHandler("get_chat_id", get_chat_id))

    print("✅ Бот запущен. Можно писать ему в Telegram.")
    app.run_polling()

if __name__ == "__main__":
    main()
