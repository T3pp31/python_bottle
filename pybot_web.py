from bottle import route, run, template, request
from pybot import bot

@route('/')
def hello():
    return template('pybot_template', input_text='', output_text='')


@route('/', method='POST')
def do_hello():
    input_text = request.forms.input_text
    output_text = bot(input_text)
    return template('pybot_template', input_text=input_text, output_text=output_text)


run(host='localhost', debug=True)






