

cmd1= 'docker images --format "{{.ID}}"'
process = subprocess.Popen(cmd1.split(), stdout=subprocess.PIPE)  #20
dockerImg, error = process.communicate() 

print("dockerImg", dockerImg)

dockerImg = dockerImg.decode("utf-8"). replace('"','')
dockerImg = dockerImg.strip()

print("dockerImg decoded  ", dockerImg)

cmd2= 'docker run -d -t --name = Airfoil '+dockerImg
subprocess.run(cmd2)


cmd3 = 'docker docker ps --format "{{.ID}}"
process2 = subprocess.Popen(cmd3.split(), stdout=subprocess.PIPE)  #20

dockerID, error = process2.communicate() 
print("dockerID", dockerID)

dockerID = dockerID.decode("utf-8"). replace('"','')
dockerID = dockerID.strip()

print("dockerID decoded  ", dockerID)

cmd4 = "docker exec -t -i " +dockerID+ " /bin/bash"
subprocess.run(cmd4)