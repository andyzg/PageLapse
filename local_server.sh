set -e

grunt lib
grunt js
grunt sass
grunt watch &
python app.py
