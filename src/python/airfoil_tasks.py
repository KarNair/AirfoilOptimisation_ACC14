#tasks.py
from celery import Celery, group
import json

#app = Flask(__name__)
#app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@localhost//')
#app.config_from_object('celeryconfig')
app = Celery('tasks', backend='rpc://', broker='pyamqp://acc14:accg14@localhost:5672/g14host')


@app.task(trail=True)
def mapper(arguments):
        import sys
        import subprocess
        str1 = ""
        for elem in  arguments:
                str1+=str(elem)
                str1+=" " 
        bashCommand = "./airfoil "+ str1+  " ../cloudnaca/msh/r2a15n200.xml"
        print(bashCommand)
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        
        print("error was ",error)

        return json.dumps(error)
