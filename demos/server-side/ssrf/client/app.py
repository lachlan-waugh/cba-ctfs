import requests, uuid
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

    image_id = uuid.uuid4()
    image = requests.get(request.form['url'])
    if ('html' in image.headers['content-type']):
        return render_template('index.html', error='ERROR: not a valid image!!\n' + image.content.decode())

    with open(f'client/src/static/img/{image_id}.png', 'wb+') as f:
        f.write(image.content)

    return render_template('index.html', file=image_id)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
