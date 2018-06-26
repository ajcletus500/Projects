#! /usr/bin/env python2.7 

import json, requests

url = "https://totalhash.cymru.com/analysis/?1ce201cf28c6dd738fd4e65da55242822111bd9f"
htmlContent = requests.get(url, verify=False)
#print htmlContent
data = htmlContent.text
#print("data",data)
jsonD = json.dumps(htmlContent.text)
#print jsonD
#jsonL = json.loads(jsonD)
#print jsonL
ContentUrl = json.dumps({
    'url': str(url),
    'page_content': htmlContent,
    'indent':4
})
print ContentUrl

