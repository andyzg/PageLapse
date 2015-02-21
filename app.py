from flask import Flask, render_template
from flask.ext.scss import Scss

app = Flask(__name__, static_folder='static', template_folder='assets/views')
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

Scss(app, static_dir='static', asset_dir='assets')

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/jade')
def test_jade():
    return render_template('test.jade')

if __name__ == '__main__':
    app.run(debug=True)
