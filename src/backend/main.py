from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient, TEXT
from pymongo.operations import IndexModel
import json


# MongoDB bağlantısı
client = MongoClient("mong************************17/")
db = client["search_db"]
collection = db["steam_db"]

'''
db.steam_db.createIndex({
    
    title: 'text',
    
  },
  {
    default_language: 'english',
    weights: {
      title:2,
      

    },
    name: 'custom_text_index',
    background: true,
    analyzer: 'lucene.whitespace',
    search_analyzer: 'lucene.standard'
  })
'''

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# GET metodunu işleyen basit bir endpoint
@app.get("/search/{search_text}")
def read_root(search_text):

    result = collection.find({"$text":{ "$search":f"{search_text}"}})

    result_list = []
    for news in result:
        news["_id"]=None
        result_list.append(news)

    return result_list

# POST metodunu işleyen basit bir endpoint
#@app.post("/search")
# def create_item(body:dict):
#     print(body)
#     return {"message": body["search_text"]}



