from flask import Flask, Response, send_file
import random
import os

app = Flask(__name__)

def get_file(filename):  
    try:
        src = os.path.join(root_dir(), filename)
        return open(src).read()
    except IOError as exc:
        return str(exc)
def root_dir():  
    return os.path.abspath(os.path.dirname(__file__))+'/static' 
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def get_resource(path):  
    if path  == '':
        path = 'index.html'
    mimetypes = {
        ".png": "image/png",
        ".css": "text/css",
        ".html": "text/html",
        ".js": "application/javascript",
    }
    complete_path = os.path.join(root_dir(), path)
    ext = os.path.splitext(path)[1]
    mimetype = mimetypes.get(ext, "text/html")
    if mimetype == "image/png":
        return send_file(complete_path, mimetype=mimetype)
    content = get_file(complete_path)
    return Response(content, mimetype=mimetype)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)