import pymongo

from pprint import pprint


def find_db(name_db, name_col):
    uri = f"mongodb+srv://user_python:54321@cluster0.yypw24v.mongodb.net/{name_db}?retryWrites=true&w=majority"
    myclient = pymongo.MongoClient(uri)
    mydb = myclient[name_db]
    mycol = mydb[name_col]

    for x in mycol.find():
        pprint(x)


if __name__ == '__main__':
    find_db("hw81", 'quotes')
