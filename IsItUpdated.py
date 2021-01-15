from dotenv import load_dotenv
import os
import discord

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")

def main():
    print("Hello World!")
    print(f"Discord Client ID: {CLIENT_ID}")


if (__name__ == '__main__'):
    main()
    client = discord.Client()
    client.run(CLIENT_ID)
