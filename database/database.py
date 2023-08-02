from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

class DataBase:
    def __init__(self) -> None:
        uri = os.getenv("URI")
        self.client = MongoClient(uri)
        self.ping()
        self.colection_voucher=  self.client.ShopeeDB['voucher']
        
    def ping(self):
        # Send a ping to confirm a successful connection
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)