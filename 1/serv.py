from http.server import HTTPServer, CGIHTTPRequestHandler
from flask import Flask, render_template
name = input('enter name:')
app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    param = {}
    param['title'] = name
    return render_template('base.html', **param)
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
