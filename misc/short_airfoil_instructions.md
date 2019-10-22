## To run airfoil on the VM where everything's installed, do the following:


ubuntu@gr14-new:~# sudo bash


root@gr14-new:~# docker run -td -v $(pwd):/home/fenics/shared -w /home/fenics/shared quay.io/fenicsproject/stable:current


root@gr14-new:~#docker ps   (—> get the container ID  from its output (for example: b202197d982e))


root@gr14-new:~# docker exec -t -i b202197d982e /bin/bash


Change to this folder: /home/fenics/shared/murtazo/cloudnaca# 


### My understanding is that this next command only needs to run once, and I have run it:

root@32c0881ed580:/home/fenics/shared/murtazo/cloudnaca#       ./runme.sh 0 30 10 200 3


Now you’ll have about 45 .msh files in /home/fenics/shared/murtazo/cloudnaca/msh ; and several  geo files in /home/fenics/shared/murtazo/cloudnaca/geo


Change to this folder:  /home/fenics/shared/murtazo/cloudnaca/msh#  


### Convert .msh files into .xml like this:
root@b202197d982e:/home/fenics/shared/murtazo/cloudnaca/msh#    dolfin-convert r2a15n200.msh r2a15n200.xml   


### Go to folder: /home/fenics/shared/murtazo/navier_stokes_solver and  run  airfoil on the new xml file you just created


root@b202197d982e:/home/fenics/shared/murtazo//navier_stokes_solver#  ./airfoil  10 0.0001 10. 1 ../cloudnaca/msh/r2a15n200.xml
