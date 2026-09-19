import os
from dotenv import load_dotenv
from pymongo import MongoClient

# 1. Load the secret password
load_dotenv()
uri = os.getenv("MONGO_URI")

# 2. Connect to the Client (The Cluster)
client = MongoClient(uri)

# 3. Access the Database (e.g., "school")
# If it doesn't exist, Mongo creates it automatically when you insert data.
db = client["school"]

# 4. Access the Collection (e.g., "students")
students = db["students"]

# 5. Test the connection
try:
    client.admin.command('ping')
    print("Successfully connected to MongoDB!")
except Exception as e:
    print(e)