import urllib.request, uuid
from flask import Flask, render_template, request, Response, redirect, flash

app = Flask(
    __name__,
    template_folder='src/templates',
    static_folder='src/static',
    static_url_path=''
)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    url = request.form.get('url', 'https://www.google.com')
    content = urllib.request.urlopen(url).read().decode().replace('\0', '\n')
    return render_template('index.html', error='Here\'s the content you requested\n' + content)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
