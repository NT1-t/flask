import json
import datetime
from flask import Flask

app = Flask(__name__)

@app.route("/save")
def save():
    f = open('data.json', 'r+', encoding='utf-8')
    json_file = json.load(f)
    ln = len(json_file)
    now = str(datetime.datetime.now())
    dt = {
    "id":ln,
    "name":"noname",
    "description":"no description",
    "now":now
    }
    json_file.append(dt)
    json_data = json.dumps(json_file, indent=4, ensure_ascii=False)
    f = open('data.json', 'w', encoding='utf-8')
    f.write(json_data)
    f.close()
    return json_data
