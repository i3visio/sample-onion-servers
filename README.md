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

5 - AUTHORS
-----------

More details about the authors in the [AUTHORS.md](AUTHORS.md) file.
