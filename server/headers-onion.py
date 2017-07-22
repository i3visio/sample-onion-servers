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


__NAME__ = "headers-onion"
__DESCRIPTION__ = "Sample .onion service that returns the headers of a request."
__VERSION__ = "1.0"

# DEFAULT OPTIONS
DEFAULT_HOST = "localhost"
DEFAULT_PORT = "5001"
DEFAULT_DATA_DIR = "/tmp"

import os
import json

# Bottle imports
# --------------
from bottle import route, run, template
# To enable response content
from bottle import response
# To enable request processing...
from bottle import request
from bottle import redirect
# To handle API
from bottle import post, get, put, delete

def getFooter():
    return ''' 
        <br>
        <br>
        <small>This software is free software under <a href="https://www.gnu.org/licenses/agpl.txt">AGPLv3</a> license.</small>
    '''

@route('/')
def index():
    # get the Accept paramter from the HTTP Header
    print json.dumps(dict(request.headers),indent=2)
    return ''' 
        <h1>Welcome to this hidden service</h1>

        <b>Hi there!</b>
        <br>
        This is just a sample hidden service with not much to do. It just says you hello answering with the headers sent by you.
        <br>
        For example, try <a href="/hola/paco">/hola/paco</a>, <a href="/hola/james">/hola/james</a>, <a href="/hola/ronaldo">/hola/ronaldo</a>...
    ''' + getFooter()

@route('/hola/<name>')
def sayHelloToName(name):
    cabeceras = json.dumps(dict(request.headers),indent=2)
    print cabeceras
    return template(
    ''' <b>Hello {{name}}!</b>
        Your petition has effectively sent the following headers:<br>
        <pre>{{headers}}</pre>
        Were you really waiting for this information?
    ''' + getFooter(), name=name, headers=cabeceras)

# Defining error websites...:
from bottle import error

@error(404)
def error404(error):
    print error
    return template('What are you looking for? Nothing here! <br> <pre>{{error}}</pre>', error=str(error))

@error(500)
def error500(error):
    print error
    return template('Internal error (code 500).. <br> <pre>{{error}}</pre>', error=str(error))


"""
    Main execution of the server... It will generally won't need to be modified...
"""
if __name__ == "__main__":
    # Importing the service_manager that launches the application...
    import service_manager

    # Grabbing the parser
    args = service_manager.getParser(__NAME__, __DESCRIPTION__, DEFAULT_HOST, DEFAULT_PORT, DEFAULT_PORT, __VERSION__)

    # Calling the main function... We set the tor variable as True so as to make it available in the Tor Network....
    service_manager.main(name = __NAME__, host = args.host, port = args.port, data_dir = args.data_dir, debug = args.debug, clean = args.clean, tor=True)
