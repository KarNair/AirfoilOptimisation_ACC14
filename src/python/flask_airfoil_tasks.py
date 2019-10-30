#flask_tasks.py
#!flask/bin/python
from flask import Flask, jsonify,request
import subprocess
import sys
from airfoil_tasks import mapper
from time import sleep
from celery.result import ResultBase

app = Flask(__name__)

@app.route('/airfoil/api/base',methods=['GET'])
def tasks():
        data= request.args.get('input','1,0.0001,1.,0.1')
        files= request.args.get('xmls','1')
        vars_split= data.split(",")
        if len(vars_split)==4:
         
                #if isinstance(float(vars_split[0]),float) and isinstance(vars_split[1],float) and isinstance(vars_split[2],float) and isinstance(vars_split[3],float):
                try:
                        air_vars =  [float(x) for x in vars_split]
                except:
                        return "The arguments you provided were not numbers."
                
                words=mapper.delay(air_vars)
        else:
                words=mapper.delay('1,0.0001,1.,0.1'.split(","))
        #words=mapper.delay(air_vars)


        while not words.ready():
                sleep(1)
                print('.')                      
        #print(words.get())
        
        error=words.get()
        success_msg="The computation is done. Contact admin to get the results. "
        return success_msg #words.get()

#tasks = app.register_task(tasks())

if __name__ == '__main__':
        app.run(host='0.0.0.0',debug=True)

