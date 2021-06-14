from flask import Flask, render_template
import time

# Create a flask app
app = Flask(__name__, template_folder='templates', static_folder='static')


# Index page (now using the index.html file)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', debug=True, port=8080)
