#tasks.py
from celery import Celery, group
import json

#app = Flask(__name__)
#app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@localhost//')
#app.config_from_object('celeryconfig')
#app = Celery('tasks', backend='rpc://', broker='pyamqp://acc14:accg14@localhost:5672/g14host')
app = Celery('tasks', backend='rpc://', broker='pyamqp://myuser:mypassword@localhost:5672/myvhost')

@app.task(trail=True)  #11
def mapper(arguments):
        import sys
        import subprocess
        str1 = ""
        for elem in  arguments:
                str1+=str(elem)
                str1+=" " 
        bs= 'docker ps --format "{{.ID}}"'
        process = subprocess.Popen(bs.split(), stdout=subprocess.PIPE)  #20
        dockerID, error = process.communicate() 
        print("dockerID", dockerID)
        dockerID = dockerID.decode("utf-8"). replace('"','')
        print("dockerID decoded  ", dockerID)

        bashCommand = "docker exec -w /home/fenics/shared/murtazo/navier_stokes_solver/ " +dockerID.strip()  + " ./airfoil "+ str1+  " ../cloudnaca/msh/r1a9n200.xml"
        print(bashCommand)
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        
        #print("error was ",error)
        dirname= "results"
        for elem in str1:
               dirname+=elem.strip() 
        print("dirname = ",dirname)
        print("dockerID  after dirname", dockerID)
        bashCommandMKDIR= "mkdir " +  dirname
        processMkdir = subprocess.Popen(bashCommandMKDIR.split(), stdout=subprocess.PIPE)
        output, error = processMkdir.communicate()
        print("dockerID  before CP", dockerID)
        bashCommandCP = "docker cp " + dockerID.strip()+ ":/home/fenics/shared/murtazo/navier_stokes_solver/results/  " + dirname
        print(bashCommandCP)
        processCP = subprocess.Popen(bashCommandCP.split(), stdout=subprocess.PIPE)
        output, error = processCP.communicate()

        return json.dumps(error)
