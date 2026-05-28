import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Fleet will dynamically inject this environment variable
    hypervisor = os.getenv('HYPERVISOR', 'Unknown Hypervisor')
    return f"Hello World! This application is being served from: {hypervisor}\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
