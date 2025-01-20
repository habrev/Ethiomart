from telethon import TelegramClient, events
import asyncio

# Replace these with your credentials from My Telegram
api_id = '24955986'
api_hash = '6208be82b9b8b0988106a8b5bb2f3542'
phone_number = '+251995062829'  # Needed only for first login

# Channels to scrape messages from (either usernames or IDs)
channel_list = [
    '@marakibrand',  # Replace with actual channel usernames or IDs
    '@AwasMart',
    '@fashiontera',
    '@Shewabrand',
    '@nevacomputer'

]

# Initialize the Telethon client
client = TelegramClient('session_name', api_id, api_hash)

# Function to log in (only required during first run)
async def authenticate():
    if not await client.is_user_authorized():
        await client.start(phone=phone_number)
        print("Authentication successful!")

# Function to fetch messages from channels
# Function to fetch messages and download images
async def fetch_messages():
    for channel in channel_list:
        print(f"Fetching messages from: {channel}")
        try:
            # Fetch the last 100 messages (adjust limit as needed)
            async for message in client.iter_messages(channel, limit=100):
                # Save text messages
                if message.text:
                    print(f"Message from {channel}: {message.text}")
                    with open(f"{channel}_messages.txt", "a", encoding="utf-8") as f:
                        f.write(f"Sender: {message.sender_id}, Message: {message.text}\n")
                
                # Save media files (e.g., images)
                if message.media:
                    print(f"Downloading media from {channel}")
                    file_path = await message.download_media(file=f"{channel}_media/")
                    print(f"Media saved to {file_path}")
        except Exception as e:
            print(f"Error fetching messages from {channel}: {e}")

# Main function to run everything
async def main():
    await authenticate()
    await fetch_messages()

# Run the script
with client:
    client.loop.run_until_complete(main())
