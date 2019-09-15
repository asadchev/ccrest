#!/usr/bin/env python3

try:
  import flask
except:
  raise Exception("need to install flask")

import os

app = flask.Flask("ccrest")
app.config['SECRET_KEY'] = 'secret'

from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)

config = dict()
import ccrest.code
import ccrest.job

@app.route('/code/<name>', methods=['POST', 'GET'])
def code(name):
  request = flask.request
  if request.method == 'GET':
    return flask.render_template('code.html', form=ccrest.job.JobForm())
  print (request)
  data = None
  if not request.json:
    data = ccrest.job.JobForm.to_dict(request.form)
  else:
    data = request.json
  assert data
  print ('/code/%s: %r' % (name, data))
  results = ccrest.code.run(name, config.get(name, None), data)
  return results


def run(host=None, port=None):
  app.run(host, port)
