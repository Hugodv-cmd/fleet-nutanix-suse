import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Fleet will dynamically inject this environment variable
    cluster_name = os.getenv('CLUSTER_NAME', 'Unknown Kubernetes Cluster')
    return f"Hello World! This application is being served from: {cluster_name}\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
