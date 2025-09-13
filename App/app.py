from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    """Return a friendly HTTP greeting."""
    return 'Hello from your DevOps pipeline!'


if __name__ == '__main__':
    # Listen on all interfaces so the container is reachable
    app.run(host='0.0.0.0', port=80)
