from flask import Flask
from flask_cors import CORS
from bson.json_util import dumps
from pymongo import MongoClient
import json

client = MongoClient('127.0.0.1', 27017)

db = client.auto_complete

collection = db.auto_complete

app = Flask(__name__)
CORS(app)
@app.route('/',methods= ['GET'])
def home():
    return {"data":'Hello, World!'}

@app.route('/test', methods = ['GET'])
def home2():
   dataList = list(collection.find({}).limit(3))
   return {"data":json.loads(dumps(dataList))}

if __name__ == '__main__':
    app.run(debug=True) #저장할때마다 변경된 것을 인식하고  다시 실행 함