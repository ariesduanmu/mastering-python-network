## generate pub-pri rsa key on the host machine

* `ssh-keygen -t rsa`

## copy the public key to target host

* `ssh-copy-id root@192.168.2.101`

## usage

### ansible ping test

* `./ansible_simple.sh`

### ansible df script

* `./ansible_df.sh`

### ansible juniper test

* `./ansible_juniper.sh`
