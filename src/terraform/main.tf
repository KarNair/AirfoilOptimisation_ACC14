resource "openstack_compute_keypair_v2" "my-cloud-key" {
  name       = "accg14key"
  public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDOk6VdPxND/vovKrZbvLl5ot8sLEB4SZxd2b9Xk6RIJMnLr9hd/PcFzNPrXh/t/ZG/uzUwlUl7s/+xFLxW8nYRutn7BOif9MZUgSU+n13tVgqHdnwIhbTERIoLgye39tlKk3DkRjWxJ0HZ9YzeC2cMSV2UniJ1qmzEpiZxlWSDJleEUVAjl12A9wqOw21pidXpwzSJ0aAsPYVDv2Pyufv7Fqf/xgJNVJzWiJGKiqdP0HE/khHSdz+ad7Ea/4u5QTkwj5n+PN43EmaCbroEBBf237tZMiEXrS3jlIjUVKXMM+Pga/XLwlTrYxZDLbDzbrxbDMYYj+P+py88wbYEiOBz"
}
resource "openstack_compute_instance_v2" "master" {
  name            = "master-vm"
  image_name      = "Ubuntu 18.04 LTS (Bionic Beaver) - latest"
  flavor_name     = "ssc.small"
  key_pair        = "${openstack_compute_keypair_v2.my-cloud-key.name}"
  security_groups = ["default"]
  user_data       = "${file("master.conf")}"

  network {
    name = "SNIC 2019/10-13 Internal IPv4 Network"
  }
}

resource "openstack_compute_instance_v2" "wrkr" {
  name            = "wrkr-${count.index}"
  image_name      = "Ubuntu 18.04 LTS (Bionic Beaver) - latest"
  flavor_name     = "ssc.small"
  key_pair        = "${openstack_compute_keypair_v2.my-cloud-key.name}"
  security_groups = ["default"]
  user_data       = "${file("worker.conf")}"
  count		  = 3

  network {
    name = "SNIC 2019/10-13 Internal IPv4 Network"
  }
}
