set -e

kill $(ps aux | grep 'jekyll serve' | awk '{print $2}')
kill $(ps aux | grep ‘phantomjs' | awk '{print $2}')
grunt lib
grunt js
grunt sass
grunt watch &
python app.py
