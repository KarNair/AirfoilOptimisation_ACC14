import sys
import subprocess

cmd1= 'docker images --format "{{.ID}}"'
process = subprocess.Popen(cmd1.split(), stdout=subprocess.PIPE)  #20
dockerImg, error = process.communicate() 

#print("dockerImg dirty", dockerImg)

dockerImg = dockerImg.decode("utf-8"). replace('"','')
dockerImg = dockerImg.strip()
dockerImg = dockerImg.replace('f99661bca197','')
dockerImg = dockerImg.strip()
#print("dockerImg decoded  ", dockerImg)

cmd2= 'docker run -d -t --name=Ajjirufoidl2 '+dockerImg
proc = subprocess.Popen(cmd2.split(), stdout=subprocess.PIPE)   #subprocess.run(cmd2)
res, error = proc.communicate() 

cmd3 = 'docker ps --format "{{.ID}}"'
proc3 = subprocess.Popen(cmd3.split(), stdout=subprocess.PIPE)   #subprocess.run(cmd2)
#res, error = proc.communicate() 

#process2 = subprocess.Popen(cmd3.split(), stdout=subprocess.PIPE)  #20

dockerID, error = proc3.communicate() 
#print("dockerID", dockerID)

dockerID = dockerID.decode("utf-8"). replace('"','')
dockerID = dockerID.strip()

#print("dockerID decoded  ", dockerID)

cmd4 = "docker exec -t -i " +dockerID+ " /bin/bash &"
#print(cmd4)
proc = subprocess.Popen(cmd4.split(), stdout=subprocess.PIPE)   #subprocess.run(cmd2)
res, error = proc.communicate() 

#subprocess.run(cmd4)
