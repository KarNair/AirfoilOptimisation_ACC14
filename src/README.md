To use the Dockerfile as source, run (from the same location as the Dockerfile):

    docker build .  //OR  sudo docker build .

Once this completes it'll say something like:

    Successfully built b7bec6991e53

Then you start the container:
    
    docker run -d -it  --name=first b7bec6991e53
    
Lastly, do docker ps to get container ID, and use it:
    
    docker exec -t -i ajkdbe1e53 /bin/bash
   

Commmand Line to run the vm-launch-userdata.py

`python3 vm-launch-userdata.py 'cloudconfig.txt'[cloud_init_file] 'SNIC 2019/10-13 Internal IPv4 Network'[Cluster_Network] 'g4master'[instance_name] 'Ubuntu 18.04 LTS (Bionic Beaver) - latest' [image_name] 'group14'[key_name] 'ssc.small'[flavor_name]`


