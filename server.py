#!/usr/bin/python
#
# Flask server, woo!
#

from flask import Flask, request, redirect, url_for, send_from_directory


# THIS IS THE ONLY PY CODE FOR THE HOME------

# Setup Flask app.
app = Flask(__name__, static_url_path='')
# app = Flask(__name__, static_url_path='') # if assets in in static root, no quotes like this
app.debug = True

# THE ANGULAR APP (GOES TO STATIC FOLDER)
# Routes
@app.route('/')
def root():
  return app.send_static_file('index.html')

@app.route('/<path:path>')
def static_proxy(path):
  # send_static_file will guess the correct MIME type
  return app.send_static_file(path)


# THE OTHER PYTHON APPS (DONE WITH BLUEPRINT)--------



from deceptronApp.deceptron import deceptron
app.register_blueprint(deceptron)
app.register_blueprint(deceptron, url_prefix='/pages')



from icApp.ic import ic
app.register_blueprint(ic)
app.register_blueprint(ic, url_prefix='/pages')


from testApp.test import test
app.register_blueprint(test)
app.register_blueprint(test, url_prefix='/pages')

from lotusApp.lotus import lotus
app.register_blueprint(lotus)
app.register_blueprint(lotus, url_prefix='/lotusApp/assets')



# RUN EVERYTHING!!!
if __name__ == '__main__':
  app.run()