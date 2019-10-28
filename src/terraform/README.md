## Cloud Cluster Deployment using Terraform

This folder defines infrastructure-as-code using Terraform. Terraform templates creates real cloud-agnostic and allows a single configuration to be used to manage multiple providers, and to even handle cross-cloud dependencies.

### Terraform Installation on Ubuntu 18.04

Update the system and packages

> sudo apt-get update

Install the terraform

> sudo snap install terraform

Verify

> terraform -v

### Set the OpenStack Environment Varibles

Log in to the OpenStack dashboard,Download the OpenStack RC file and save it.

>source ./SNICopenrc.sh

