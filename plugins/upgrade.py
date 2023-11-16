"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**VIP 1 ** 
	Daily  Upload  limit 50GB
	Price Rs 1231  🇮🇳/🌎 15$  per Year 
	
	**VIP 2 **
	Daily Upload limit Unlimited 
	Price Rs  2051  🇮🇳/🌎 25$  per Year
	
	
	Pay Using Upi I'd ```ravikohli.ind@ibl```
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("𝙰𝙳𝙼𝙸𝙽 🛂",url = "https://t.me/R_KOHLI")], 
        			[InlineKeyboardButton("𝚄𝙿𝙳𝙰𝚃𝙴🌎",url = "https://t.me/movie_a1"),
        			InlineKeyboardButton("𝙹𝙾𝙸𝙽 𝙼𝙾𝚅𝙸𝙴",url = "https://t.me/movie_on1")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**VIP 1 ** 
	Daily  Upload  limit 50GB
	Price Rs 1231  🇮🇳/🌎 15$  per Year 
	
	**VIP 2 **
	Daily Upload limit Unlimited
	Price Rs  2051  🇮🇳/🌎 25$  per Year
	
	
	Pay Using Upi I'd ```ravikohli.ind@ibl```
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("𝙰𝙳𝙼𝙸𝙽 🛂",url = "https://t.me/R_KOHLI")], 
        			[InlineKeyboardButton("𝚄𝙿𝙳𝙰𝚃𝙴🌎",url = "https://t.me/movie_a1"),
        			InlineKeyboardButton("𝙹𝙾𝙸𝙽 𝙼𝙾𝚅𝙸𝙴",url = "https://t.me/movie_on1")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
