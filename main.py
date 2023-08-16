# main.py

import os
import asyncio
from pyrogram import idle
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

from menfess import GenshinMF, MongoDB


async def main():
	load_dotenv()
	conn = AsyncIOMotorClient(os.getenv("MONGO_URI"))
	mongo = MongoDB(conn)
	await mongo.init()

	bot = GenshinMF(
		name="Piemon",
		api_id=int(os.getenv("API_ID")),
		api_hash=os.getenv("API_HASH"),
		bot_token=os.getenv("BOT_TOKEN"),
		plugins=dict(root="menfess.bot.plugins"),
		mongo=mongo
	)
	await bot.start()
	await idle()
	await bot.stop()


if __name__ == "__main__":
	asyncio.run(main())
