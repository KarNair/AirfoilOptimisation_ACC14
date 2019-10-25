## Python Launch VM script using user_data
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
##Set input parameters
user_data = open(os.getcwd()+'/cloudconfig.txt')  #Change the user_data file here
image = nova.glance.find_image('Ubuntu 18.04 LTS (Bionic Beaver) - latest')
flavor = nova.flavors.find(name="ssc.small")
networks = neutron.list_networks(name='SNIC 2019/10-32 Internal IPv4 Network') #Change the network here
network_id = networks['networks'][0]['id']
nics = [{'net-id': network_id}]
##Create the instance and boot with cloud-init configuration
instance = nova.servers.create(name="grp14_master_vm", image=image.id, flavor=flavor, key_name="group14", userdata=user_data, nics=nics) #Change the instance and key name here
# Poll at 5 second intervals, until the status is no longer 'BUILD'
status = instance.status
while status == 'BUILD':
    time.sleep(5)
    # Retrieve the instance again so the status field updates
    instance = nova.servers.get(instance.id)
    status = instance.status
print ("status: %s" % status)
