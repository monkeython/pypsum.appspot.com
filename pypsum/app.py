"""
pypsum.appspot.com
~~~~~~~~~~~~~~~~~~

This is the pypsum Google Appengine application runner. It does nothing more
than importing the pypsum application, Goolge Appengine SDK utils and run the
application.
"""

__author__ = "Luca De Vitis <luca@monkeython.com>"
__version__ = '0.2'
__copyright__ = "2011, %s " % __author__
__license__ = """
   Copyright (C) %s

      This program is free software: you can redistribute it and/or modify
      it under the terms of the GNU General Public License as published by
      the Free Software Foundation, either version 3 of the License, or
      (at your option) any later version.

      This program is distributed in the hope that it will be useful,
      but WITHOUT ANY WARRANTY; without even the implied warranty of
      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
      GNU General Public License for more details.

      You should have received a copy of the GNU General Public License
      .along with this program.  If not, see <http://www.gnu.org/licenses/>.
""" % __copyright__
__doc__ = """
:version: %s
:author: %s
:organization: Monkeython
:contact: http://www.monkeython.com
:copyright: %s

%s
""" % (__version__, __author__, __license__, __doc__)
__docformat__ = 'restructuredtext en'
__classifiers__ = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Operating System :: OS Independent',
    'Topic :: Internet :: WWW/HTTP' ]

if __name__ == '__main__':
    from google.appengine.ext.webapp.util import run_wsgi_app
    from pypsum.application import pypsum
    from pypsum.settings import AppSpot
    pypsum.config.from_object(AppSpot)
    run_wsgi_app(pypsum)
