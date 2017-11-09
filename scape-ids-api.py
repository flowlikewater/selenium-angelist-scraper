import json, requests

def findIds(page, array):
    payloadKeywords = ''
    for i in range(len(array)):
        payloadKeywords += '"filter_data[keywords]":"' + str(array[i]) + '",'
    payloadKeywords =  '{' + payloadKeywords + '"sort":"joined",' + '"page":' + str(page) + '}'
    print(payloadKeywords)
    url = 'https://angel.co/company_filters/search_data'
    headers = {'X-Requested-With': 'XMLHttpRequest'}
    payload = json.loads(payloadKeywords)
    r = requests.post(url, headers=headers, data=payload)
    data = json.loads(r.text)
    print data
    print data['ids']

def run20Times():
    for i in range(2):
        findIds(i, ['AI', 'Asia'])

keywords_to_scrape = [['AI'],['AI', 'Asia'],['AI', 'Japan']]

# run20Times()

findIds(1,['AI', 'Asia'])
findIds(2,['AI', 'Asia'])