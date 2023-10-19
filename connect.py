import pymongo


def connect_db(name_db):
    client = pymongo.MongoClient(
        "mongodb+srv://user_python:54321@cluster0.yypw24v.mongodb.net/?retryWrites=true&w=majority")

    database_name = name_db
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
    print(connect_db('hw8_1'))
