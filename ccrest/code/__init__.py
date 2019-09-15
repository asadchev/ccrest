import importlib
import flask

def load(code):
  return importlib.import_module(".%s" % code, "ccrest.code")

def run(code, config, data):
  job = load(code).job(config, data)
  print (job)
  p = job.run()
  return flask.Response(p.stdout, mimetype='text/plain')
