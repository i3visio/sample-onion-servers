Sample Onion Services
====================

Copyright (C) 2016-2017  F. Brezo and Y. Rubio, i3visio

1 - Description
---------------

This project includes a couple of onion services deployed with Bottle and Tor's stem.
By doing so, we want to provide an easy-to-use approach that makes to understand the
behaviour of certain Tor Gateways.

2 - License: AGPLv3+
-------------------

This is free software, and you are welcome to redistribute it under certain conditions.

	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU Affero General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU Affero General Public License for more details.

	You should have received a copy of the GNU Affero General Public License
	along with this program. If not, see <http://www.gnu.org/licenses/>.


For more details on this issue, check the [COPYING](COPYING) file.

3 - Installation
----------------

You will also need to have Tor up and running with several special specifications
Open the `/et/tor/torrc` file and search the `ControlPort 9051` line and uncomment
it. You will also need to uncomment the `CookieAuthentication 1` line to let `stem`
control the instance from Python code. Full details can be found in the 
[INSTALL.md](INSTALL.MD) file. Afterwards, restart tor service:
```
service tor restart
```

If everything went Ok, you can download the project knowing that you need a 
Python 2 installation (tested with 2.7) and pip. Check it using:
```
python --version
pip --version
```

You can now clone the project using `git` for example.
```
git clone https://github.com/i3visio/sample-onion-servers
```

Afterwards, fix the dependencies:
```
cd sample-onion-servers
pip install -r requirements.txt
```

You should be ready to go now.

4 - Basic usage
---------------

You should explore the `server` folder. There you will be able to find a couple 
of servers that may help you:
* `hello-onion.py`. Just a hello world as an example.
* `headers-onion.py`. It shows the headers sent by the user who performed the
request as seen by the server. Useful to test the queries sent by third parties
gateways without messing up too much.

Check your Tor configuration as defined in [INSTALL.md](INSTALL.md) If when 
launching the scripts with python, you are refused an error similar to this 
one:
```
 * Connecting to tor...
Traceback (most recent call last):
  File "headers-onion.py", line 104, in <module>
    service_manager.main(name = __NAME__, host = args.host, port = args.port, data_dir = args.data_dir, debug = args.debug, clean = args.clean, tor=True)
  File "/root/Documents/sample-onion-servers/server/service_manager.py", line 43, in main
    with Controller.from_port(port=9051) as controller:
  File "/usr/local/lib/python2.7/dist-packages/stem/control.py", line 998, in from_port
    control_port = stem.socket.ControlPort(address, port)
  File "/usr/local/lib/python2.7/dist-packages/stem/socket.py", line 372, in __init__
    self.connect()
  File "/usr/local/lib/python2.7/dist-packages/stem/socket.py", line 243, in connect
    self._socket = self._make_socket()
  File "/usr/local/lib/python2.7/dist-packages/stem/socket.py", line 401, in _make_socket
    raise stem.SocketError(exc)
stem.SocketError: [Errno 111] Connection refused
```

This is typically shown either when Tor is not up and running or when the 
ControlPort and authentication method have not been defined.

5 - Hacking
-----------

Check the details at the [HACKING.md](HACKING.md) file to read the guidelines
about how to contribute to this project.

6 - Authors
-----------

More details about the authors in the [AUTHORS.md](AUTHORS.md) file.
