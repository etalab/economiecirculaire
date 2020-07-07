import os
import requests

from flask import Flask, render_template, jsonify, request
from flask_caching import Cache
from flask_cors import CORS

app = Flask(__name__,
            static_folder="../dist/assets",
            template_folder="../dist")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
cache = Cache(app, config={"CACHE_TYPE": "filesystem", "CACHE_DIR": "/tmp"})

AIRTABLES_URL = "https://api.airtable.com/v0/appXjbMenFXlzxNLp"
API_KEY = os.getenv("AIRTABLES_API_KEY")
HEADERS = {"Authorization": f"Bearer {API_KEY}"}
CACHE_TIMEOUT = 0 if app.config['DEBUG'] else os.getenv('CACHE_TIMEOUT', 600)


@app.route("/api/inventaire")
@cache.cached(timeout=CACHE_TIMEOUT)
def inventaire():
    url = f"{AIRTABLES_URL}/Inventaire%20public?view=viwlHW6pyW1NOkF42"
    r = requests.get(url, headers=HEADERS)
    return jsonify(r.json())


@app.route("/api/demande", methods=["POST"])
def demande():
    fields = [
        "Quelles données recherchez-vous ?",
        "S’il est connu, quel est le titre du jeu de données recherché ?"
    ]
    url = f"{AIRTABLES_URL}/Demandes%20d'ouverture"
    fields_dict = {field: request.json["fields"].get(field) for field in fields}
    r = requests.post(url, json={
        "fields": fields_dict
    }, headers=HEADERS)
    r.raise_for_status()
    return "", 201


@app.route("/", defaults={"path": ""})
# allows routing in vuejs
@app.route("/<path:path>")
def index(path):
    return render_template("index.html")
