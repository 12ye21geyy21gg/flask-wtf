from http.server import HTTPServer, CGIHTTPRequestHandler
from flask import Flask, render_template,url_for

app = Flask(__name__)


@app.route('/training/<prof>')
def training(prof):
    param = {}
    param['number'] = prof
    if prof != 'врач':
        param['url'] = url_for('static',filename='pen.jpg')
    else:
        param['url'] = url_for('static',filename='kolba.jpg')
    return render_template('base.html', **param)
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')




