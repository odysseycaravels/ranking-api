# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  config.vm.box = "debian/buster64"

  config.vm.network "forwarded_port", guest: 5432, host: 5432

  config.vm.provider "virtualbox" do |vb|
    # Name as displayed in VirtualBox
    vb.name = "vagrant_debian10_postgresql_rankingapi"
    # Display the VirtualBox GUI when booting the machine
    # vb.gui = true

    # Customize the amount of memory on the VM:
    vb.memory = "2048"
  end

  config.ssh.insert_key = false

  config.vm.provision "shell", inline: <<-SHELL
    echo "[ Updating system ]"
    apt update
    apt upgrade -y
    echo "[ Installing postgres ]"
    apt install -y postgresql-11 postgresql-contrib
    echo "[ Configuring and starting PostgreSQL ]"
    pg_ctlcluster 11 main start
	# Configure network access
	echo "[ Configuring postgresql network access ]"
    echo 'listen_addresses = '"'"'*'"'" >> /etc/postgresql/11/main/postgresql.conf
    echo 'host    all             all             10.0.0.0/8            md5' >> /etc/postgresql/11/main/pg_hba.conf
	echo 'host    all             all             192.168.0.0/16        md5' >> /etc/postgresql/11/main/pg_hba.conf
	echo 'host    all             all             172.16.0.0/12         md5' >> /etc/postgresql/11/main/pg_hba.conf
	# Alternatively, you can do 0.0.0.0/0 to accept from anywhere.
    echo "[ Creating vagrant user and database ]"
    cd /  # Just to avoid errors about postgres not having directory access
    echo "CREATE ROLE vagrant CREATEDB CREATEROLE LOGIN PASSWORD 'vagrant'" | sudo -u postgres psql -a -f -
    echo "ALTER USER vagrant WITH SUPERUSER" | sudo -u postgres psql -a -f -
    echo "CREATE DATABASE vagrant OWNER vagrant" | sudo -u postgres psql -a -f -
    echo "ALTER USER postgres WITH PASSWORD 'POSTGRES'" | sudo -u postgres psql -a -f -
    echo "[ Restarting postgresql service ]"
    pg_ctlcluster 11 main restart
    echo "[ Done! ]"
  SHELL
end