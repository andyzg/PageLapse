set -e

kill $(ps aux | grep 'jekyll serve' | awk '{print $2}') || true
kill $(ps aux | grep 'phantomjs' | awk '{print $2}') || true
rm -rf backend/tmp/*
rm -rf backend/tmp_host/*
rm -rf static/assets/screenshots/*
grunt lib
grunt js
grunt sass
grunt watch &
python app.py
