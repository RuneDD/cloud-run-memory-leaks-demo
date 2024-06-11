import os
import time
from flask import Flask
from jinja2.utils import Markup, escape

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/write')
def write_files():
    large_content = "This is a very large file.\n" * 10000
    counter = 0
    while counter < 1000:
        filename = f"/tmp/file_{counter}.txt"
        with open(filename, "w") as file:
            file.write(large_content)
        counter += 1
        time.sleep(0.5)
    return 'Finished writing files'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
