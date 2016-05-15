#!/usr/bin/python
#
# Flask server, woo!
#

from flask import Flask, request, redirect, url_for, send_from_directory

# Setup Flask app.
app = Flask(__name__, static_url_path='')
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




# THE OTHER PYTHON APPS (DONE WITH BLUEPRINT)

from deceptron.deceptron import deceptron
app.register_blueprint(deceptron)
app.register_blueprint(deceptron, url_prefix='/pages')

from lotusApp.lotus import lotus
app.register_blueprint(lotus)
app.register_blueprint(lotus, url_prefix='/lotusApp/assets')



# RUN EVERYTHING!!!
if __name__ == '__main__':
  app.run()