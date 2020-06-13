from flask import Flask
import time

app = Flask(__name__)

@app.route('/time')
def index():
    # return("test")
    return {'time': time.time()}

if __name__ == "__main__":
    index()