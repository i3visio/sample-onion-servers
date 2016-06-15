Installation instructions
=========================

More detailed installation instructions can be found in this file. This will use the official package uploaded to pip.

1.- Verifying the Python and pip installation
---------------------------------------------

First of all, on any system we should verify that we have a Python 2.7 installation and a Pip installation setup properly. Opening the terminal or the powershell, we can try the following to check your python installation:
```
python --version
```

Now it's the turn of the Package manager. Check that you have the pip version installed:
```
pip --version
```
If you get any errors at this point, you have several options:
* If your running Ubuntu or Debian-like systems, try sudo apt-get install python-pip
* In any case you can always download <https://bootstrap.pypa.io/get-pip.py> and install it manually. In Windows-like systems, you do NOT need to type sudo.
```
# Going to the downloads folder
python get-pip.py
```
You can do it at a time in Linux and MacOS systems:
```
# Downloading
wget https://bootstrap.pypa.io/get-pip.py
# Installing as root
sudo python get-pip.py
```
Try again and check if the new pip version is installed.


2 - Installing the application
------------------------------

Under Ubuntu-like systems, the system will need to solve the dependencies first:
```
sudo apt-get install tor
```
We can run then the Tor service:
```
tor
```
And then testing if it works:
```
# Getting your own public IP:
curl ifconfig.co
# Getting your Tor Public IP:
torify curl ifconfig.co 2> /dev/null
```

Once solved, we can clone the package and install the dependencies:
```
# Cloning the package...
git clone http://bitbucket.org/febrezo/onion-service
cd onion-service
# Solving Python depencies...
pip install -r requirements.txt
```

Everything is prepared now.


3 - Testing the installation
-----------------------------


So as to create a service we have to enable some options in `/etc/tor/torrc` uncommenting the reference to the ControlPort to enable Stem manage the Tor Service and the CookieAuthentication method. Uncommenting the options should be enough:
```
## The port on which Tor will listen for local connections from Tor
## controller applications, as documented in control-spec.txt.
ControlPort 9051
## If you enable the controlport, be sure to enable one of these
## authentication methods, to prevent attackers from accessing it.
#HashedControlPassword 16:872860B76453A77D60CA2BB8C1A7042072093276A3D701AD684053EC4C
CookieAuthentication 1
```

We need to stop the tor service and run it again using:
```
tor
```

In the trace, we would see now:
```
...
Jun 15 12:49:12.718 [notice] Read configuration file "/etc/tor/torrc".
Jun 15 12:49:12.722 [notice] Opening Socks listener on 127.0.0.1:9050
Jun 15 12:49:12.722 [notice] Opening Control listener on 127.0.0.1:9051
Jun 15 12:49:12.000 [notice] Parsing GEOIP IPv4 file /usr/share/tor/geoip.
Jun 15 12:49:12.000 [notice] Parsing GEOIP IPv6 file /usr/share/tor/geoip6.
...
```

Now we can test if the default configuration works:
```
cd server
python hello-onion.py
```

Now, we can see some info in the trace:
```
* Connecting to tor
* Creating our hidden service in /home/<user>/.tor/hello-onion
* Our service is available at ao7ntlxy4exd5k7f.onion, press ctrl+c to quit
Bottle v0.12.9 server starting up (using WSGIRefServer())...
Listening on http://localhost:5000/
Hit Ctrl-C to quit.
```

Thus, we can access the service by going to localhost:5000 to try it locally or to the recently created hidden service in the Tor Browser Bundle.
