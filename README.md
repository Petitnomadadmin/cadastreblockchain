## Install development environment

Launch VM provisioning and connect through ssh

    git clone git@github.com:Petitnomadadmin/cadastreblockchain.git
    cd cadastreblockchain/vm
    vagrant up && vagrant ssh

Use folder synchronisation in another prompt if you're in dev mode with no autosync
    vagran rsync-auto

To trash the VM (from your host in the vm folder):

    vagrant halt && vagrant destroy
    rm -rf .vagrant
