import json
import os
import shutil
from pymongo import MongoClient
from pymongo.server_api import ServerApi
# from models import Authors, Quotes
input_directory = 'input'
arch_directory = 'arch'


def create_db_load_date(name_db):
    uri = f"mongodb+srv://user_python:54321@cluster0.yypw24v.mongodb.net/{name_db}?retryWrites=true&w=majority"
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client[name_db]

    for file in os.listdir(input_directory):
        if file.endswith(".json"):
            if file.startswith("authors"):
                collection_name = file.split('.')[0]
                collection = db[collection_name]
                with open(os.path.join(input_directory, file), "r", encoding="utf-8") as af:
                    authors_date = json.load(af)
                    collection.insert_many(authors_date)
                
            if file.startswith("quotes"):
                with open(os.path.join(input_directory, file), "r", encoding="utf-8") as qf:
                    file_date = json.load(qf)
                    for quote_data in file_date:
                        author_fullname = quote_data.get('author')
                        author = db.authors.find_one({'fullname': author_fullname})
                        # print(author)
                        quote_data['author'] = author['_id']
                        db.quotes.insert_one(quote_data) 
 
        shutil.move(f'input/{file}', f'arch/{file}')

    client.close()
    return 'OK'


if __name__ == '__main__':
    create_db_load_date("hw81")
