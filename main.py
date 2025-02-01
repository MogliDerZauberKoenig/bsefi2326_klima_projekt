from flask import Flask, Response, send_file
import random
import os

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return render_template("index.html")

# @app.route("/history")
# def page_history():
#     return render_template("history.html")

def get_file(filename):  # pragma: no cover
    try:
        src = os.path.join(root_dir(), filename)
        # Figure out how flask returns static files
        # Tried:
        # - render_template
        # - send_file
        # This should not be so non-obvious
        return open(src).read()
    except IOError as exc:
        return str(exc)
def root_dir():  # pragma: no cover
    return os.path.abspath(os.path.dirname(__file__))+'/static' 
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def get_resource(path):  # pragma: no cover
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