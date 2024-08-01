from flask import Flask, render_template # type: ignore

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/order')
def order():
    return render_template('order.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)