"""
flask shell
    仔细思考他对实现逻辑。
    MongoEngine与app的绑定。
    继承类
"""
from flask import Flask
from mongoengine import *
from flask_mongoengine import MongoEngine
import datetime

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb+srv://LeeCQ:1234@cluster0-l3jqa.azure.mongodb.net/test?retryWrites=true',
    'db': 'test',
    'username': 'LeeCQ',
    'password': '1234',
}

db = MongoEngine(app=app)


class Book(db.Document):
    title = StringField(max_length=100, required=True)
    price = DecimalField(default=0.0)
    tags = ListField(StringField(max_length=20))
    available = BooleanField(default=True)
    date = DateField(default=datetime.datetime.now)


@app.route('/')
def home():
    return "Hello Word"
