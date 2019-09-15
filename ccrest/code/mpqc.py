import ccrest.job

def make_input(params):
  method = params["method"]
  basis = params["basis"]
  molecule = "\n".join([ "%s %f %f %f" % tuple(atom) for atom in params["molecule"]])
  return """
  checkpoint: no
  optimize: yes
  method: {method}
  basis: {basis}
  molecule: (angstrom)
  {molecule}
""".format(**locals())

def job(config, params):
  from ccrest.job import Job
  print (make_input(params))
  return Job(
    ["mpqc", "-W", "/tmp", "/dev/stdin" ],
    stdin=Job.TemporaryFile(make_input(params))
  )
