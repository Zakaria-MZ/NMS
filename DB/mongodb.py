import pymongo
from NMS.configs import config

def check_mongo_connection():
    client = None
    try:
        client = pymongo.MongoClient(config["mongodb"]["connectionString"], serverSelectionTimeoutMS=5000)
        server_info = client.admin.command("serverStatus")
        print("MongoDB version:", server_info['version'])
        print("Current server time:", server_info['localTime'])
    except pymongo.errors.ConnectionFailure:
        print("Failed to connect to MongoDB.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        if client:
            client.close()
