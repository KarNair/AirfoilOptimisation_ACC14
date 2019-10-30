FROM quay.io/fenicsproject/stable:current

USER root
RUN mkdir Airfoil
WORKDIR Airfoil
RUN git clone https://github.com/KarNair/AirfoilOptimisation_ACC14.git
COPY /AirfoilOptimisation_ACC14/project_description/murtazo.tgz /Airfoil/murtazo.tgz
COPY /AirfoilOptimisation_ACC14/project_description/murtazo/cloudnaca  /Airfoil/murtazo/cloudnaca
COPY /AirfoilOptimisation_ACC14/project_description/murtazo/navier_stokes_solver  /Airfoil/murtazo/navier_stokes_sol$
#RUN apt-get -y update

#RUN apt-get -y upgrade
#RUN tar xzvf /Airfoil/murtazo.tgz
#RUN tar xvf  /Airfoil/murtazo/cloudnaca.tgz
#RUN tar xvf /Airfoil/murtazo/navier_stokes_solver.tar
WORKDIR /Airfoil/murtazo/navier_stokes_solver/src
RUN ./compile_forms
WORKDIR /Airfoil/murtazo/navier_stokes_solver
RUN cmake .
RUN make -j 2

WORKDIR /Airfoil/murtazo/cloudnaca
#RUN apt-get -y update
#RUN apt-get -y install gmsh python-numpy
