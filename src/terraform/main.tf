resource "openstack_compute_keypair_v2" "my-cloud-key" {
  name       = "grp14key"
  public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDEyR8OwjwtjLTJzs8jRPVpoHJ1RcDXYaYgHSurX3MPO5lh+wCwy1fPyoOPagRglZUe11MMflD/s6YIjmjHXWto/I7nIIb+EtiF5RLFtsiVYU1kNP2lDaBImKvl8M4AwoWGv+dUZGCx71oZjmZCjShXi$
}
resource "openstack_compute_instance_v2" "master" {
  name            = "Group14_master-vm"
  image_name      = "Ubuntu 18.04 LTS (Bionic Beaver) - latest"
  flavor_name     = "ssc.small"
  key_pair        = "${openstack_compute_keypair_v2.my-cloud-key.name}"
  security_groups = ["default"]
  user_data       = "${file("master.conf")}"

  network {
    name = "SNIC 2019/10-32 Internal IPv4 Network"
  }
}

resource "openstack_compute_instance_v2" "wrkr" {
  name            = "Group14_worker-${count.index}"
  image_name      = "Ubuntu 18.04 LTS (Bionic Beaver) - latest"
  flavor_name     = "ssc.small"
  key_pair        = "${openstack_compute_keypair_v2.my-cloud-key.name}"
  security_groups = ["default"]
  user_data       = "${file("worker.conf")}"
  count           = 2

  network {
    name = "SNIC 2019/10-32 Internal IPv4 Network"
  }
}


