## Python Launch VM script using user_data
## Sample Command Line: python3 vm-launch-userdata.py 'master.conf'[cloud_init_file] 'SNIC 2019/10-13 Internal IPv4 Network'[Cluster_Network] 'g4master'[instance_name] 'Ubuntu 18.04 LTS (Bionic Beaver) - latest' [image_name] 'accgrp14'[key_name] 'ssc.small'[flavor_name]
import time, os, sys
import inspect
from os import environ as env

from novaclient import client
from neutronclient.v2_0 import client as nclient
import keystoneclient.v3.client as ksclient
from keystoneauth1 import loading
from keystoneauth1 import session

private_net = None
floating_ip_pool_name = None
floating_ip = None
cname=sys.argv[1]
nname=sys.argv[2]
iname=sys.argv[3]
ename=sys.argv[4]
kname=sys.argv[5]
fname=sys.argv[6]

loader = loading.get_plugin_loader('password')
auth = loader.load_from_options(auth_url=env['OS_AUTH_URL'],
                                username=env['OS_USERNAME'],
                                password=env['OS_PASSWORD'],
                                project_name=env['OS_PROJECT_NAME'],
                                user_domain_name=env['OS_USER_DOMAIN_NAME'],
                                project_domain_name=env['OS_USER_DOMAIN_NAME'])


sess = session.Session(auth=auth)
nova = client.Client(2.1, session=sess)
neutron = nclient.Client(session=sess)
master_data = open(os.getcwd()+'/'+cname)
#image='Ubuntu 18.04 LTS (Bionic Beaver) - latest'
image = nova.glance.find_image(ename)
flavor = nova.flavors.find(name=fname)
#name='SNIC 2019/10-13 Internal IPv4 Network'
networks = neutron.list_networks(name=nname)
network_id = networks['networks'][0]['id']
nics = [{'net-id': network_id}]
instance = nova.servers.create(name=iname, image=image.id, flavor=flavor, key_name=kname, userdata=master_data, nics=nics) 
# Poll at 5 second intervals, until the status is no longer 'BUILD'
status = instance.status
while status == 'BUILD':
    time.sleep(5)
    # Retrieve the instance again so the status field updates
    instance = nova.servers.get(instance.id)
    status = instance.status
print ("status: %s" % status)
