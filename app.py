from flask import Flask
from subprocess import Popen, PIPE

app = Flask(__name__)


@app.route('/status')
def status():
    with Popen(["hostname"], stdout=PIPE) as proc:
        return proc.stdout.read()
