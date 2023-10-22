from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://user_python:54321@cluster0.yypw24v.mongodb.net/?retryWrites=true&w=majority"


def connect_db(name_db, uri):
    uri = uri
    client = MongoClient(uri, server_api=ServerApi("1"))
    database_name = client[name_db]
    if database_name in client.list_database_names():
        print(f"База данных {database_name} существует.")
        try:
            client.admin.command('ping')
            return "Pinged your deployment. You successfully connected to MongoDB!"
        except Exception as e:
            return e
    else:
        print(f"База данных {database_name} не существует.")

    client.close()


if __name__ == '__main__':
    uri = "mongodb+srv://user_python:54321@cluster0.yypw24v.mongodb.net/?retryWrites=true&w=majority"
    print(connect_db('hw777', uri))
