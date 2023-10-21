from mongoengine import connect
from mongoengine import Document, StringField, ListField, CASCADE, ReferenceField, DateTimeField

connect(
    host=f"mongodb+srv://user_python:54321@cluster0.yypw24v.mongodb.net/", ssl=True)


class Authors(Document):
    fullname = StringField(required=True)
    born_date = StringField(max_length=30)
    born_location = StringField(max_length=50)
    description = StringField(max_length=None)


class Quotes(Document):
    tags = ListField(StringField(max_length=30))
    author = ReferenceField(Authors, reverse_delete_rule=CASCADE)
    quote = StringField(max_length=None)


def models_db(name_db):
    connect(
        host=f"mongodb+srv://user_python:54321@cluster0.yypw24v.mongodb.net/{name_db}", ssl=True)


if __name__ == '__main__':
    models_db('hw9')
