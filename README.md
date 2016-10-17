## Install development environment

Launch VM provisioning and connect through ssh

    git clone git@github.com:Petitnomadadmin/cadastreblockchain.git
    cd cadastreblockchain
    vagrant up && vagrant ssh

Use folder synchronisation in another shell if you're in dev mode with no autosync

    vagrant rsync-auto

To start Django server inside the VM

    cd /vagrant/cadastreblockchain
    ./manage.py runserver 0.0.0.0:8000

If you change something in ansible provisioning and you want to provision the vm, run this command as vagrant user:

    cd /vagrant && ansible-playbook /vagrant/provisioning/bootstrap.yml -i /vagrant/provisioning/hosts -vvvv

To trash the VM (from your host in the vm folder):

    vagrant halt && vagrant destroy
    rm -rf .vagrant
