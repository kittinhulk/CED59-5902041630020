from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('register.html')

@app.route('/' ,methods=["post"])
def register():
    return 'ok'

if __name__== '__main__':
    app.run()
