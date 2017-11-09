import json, requests

companyList = []

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
    companyList.extend(data['ids'])

def run20Times(keywordsArray):
    for i in range(2):
        findIds(i, keywordsArray)

def scrapeKeywords(arrayOfArray):
    for i in range(len(keywords_to_scrape)):
        run20Times(keywords_to_scrape[i])
    print(companyList)

keywords_to_scrape = [['AI'],['AI', 'Asia'],['AI', 'Japan']]
scrapeKeywords(keywords_to_scrape)