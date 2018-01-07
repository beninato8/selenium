import urllib.request
import json 

with urllib.request.urlopen("http://gimmeproxy.com/api/getProxy?country=US") as url:
    data = json.loads(url.read().decode())

try: 
    IP = data['ip'] 
    PORT = data['port']

    IP = IP.replace(':','') 
    IP = IP.replace('','') 
    IP = IP.replace(' ','') 
    IP = IP.replace('\n','') 
    IP = IP.replace('ip','') 

    PORT = PORT.replace(':','') 
    PORT = PORT.replace('"','') 
    PORT = PORT.replace(' ','') 
    PORT = PORT.replace('\n','') 
    PORT = PORT.replace('port','') 

    string_proxy = IP + ':' + PORT 
    print('PROXY: ' + string_proxy)

    f = open('proxy_file.txt','w') 
    f.write(string_proxy) 
    f.close() 
except: 
    print("Error requesting proxy")
    f = open('proxy_file.txt','w') 
    f.write('0') 
    f.close() 