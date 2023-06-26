from flask import Flask, render_template, request
import db

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        db.add_comment(request.form['comment'])

    query = request.args.get('q')
    return render_template('index.html', comments=db.get_comments(query), query=query)

@app.route('/admin')
def a():
    return 'you found me :)'

@app.route('/testing')
def b():
    return 'you found me :)'

@app.route('/dev')
def c():
    return 'you found me :)'

@app.route('/update')
def d():
    return 'you found me :)'

@app.route('/upload')
def e():
    return 'you found me :)'

@app.route('/files')
def f():
    return 'you found me :)'

@app.route('/login')
def g():
    return 'you found me :)'

@app.route('/logout')
def h():
    return 'you found me :)'

@app.route('/image')
def i():
    return 'you found me :)'

@app.route('/config')
def j():
    return 'you found me :)'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80)
