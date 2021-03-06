﻿from flask import Flask, request, render_template, redirect, url_for
import json
import time

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    p = draw_nbc(app.config.root_path)
    return render_template('index.html', p=p['param'], uid='', action='nbc/upload')


@app.route('/nbc/<float:timing>', methods=['GET'])
def show_nbc(timing):
    p = draw_nbc(app.config.root_path, timing)
    return render_template('index.html', p=p['param'], uid=str(timing), action='upload')


@app.route('/nbc/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['settings_json']
        if f:
            timing = str(time.time())
            f.save(app.config.root_path + '/static/results/settings'+timing+'.json')
            return redirect(url_for('show_nbc', timing=timing))
        else:
            return redirect(url_for('index'))
    else:
        return render_template('load.html')


def draw_nbc(path='', timing=''):
    import script
    settings = script.load_settings(path, timing)
    script.zodiaks_angle = settings['zodiaks_angle'] # angle change fo degree
    script.zodiac_signs = settings['zodiac']
    script.hosts_of_heaven = settings['hosts_of_heaven']
    def key_sort_hosts(key):
        return int(script.hosts_of_heaven[key]['order'])
    script.hosts = sorted(list(script.hosts_of_heaven),key=script.key_sort_hosts)
    script.aspects = settings['aspects']
    script.houses = settings['houses']
    return script.draw_birth_chart(app.config.root_path, timing, settings['png'])


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
