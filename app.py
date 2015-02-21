from flask import Flask, render_template
app = Flask(__name__)

app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/jade')
def test_jade():
    return render_template('test.jade')

if __name__ == '__main__':
    app.run(debug=True)
