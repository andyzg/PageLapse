from flask import Flask, render_template, request, jsonify, Response
from flask.ext.scss import Scss

app = Flask(__name__, static_folder='static', template_folder='assets/views')
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

Scss(app, static_dir='static', asset_dir='assets')

@app.route('/')
def get_root():
    return render_template('index.jade')

@app.route('/query')
def get_gif():
    url = request.args.get('url')
    history = [1, 2, 3, 4, 5];
    return jsonify(url=url, commitHistory=history)
    # return Response(status=300)

if __name__ == '__main__':
    app.run(debug=True)
