#!/usr/bin/scl enable rh-python35 -- /home/cone8536/.virtualenv/bin/python
 
import os, sys
 
from flup.server.fcgi import WSGIServer
from django.core.wsgi import get_wsgi_application
 
sys.path.insert(0, "/home/cone8536/public_html")
os.environ['DJANGO_SETTINGS_MODULE'] = "public_html.settings"
 
WSGIServer(get_wsgi_application()).run()
