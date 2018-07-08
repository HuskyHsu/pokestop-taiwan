from flask import Flask, jsonify, Response
from flask_cors import CORS, cross_origin
import requests
import sqlite3

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/get_bbox_sites/<lat>/<lng>")
@cross_origin()
def get_bbox_sites(lat, lng):

    lat = float(lat)
    lng = float(lng)

    conn = sqlite3.connect('pokestop.db')
    c = conn.cursor()

    data = [{"poke_title": row[1], "poke_lat": float(row[2]), "poke_lng": float(row[3]), "poke_image": row[4]} for row in c.execute("select * from pokestop where lat between ? and ? and lng between ? and ?", (lat - 0.001, lat + 0.001, lng - 0.001, lng + 0.001))]

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)