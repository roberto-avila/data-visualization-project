import requests

from plotly.graph_objs import Bar
from plotly import offline

#Make API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
v3_headers = {'Accept': 'application/vnd.github.v3+json'}
response = requests.get(url, headers=v3_headers, verify=False)  
print(f"Status code: {response.status_code}")

#Process results.
response_dict = response.json()
repo_dicts = response_dict['items']

repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])
    
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)

#Make visualization
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'orange',
        'line': {'width': 1.5, 'color': 'red'}
    },
    'opacity': 0.6
}]

my_layout = {
    'title': 'Top-Starred Python Projects on GitHub',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='top_python_repos.html')
