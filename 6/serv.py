from http.server import HTTPServer, CGIHTTPRequestHandler
from flask import Flask, render_template,url_for

app = Flask(__name__)

@app.route('/distribution')
def d():
    return 'список имен вводить так "/distribution/name1,name2,name3"'

@app.route('/distribution/<k>')
def list_prof(k):
    param = {}
    param['k'] = list(k.split(','))
    return render_template('base.html', **param)
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')




