from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.getenv("MONGODB_URI"))

print("Connected URI cluster info:")
print(client.address)

print("\nDatabases:")
for db_name in client.list_database_names():
    print("-", db_name)

print("\nCollections inside ticket_management:")
db = client["ticket_management"]
for collection_name in db.list_collection_names():
    print("-", collection_name)

print("\nTicket count in ticket_management.tickets:")
print(db["tickets"].count_documents({}))

print("\nTicket count in ticket_management.mahim:")
print(db["mahim"].count_documents({}))