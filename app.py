from flask import Flask
app = Flask(__name__)

@app.get("/")
def hello():
    return "Hello from Week3 Lab3 v2!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
