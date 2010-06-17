**RopeMate.tmbundle**
===========================

Integrates the Python refactoring/completion framework Rope with Textmate.
Screenshots and more info can be found at the project's [GitHub page](http://specialunderwear.github.com/RopeMate.tmbundle/).

Many thanks to Github user [specialunderwear](http://github.com/specialunderwear) for his contributions!

Copyright (C) 2010 Julian Eberius

CONFIGURATION
-------------

If you are using virtualenv, add the path to the virtualenv in .ropeproject/config.pythonpath:

    # You can extend python path for looking up modules
    prefs.add('python_path', '/Users/ebone/.virtualenvs/lukkien/lib/python2.6/site-packages/')

If you are doing django development, it might help to set the `DJANGO_SETTINGS_MODULE` in .ropeproject/config.project_opened:

    def project_opened(project):
        """This function is called after opening the project"""
        # Do whatever you like here!
        os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'


    License: 
    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

    Have a look at "LICENSE.txt" file for more information.

EXTERNAL LICENSES
-----------------
This project uses code from other open source projects (Rope) 
which may include licenses of their own.