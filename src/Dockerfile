FROM fenics/stable

WORKDIR Airfoil
COPY ./AirfoilOptimisation_ACC14/project_description/murtazo.tgz /Airfoil/murtazo.tgz
RUN apt-get -y update
RUN apt-get -y upgrade
RUN tar zxvf /Airfoil/murtazo.tgz
RUN tar zxvf /Airfoil/murtazo/cloudnaca.tgz
RUN tar xvf /Airfoil/murtazo/navier_stokes_solver.tar
WORKDIR /Airfoil/murtazo/navier_stokes_solver/src
RUN ./compile_forms
WORKDIR /Airfoil/murtazo/navier_stokes_solver
RUN cmake .
RUN make -j 2

WORKDIR /Airfoil/murtazo/cloudnaca
RUN apt-get -y install gmsh python-numpy
RUN sed -i 's|GMSHBIN="/Applications/Gmsh.app/Contents/MacOS/gmsh"|GMSHBIN="/usr/bin/gmsh"|g' ./runme.sh


ENV TERM xterm
CMD ["/bin/sh"]
