from flask import Flask, jsonify, render_template
import socket

app = Flask(__name__)

def fetchHostDetails():
    host_name = socket.gethostname()
    host_ip = "unknown"
    try:
        host_ip = socket.gethostbyname(host_name)
    finally:
        return str(host_name), str(host_ip)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# emits the liveliness of the app to k8s
@app.route("/health")
def health():
    return jsonify(
        status="UP"
    )

# dynamic web pages using Jinja templates
@app.route("/details")
def details():
    hostname, ip = fetchHostDetails()
    return render_template('index.html', HOSTNAME=hostname, IP=ip)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
