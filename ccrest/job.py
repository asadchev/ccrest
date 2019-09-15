import tempfile
import subprocess
import flask

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField

class Job:
  def __init__(self, *args, stdin=None):
    self._args = list(*args)
    self._stdin = stdin
  def run(self):
    print (self._args)
    p = subprocess.Popen(
      self._args,
      stdin=self._stdin,
      stdout=subprocess.PIPE,
      stderr=subprocess.STDOUT
    )
    return p

  @staticmethod
  def TemporaryFile(data):
    f = tempfile.TemporaryFile(mode="w")
    f.write(data)
    f.flush()
    f.seek(0)
    return f

class JobForm(FlaskForm):
    basis = StringField('Basis', render_kw={"size": 10})
    method = StringField('Method', render_kw={"size": 10})
    molecule = TextAreaField('Molecule', render_kw={"rows": 10, "cols": 20})
    submit = SubmitField('Run')

    @staticmethod
    def to_dict(form):
      data = form.to_dict()
      print (type(data['molecule']), data['molecule'])
      molecule = [ JobForm.parse_atom(line) for line in data['molecule'].splitlines() if line ]
      data['molecule'] = molecule
      return data

    @staticmethod
    def parse_atom(line):
      (s,x,y,z) = line.split()
      return (s, float(x), float(y), float(z))
