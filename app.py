from flask import Flask, render_template, redirect, url_for
from admin.admin import admin

app = Flask(__name__)

app.register_blueprint(admin, url_prefix='/admin')


@app.route('/')
def index():
    context = {
        'message': 'home page content',
        'page_title': 'Home'
    }
    return render_template('index.html', context=context)


@app.route('/news')
@app.route('/news/<string:tail>')
def news(tail=None):
    context = {
        'message': 'news page content',
        'page_title': 'News'
    }
    return render_template('news.html', context=context)


@app.route('/management')
@app.route('/management/<string:tail>')
def management(tail=None):
    context = {
        'message': 'management page content',
        'page_title': 'Management'
    }
    return render_template('management.html', context=context)


@app.route('/about')
@app.route('/about/<string:tail>')
def about(tail=None):
    context = {
        'message': 'about page content',
        'page_title': 'About'
    }
    return render_template('about.html', context=context)


@app.route('/contacts')
@app.route('/contacts/<string:tail>')
def contacts(tail=None):
    context = {
        'message': f'contacts page content',
        'page_title': 'Contacts'
    }
    return render_template('contacts.html', context=context)


@app.route('/history')
def history():
    context = {
        'message': 'history page content',
        'page_title': 'History'
    }
    return render_template('history.html', context=context)


@app.route('/history/people')
def history_people():
    context = {
        'message': 'history people page content',
        'page_title': 'People in History'
    }
    return render_template('history_people.html', context=context)


@app.route('/history/photos')
def history_photos():
    context = {
        'message': 'history photos page content',
        'page_title': 'History Photos'
    }
    return render_template('history_photos.html', context=context)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True, port=8000)
