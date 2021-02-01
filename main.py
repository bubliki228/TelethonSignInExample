from telethon import TelegramClient
from telethon.errors.rpcerrorlist import SessionPasswordNeededError
import asyncio

API_ID = 123456
API_HASH = 'abcd125qwerty885448'

loop = asyncio.get_event_loop()

phone = input('Enter phone')

client = TelegramClient(
    'client',
    api_id=API_ID,
    api_hash=API_HASH
)


async def main():
    global client
    await client.connect()
    await client.send_code_request(phone=phone)
    try:
        code = input('Code: ')
        await client.sign_in(code=code)
    except SessionPasswordNeededError:
        twofa = input('Enter 2fa: ')
        await client.sign_in(password=twofa)

    print((await client.get_me()).username)


if __name__ == '__main__':
    loop.run_until_complete(main())
