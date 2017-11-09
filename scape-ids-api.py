import json, requests

def findIds(page):
    url = 'https://angel.co/company_filters/search_data'
    headers = {'X-Requested-With': 'XMLHttpRequest'}
    payload = {
        'filter_data[keywords]':'ai',
        'sort':'joined',
        'filter_data[keywords]':'asia',
        'page':page
    }
    r = requests.post(url, headers=headers, data=payload)
    data = json.loads(r.text)
    print data['ids']

def run20Times():
    for i in range(20):
        findIds(i)

run20Times()