from flask import Flask,jsonify
from pandas import Timestamp
import random
import datetime

from flask import  stream_with_context,request,Response
server = Flask(__name__)

@server.route('/', methods=['GET','POST'])
def data_generate():
    timestapm= datetime.datetime.now().isoformat()
    lat= random.uniform(35,45)
    lon= random.uniform(35,45)
    sensor_1= random.uniform(10,30)
    sensor_2= random.uniform(30,50)
    sensor_3= random.uniform(50,70)
    sensor_4= random.uniform(70,100)


    return jsonify(
        datetimenow=timestapm,
        lat=lat,
        lon=lon,
        sensor_1=sensor_1,
        sensor_2=sensor_2,
        sensor_3=sensor_3,
        sensor_4=sensor_4
    )
if __name__=="__main__":
    server.run(host='0.0.0.0', port=8005)