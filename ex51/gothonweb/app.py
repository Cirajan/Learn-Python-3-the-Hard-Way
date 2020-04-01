from flask import Flask
from flask import render_template
from flask import request
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))




app = Flask(__name__)

@app.route('/hello', methods=['POST', 'GET'])
def index():
    greeting = 'Hello World'

    if request.method == 'POST':
        name = request.form['name']
        greet = request.form['greet']
        greeting = f'{greet}, {name}'
        return render_template('index_laid_out.html', greeting=greeting)
    else:
        return render_template('hello_form_laid_out.html')


@app.route('/upload_pic', methods=['POST'])
def upload_pic():
    photo_object = request.files['pic']
    target = os.path.join(APP_ROOT, 'images/')
    filename = photo_object.filename
    destination = '/'.join([target, filename])

    photo_object.save(destination)



    return render_template('pic_saved.html')



if __name__ == '__main__':
    app.run(debug=True)
