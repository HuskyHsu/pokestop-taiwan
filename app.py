from flask import Flask, jsonify, Response
from flask_cors import CORS, cross_origin
import requests, sqlite3

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def hello():
    with open('inngress_20181210.csv', 'rt', encoding="UTF-8") as fin:
        data = fin.readlines()
    
    conn = sqlite3.connect('pokestop_.db')

    print("Opened database successfully");
    c = conn.cursor()
    c.execute('''
        CREATE TABLE `pokestop` (
            `id`	TEXT,
            `name`	TEXT,
            `lat`	TEXT,
            `lng`	TEXT,
            `image_url`	TEXT
        );
    ''')
    print("Table created successfully");

    conn.commit()

    outdata = []
    for row in data:
        outdata.append(row.replace("\n", "").split('❦'))

    print(outdata[0])

    conn.executemany('INSERT INTO pokestop VALUES (?,?,?,?,?)', outdata[1:])

    conn.commit()
    conn.close()

    return "Hello World!"

@app.route("/get_bbox_sites/<lat>/<lng>")
@cross_origin()
def get_bbox_sites(lat, lng):

    lat = float(lat)
    lng = float(lng)

    conn = sqlite3.connect('pokestop.db')
    c = conn.cursor()

    data = [{"poke_id": row[0], "poke_title": row[1], "poke_lat": float(row[2]), "poke_lng": float(row[3]), "poke_image": row[4]} for row in c.execute("select * from pokestop where lat between ? and ? and lng between ? and ?", (lat - 0.001, lat + 0.001, lng - 0.001, lng + 0.001))]

    return jsonify(data)

@app.route("/get_sites/<site_name>/")
def get_sites(site_name):

    conn = sqlite3.connect('pokestop.db')
    c = conn.cursor()

    data = ['<tr><td>{}</td><td>{}</td><td>{}</td><td><img src="{}" height="200px"></td></tr>'.format(row[1], row[0], row[2] + ',' + row[3], row[4]) for row in c.execute("select * from pokestop where name = ?", (site_name,))]

    table_str = '''
    <table border="2">
        <tr>
            <th>名稱</th>
            <th>ingress ID</th>
            <th>座標</th> 
            <th>照片</th>
        </tr>
    {}
    </table>
    '''.format(''.join(data))

    return table_str

if __name__ == '__main__':
    app.run(debug=True)