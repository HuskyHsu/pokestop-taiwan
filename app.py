from flask import Flask, jsonify, Response
import requests

app = Flask(__name__)

@app.route("/get_bbox_sites/<lat>/<lng>")
def get_bbox_sites(lat, lng):

    lat = float(lat)
    lng = float(lng)

    headers = {
        "X-Requested-With":"XMLHttpRequest",
        "Referer":"https://www.pokemongomap.info",
        "Cookie": '__cfduid=dc1fdf477a64225cd6b8005548b5176ec1527300954; _ga=GA1.2.527083445.1527300954; disqus_unique=6olkqof3rt88l0; PHPSESSID=4p8kdvr2gdnq6c1vh6gd0ldde0; announcementnews17=1; mapfilters=1[##split##]1[##split##]1[##split##]0[##split##]0[##split##]1[##split##]0[##split##]0[##split##]1[##split##]1[##split##]1[##split##]0[##split##]1[##split##]1[##split##]1[##split##]1[##split##]1[##split##]0[##split##]1[##split##]6[##split##]0[##split##]2[##split##]1[##split##]0[##split##]0[##split##]0[##split##]0[##split##]1[##split##]; _gid=GA1.2.1164560502.1528201848; alertmsg4=1; __atuvc=15%7C21%2C5%7C22%2C11%7C23; __atuvs=5b16827738947956001; __atssc=facebook%3B1; __jid=7jgtgk93sqie3j; latlngzoom=17[##split##]25.059815932803865[##split##]121.52229168913263'
    }

    payload = {
        "fromlat": lat - 0.001,
        "fromlng": lng - 0.001,
        "tolat": lat + 0.001,
        "tolng": lng + 0.001
    }

    return jsonify(payload)

    r = requests.post("https://www.pokemongomap.info/includes/it77nmsq9.php", data=payload, headers=headers)

    print(r.text)
    return jsonify(r.text)

@app.route("/get_PokeStops/<name>/<lat>/<lng>")
def get_PokeStops(name, lat, lng):

    headers = {
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://www.pokemongomap.info",
        "Cookie": "__cfduid=dc1fdf477a64225cd6b8005548b5176ec1527300954; _ga=GA1.2.527083445.1527300954; disqus_unique=6olkqof3rt88l0; PHPSESSID=4p8kdvr2gdnq6c1vh6gd0ldde0; announcementnews17=1; mapfilters=1[##split##]1[##split##]1[##split##]0[##split##]0[##split##]1[##split##]0[##split##]0[##split##]1[##split##]1[##split##]1[##split##]0[##split##]1[##split##]1[##split##]1[##split##]1[##split##]1[##split##]0[##split##]1[##split##]6[##split##]0[##split##]2[##split##]1[##split##]0[##split##]0[##split##]0[##split##]0[##split##]1[##split##]; _gid=GA1.2.1164560502.1528201848; alertmsg4=1; __atuvc=15%7C21%2C5%7C22%2C11%7C23; __atuvs=5b16827738947956001; __atssc=facebook%3B1; __jid=7jgtgk93sqie3j; latlngzoom=17[##split##]25.059815932803865[##split##]121.52229168913263; __cfduid=dc1fdf477a64225cd6b8005548b5176ec1527300954; _ga=GA1.2.527083445.1527300954; disqus_unique=6olkqof3rt88l0; PHPSESSID=4p8kdvr2gdnq6c1vh6gd0ldde0; announcementnews17=1; mapfilters=1[##split##]1[##split##]1[##split##]0[##split##]0[##split##]1[##split##]0[##split##]0[##split##]1[##split##]1[##split##]1[##split##]0[##split##]1[##split##]1[##split##]1[##split##]1[##split##]1[##split##]0[##split##]1[##split##]6[##split##]0[##split##]2[##split##]1[##split##]0[##split##]0[##split##]0[##split##]0[##split##]1[##split##]; _gid=GA1.2.1164560502.1528201848; alertmsg4=1; __atuvc=15%7C21%2C5%7C22%2C11%7C23; __atuvs=5b16827738947956001; __atssc=facebook%3B1; __jid=7jgtgk93sqie3j; latlngzoom=17[##split##]25.059815932803865[##split##]121.52229168913263"
    }

    payload = {
        "mode": 1,
        "searchloc": name,
        'tlat': lat,
        'tlng': lng
    }

    r = requests.post("https://www.pokemongomap.info/includes/locsearch.php", data=payload, headers=headers)

    return jsonify(r.text)

if __name__ == '__main__':
    app.run(debug=True)