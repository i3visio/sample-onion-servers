# !/usr/bin/python
# -*- coding: UTF-8 -*-
#
##################################################################################
#
#    Copyright 2016-2017 Félix Brezo and Yaiza Rubio (i3visio, contacto@i3visio.com)
#
#    This program is free software. You can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##################################################################################


__NAME__ = "hello-onion"
__DESCRIPTION__ = "Sample .onion service."
__VERSION__ = "1.0"

# DEFAULT OPTIONS
DEFAULT_HOST = "localhost"
DEFAULT_PORT = "5000"
DEFAULT_DATA_DIR = "/tmp"

# Bottle imports
# --------------
from bottle import route, run, template
# To enable response content
from bottle import response
# To enable request processing...
from bottle import request
from bottle import redirect


@route('/')
def index():
    return ''' 
        <h1>Hi guys!</h1>
        Another sample onion service built in Python with Bottle and Stem.
        Just a couple of things to be seen here:
        <ul>
            <li><a href="/javascript">/javascript</a>: To see if you have Javascript active in your current browser.</li>
            <li><a href="/hola/hacker">/hola/paco</a>: To say hello as Paco. That's all!</li>
        </ul>
    '''


@route('/javascript')
def sayHello():
    return ''' 
        This website has a Javascript embedded.
        <script>alert("I'm just some arbitrary Javascript running on your browser. Is Tor browser enough?");</script>
    '''


@route('/hola/<name>')
def sayHelloToName(name):
    print "[*] From the backend, we log that we are going to say hello to " + name
    return template(
    'Hi <b>{{name}}</b>!', name=name)


# Main execution of the server... It will generally won't need to be modified...
if __name__ == "__main__":
    # Importing the service_manager that launches the application...
    import service_manager

    # Grabbing the parser
    args = service_manager.getParser(__NAME__, __DESCRIPTION__, DEFAULT_HOST, DEFAULT_PORT, DEFAULT_PORT, __VERSION__)

    # Calling the main function... We set the tor variable as True so as to make it available in the Tor Network....
    service_manager.main(name = __NAME__, host = args.host, port = args.port, data_dir = args.data_dir, debug = args.debug, clean = args.clean, tor=True)
