from requests import * 

# All needed headers
header= {'User-agent':'PicoBrowser',
'Referer':'http://mercury.picoctf.net:39114/',
'Date':'Wed, 21 Oct 2018 07:28:00 GMT',
'dnt':'1',
'X-Forwarded-For': '31.15.32.0',
'Accept-Language': 'sv'}

html_content = get("http://mercury.picoctf.net:39114/", headers=header) # GET method
print(html_content.content.decode()) #The content
