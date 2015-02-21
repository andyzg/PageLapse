set -e

bundle exec sass --watch assets/scss:static/css &
python app.py
