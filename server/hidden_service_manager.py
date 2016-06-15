# !/usr/bin/python
# -*- coding: UTF-8 -*-
#
##################################################################################
#
#    Copyright 2016 Félix Brezo and Yaiza Rubio (i3visio, contacto@i3visio.com)
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

import os
import shutil

# Bottle imports
# --------------
from bottle import run

# Stem controller imports
# -----------------------
from stem.control import Controller


"""
    Main function that launches the onion service
"""
def main(host = "localhost", port = 5000, data_dir = "/tmp", debug = True, clean = False, name = "a_hidden_service"):
    print(' * Connecting to tor...')

    with Controller.from_port(port=9051) as controller:
        controller.authenticate()

        # All hidden services have a directory on disk. Lets put ours in tor's data
        # directory.

        hidden_service_dir = os.path.join(controller.get_conf('DataDirectory', data_dir), name)

        # Create a hidden service where visitors of port 80 get redirected to local
        # port where Bottle will be listening.

        print(" * Creating our hidden service in %s..." % hidden_service_dir)
        try:
            result = controller.create_hidden_service(hidden_service_dir, 80, target_port = port)
            # The hostname is only available when we can read the hidden service
            # directory. This requires us to be running with the same user as tor.

            if result.hostname:
                print(" * Our service is available at %s. Press Ctrl+c to quit." % result.hostname)
            else:
                print(" * Unable to determine our service's hostname, probably due to being unable to read the hidden service directory.")

        except Exception as e:
            print(" * Something happened... Does it exist?")
            print(" * Trace:\n" + str(e))

        try:
            run(host=host, port=port, debug=debug)
        finally:
            # Shut down the hidden service and clean it off disk. Note that you *don't*
            # want to delete the hidden service directory if you'd like to have this
            # same *.onion address in the future.

            print(" * Shutting down our hidden service...")
            controller.remove_hidden_service(hidden_service_dir)
            if clean:
                print(" * Cleaning the hidden service directory...")
                shutil.rmtree(hidden_service_dir)
