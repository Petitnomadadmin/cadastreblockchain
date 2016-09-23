## Install development environment

Launch VM provisioning and connect through ssh

    git clone git@github.com:Petitnomadadmin/cadastreblockchain.git
    cd cadastreblockchain/vm
    vagrant up && vagrant ssh

Trash the VM (from yout host in the vm folder):

    vagrant halt && vagrant destroy
    rm -rf .vagrant

