## Cloud Cluster Deployment using Terraform

This folder defines infrastructure-as-code using Terraform. Terraform templates creates real cloud-agnostic and allows a single configuration to be used to manage multiple providers, and to even handle cross-cloud dependencies.

### Terraform Installation on Ubuntu 18.04

Update the system and packages

> sudo apt-get update

Install the terraform

> sudo snap install terraform

Verify

> terraform -v

### Install the OpenStack and set the Environment Variables

> sudo apt  install python3-openstackclient

Log in to the OpenStack dashboard,Download the OpenStack RC file and save it.

> source ./SNICopenrc.sh

### Generate the Public Key 

To Generate the Public key, we can use the private key which created in OpenStack Dashboard

> ssh-keygen -y -f .ssh/group14.pem

### Create the two Terraform Templates to setup the VM cluster.

```
providers.tf
main.tf
```
providers.tf

```
#Terraform Proivders
provider "openstack" {}
```
main.tf

```
#Specify resources details here

resource "openstack_compute_keypair_v2" "my-cloud-key" {
  name       = "accg14key"
  public_key = "ssh-rsa AAAAB3NzaC1y....
  }
  resource "openstack_compute_instance_v2" "wrkr" {
  name            = "wrkr-${count.index}"
  image_name      = "Ubuntu 18.04 LTS (Bionic Beaver) - latest"
  flavor_name     = "ssc.small"
  key_pair        = "${openstack_compute_keypair_v2.my-cloud-key.name}"
  security_groups = ["default"]
  user_data       = "${file("worker.conf")}"
  count           = 3  ***#Number of Workers to increase or decrease****

  network {
    name = "SNIC 2019/10-32 Internal IPv4 Network"
  }
}

  ```
  
  
