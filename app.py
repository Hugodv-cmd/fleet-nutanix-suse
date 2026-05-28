import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    hypervisor = os.getenv('HYPERVISOR', 'Unknown Hypervisor')
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello World GitOps</title>
        <style>
            body {{
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
                background-color: #f4f6f9;
            }}
            .card {{
                text-align: center;
                padding: 40px;
                background: white;
                border-radius: 12px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }}
            h1 {{
                font-size: 3rem;
                color: #2c3e50;
                margin-bottom: 10px;
            }}
            p {{
                font-size: 1.5rem;
                color: #7f8c8d;
                margin: 0;
            }}
            .highlight {{
                color: #326ce5; /* Kubernetes Blue */
                font-weight: bold;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Hello World!</h1>
            <p>This application is being served from: <span class="highlight">{hypervisor}</span></p>
        </div>
    </body>
    </html>
    """
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
