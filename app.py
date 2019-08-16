# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request
from aiutil import airoot

app = Flask(__name__)
conv_list = []

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template('index.html', name=name)

@app.route('/chatbot', methods=['GET','POST'])
def chatbot_views():
    if request.method == 'POST':
        word = request.form.get('word')
        res = airoot().getword(word)
        conv_list.append((word, res))
        return render_template('index.html', name='chatbot', res=conv_list)
    else:
        return render_template('index.html', name='chatbot', res='')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)