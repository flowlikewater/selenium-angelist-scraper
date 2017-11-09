import json, requests

url = 'https://angel.co/company_filters/search_data'
headers = {'X-Requested-With': 'XMLHttpRequest'}
payload = {
    'filter_data[keywords]':'ai',
    'sort':'joined',
    'filter_data[keywords]':'asia',
    'page':'1'
}
r = requests.post(url, headers=headers, data=payload)
data = json.loads(r.text)
print data['ids']