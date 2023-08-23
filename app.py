import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove



API_ID = "27957041"
API_HASH = "2ae1c9912cd2efdecae7f0208994f0b0"
BOT_TOKEN = "6648521609:AAEp0nq17i2WdLgCnf1sa_Yii3bGoYW8epw"

bot = Client("STARK",api_id=API_ID,api_hash=API_HASH,bot_token=BOT_TOKEN)

START_BUTTON = [
    [
        InlineKeyboardButton("Free Server 1", url="https://t.me/Lochakpochak"),
        InlineKeyboardButton("Free Server 2", url="https://t.me/Soupboy_single") 
    ],
    [
        InlineKeyboardButton("Close", url="https://t.me/universe_we_are")  
]]


TEXT = """
[🚩🚩🚩 click here  🚩🚩🚩](https://t.me/we_are_universee)

Yunga bots yenga vps la run pandrom nu sonom la 😍

🔤🔤🔤🔤 - 🐻 

Process: 

😵. Deploy pannaum nu sonna avangaluku intha services

😵. Yenna spec nu sollunga 

😵. Vps server yungaluku venum na kuduturvom illana yenga kitta irrukum .

😵. Repo la editing pannanum na charge vanguvom .

Important ❤️

🚩 Nambo universe symbol ha yunga bots la potukanum 

     Or ,

🚩 Bio la running under 
Universe Networks nu link potukanum ..

    Or, 

🚩 Sudo la add pannikonga ❤️


Ok na ! 

📔 - kurivhi vechikonga 😐
@Lochakpochak
@Soupboy_single
"""

@bot.on_message(filters.command("start") & filters.private)
async def start(bot, update):
    await bot.send_message(chat_id=int(-1001844914241),text=TEXT,reply_markup=InlineKeyboardMarkup(START_BUTTON),disable_web_page_preview=True)
    print("done")



if __name__ == "__main__":
    bot.run()