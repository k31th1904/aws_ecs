from flask import Flask, request, render_template
import socket

app = Flask(__name__)
title = socket.gethostname()

@app.route('/', methods=['GET'])
def index():

    if request.method == 'GET':      
        # Return index with hostname values
        return render_template("index.html", title=title)

if __name__ == "__main__":
    app.run()
