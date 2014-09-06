from flask import Flask
from flask import render_template
from google.appengine.api import urlfetch
import json
app = Flask(__name__)
app.debug = True

api_url = "http://www.aethyrnet.com/api/lcs"

@app.route('/')
def show_chart():
    # Load the api data
    result = urlfetch.fetch(api_url)
    if result.status_code != 200:
        return "Error getting data from api", 500
    
    player_infos = json.loads(result.content)
    return render_template('show_chart.html', player_infos=player_infos)
