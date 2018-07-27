# pokestop-taiwan
query igress Portal site info API

```
get http://127.0.0.1:8000/get_bbox_sites/<lat>/<lng>

[
  {
  poke_image: <image_url>,
  poke_lat: <lat>,
  poke_lng: <lng>,
  poke_title: <name>
  },
  ...
]
```

```
get http://127.0.0.1:8000/get_sites/<Portal site name>/

[
  {
  poke_title: <image_url>,
  poke_lat: <lat>,
  poke_lng: <lng>
  },
  ...
]
```
