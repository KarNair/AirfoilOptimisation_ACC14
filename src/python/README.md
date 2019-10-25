**To start a new docker container:**
root@gr14-new:~# docker run -d -p 5000:5000 -td -v $(pwd):/home/fenics/shared -w /home/fenics/shared quay.io/fenicsproject/stable:current

**To see if there are running containers**
root@gr14-new:~# docker ps
CONTAINER ID        IMAGE                                                 COMMAND                  CREATED               STATUS                 PORTS                             NAMES
498c3c534c8c        quay.io/fenicsproject/stable:current   "/sbin/my_init --qui…"   7 seconds ago       Up 4 seconds        0.0.0.0:5000->5000/tcp   jovial_murdock

**Copy the CONTAINER ID from above in the following command to reconnect to a container**
root@gr14-new:~# docker exec -t -i 498c3c534c8c /bin/bash

**All the code, incl. REST API and ./airfoil is here:**
root@498c3c534c8c:/home/fenics/shared# cd murtazo/navier_stokes_solver/


**To run the python code:**

sudo pkill -KILL -u rabbitmq  <- only if  you have an old rabbit running and it's behaving weirdly
sudo service rabbitmq-server start 
screen celery -A airfoil_tasks worker --loglevel=info  <- check first you don't already have a celery worker  working 
Then CTRL+a+CTRL+d   to return to main screen from celery

python3 flask_airfoil_tasks.py

**To send a request from the end-user to the VM**
curl -i http://130.238.28.73:5000/airfoil/api/base?input=1,1,1,1

