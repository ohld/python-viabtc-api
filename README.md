# python-viabtc-api
API Wrapper for ViaBTC exchange server 

## Install exchange

For me the easiest way to install the exchange was found in [bitlum](https://github.com/bitlum)'s fork of the original [ViaBTC](https://github.com/viabtc/viabtc_exchange_server) repository. You need `docker` and `docker-compose` (up-to-date) to launch this installation script. 

``` bash
git clone https://github.com/bitlum/viabtc_exchange_server
cd viabtc_exchange_server/docker
docker-compose up
```

That's it! It successfully run on Ubuntu server, but failed on macOS (there were some disk path errors that I balieve can be easily fixed if you are familiar with docker or stackoverflow).

## Connect to exchange local network

`Docker-compose` creates the local net for all dockers images. Take a look at [docker-compose file](https://github.com/bitlum/viabtc_exchange_server/blob/master/docker/docker-compose.yml): you may notice the local ip addresses near every docker container. We will use the address of `accesshttp` container to make API requests. 

As all of that stuff is happening on the remote server's local network, we need to make some port forwarding from it to out development machine (in my case this is my macbook laptop):

``` bash
ssh user@<your-server-id-address-> -L 8080:192.168.18.45:8080 -N -f
```

where `192.168.18.45` is the ip address of `accesshttp` container and `8080` is its port. 

And now you can send API requests to `exchange_url = "http://localhost:8080"`

## Python API installation

This API is very simple. The installation is just the downloading sources from github

``` bash
git clone https://github.com/testnet-exchange/python-viabtc-api
pip3 install requests 
```

The examples of requests making you han find in [examples.py](https://github.com/testnet-exchange/python-viabtc-api/blob/master/example.py) file.

----

I spent a few hours to figure out how to run the exchange and make requests to it. If this tutorial helped you, smash the star button at the top of the page. And fell free to make Pull Requests with some additional functionallity. 

*Happy Coding!*
