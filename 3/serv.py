from http.server import HTTPServer, CGIHTTPRequestHandler
from flask import Flask, render_template,url_for

app = Flask(__name__)


@app.route('/list_prof/<typ>')
def list_prof(typ):
    param = {}
    param['typ'] = typ
    param['profs'] = list('инженер-исследователь, пилот, строитель, экзобиолог, врач, инженер по терраформированию, климатолог, специалист по радиационной защите, астрогеолог, гляциолог, инженер жизнеобеспечения, метеоролог, оператор марсохода, киберинженер, штурман, пилот дронов'.split(', '))
    return render_template('base.html', **param)
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')




