from encodings import utf_8
import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#Indenting JSON file.
filename = 'eq_week_sep_18.json'
with open(filename, encoding='utf-8') as f:
    all_eq_data = json.load(f)

readable_file = 'readable_eq_week_sep_18.json'
with open(readable_file, 'w') as rf:
    json.dump(all_eq_data, rf, indent=4) 

#Processing earthquake data.
all_eq_dicts = all_eq_data['features']                

mags, lons, lats, hover_texts = [], [], [], []

for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

#Mapping the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]
my_layout = Layout(title=f"{all_eq_data['metadata']['title']}")

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')