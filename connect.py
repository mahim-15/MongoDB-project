from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv("MONGODB_URI")

client = MongoClient(uri)

try:
    client.admin.command("ping")
    print("MongoDB connected successfully!")
except Exception as e:
    print("Connection failed:")
    print(e)