from flask import Flask, request, render_template, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    with open('template.html', 'r') as file:
        template = file.read()

    return render_template_string(template.format(request.args.get('data', '')))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
