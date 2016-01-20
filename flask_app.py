from flask import Flask, request, render_template, redirect, url_for
import json, script

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    p = script.draw_img(app.config.root_path)

    return render_template('index.html', p=p['param'])


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        #request.form.getlist('checkbox1')
        f = request.files['settings_json']
        f.save(app.config.root_path + '/static/results/settings.json')
        return redirect(url_for('index'))
    else:
        return render_template('load.html')
    #return redirect(url_for('index'))


@app.route('/img_map', methods=['GET', 'POST'])
def img_map():

    script.draw_img(app.config.root_path)

    return json.dumps(read_file_json())


def read_file_json():
    f = open(app.config.root_path + '/static/results/test.json', 'r+')
    t = f.read()
    if t == '':
        return t
    g = json.loads(t)
    s = ''
    f.write(s)
    f.close()

    for key in g['param']:
        s = s + '<div style="top:' + str(g['param'][key]['top']) + '%; left:' + str(
                g['param'][key]['left']) + '%; width:' + str(g['param'][key]['size']) + '%;height:' + str(
                g['param'][key]['size']) + '%"'
        s = s + ' id="' + key + '" class="mapObject" title="' + g['param'][key]['title'] + '" data-text="' + \
            g['param'][key]['description'] + '"></div>'

    return s


if __name__ == '__main__':
   app.run()
