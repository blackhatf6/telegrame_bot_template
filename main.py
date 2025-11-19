import asyncio
import aiohttp
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from colorama import Fore, Style, init
import cloudscraper
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)
init(autoreset=True)

TOKEN = "YOUR_TOKEN_HERE"
#PROXY = "http://192.168.43.1:8181"

BANNER = f"""
{Fore.BLUE}{Style.BRIGHT}
████████╗███████╗██╗      ███████╗ ██████╗ █████╗ ███╗   ███╗
╚══██╔══╝██╔════╝██║      ██╔════╝██╔════╝██╔══██╗████╗ ████║
   ██║   █████╗  ██║      █████╗  ██║     ███████║██╔████╔██║
   ██║   ██╔══╝  ██║      ██╔══╝  ██║     ██╔══██║██║╚██╔╝██║
   ██║   ███████╗███████╗███████╗╚██████╗██║  ██║██║ ╚═╝ ██║
   ╚═╝   ╚══════╝╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝
{Fore.RED}{Style.BRIGHT}          Telegram Bot v1.0
{Style.RESET_ALL}
"""

print(BANNER)
print(f"{Fore.GREEN}[✓] Bot Started...")
print(f"{Fore.YELLOW}Token Loaded: {Fore.WHITE}{TOKEN[:10]}********")

COMMANDS = {
    "start": "เริ่มต้นใช้งานบอท",
    "help": "วิธีใช้บอททั้งหมด"
}

async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("📌 รายการคำสั่ง", callback_data="help_menu")]
    ])
    await update.message.reply_text("สวัสดีครับ 👋\nใช้ปุ่มด้านล่างเพื่อดูเมนู", reply_markup=keyboard)

async def help_cmd(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    text = "🧾 **รายการคำสั่งทั้งหมด**\n\n"
    for cmd, desc in COMMANDS.items():
        text += f"/{cmd} — {desc}\n"
    await update.message.reply_text(text)

async def callback_handler(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    data = q.data

    if data == "help_menu":
        text = "📌 **เมนูคำสั่ง**\n\n"
        for cmd, desc in COMMANDS.items():
            text += f"/{cmd} — {desc}\n"
        await q.answer()
        await q.edit_message_text(text)
    else:
        await q.answer("ไม่มีคำสั่งนี้")

def register_commands(app):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    register_commands(app)
    app.add_handler(CallbackQueryHandler(callback_handler))

    print("Bot is running...")
    app.run_polling()
