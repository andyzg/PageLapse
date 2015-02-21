set -e

grunt lib
grunt watch &
python app.py
