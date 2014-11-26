__author__ = 'ventum11'

from flask import Flask,render_template

blog = Flask(__name__)

@blog.route('/')
def index():
    return render_template('index.html')

@blog.route('/about-us')
def about():
    return render_template('about.html')

@blog.route('/people')
def people():
    return render_template('people.html')

@blog.route('/dealers')
def dealer():
    return render_template('dealers.html')

@blog.route('/fashion')
def fashion():
    return render_template('fashion.html')

@blog.route('/contact-us')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
   blog.run(debug = True)