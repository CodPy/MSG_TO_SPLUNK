import pymqi
import os
import  requests


# Параметры подключения SPLUNK
url_splunk = '10.99.16.77'
port_splunk = '8088'
securitytoken_splunk = """5af3ea57-bca1-45cf-ae82-2275d038de58"""


#содаем сообщение для записи в SPLUNK
def create_splunk_message(url,queue, depth):
    dictjson = {
        "index": 'int_status',
        "sourcetype": "JSON",
        "event": {
            "url": url,
            "Message": 'Completed',
            "Queue": queue,
            "Action": 'Read_Queue_Depth',
            "System_Create_Log":'Python_script',
            "Depth":depth
        }
    }
    return dictjson


#Запись соообщения в SPLUNK
def writejsontosplunk (jsontext,adr,port_,token_):
    url =adr
    port = port_
    securitytoken = token_
    os.environ['NO_PROXY'] = url
    # authHeader = {'Authorization': 'Splunk {}'.format(securitytoken)}

    authHeader = {'Authorization': 'Splunk {}'.format(securitytoken),'Content-type': 'application/json; profile=urn:splunk:event:1.0; charset=utf-8'}

    #print (authHeader)
    jsonDict = jsontext
    try:
     #print('''https://''' + url + ':' + port + '/services/collector/event''')
     r1 = requests.post('''http://''' + url + ':' + port + '/services/collector/event', headers=authHeader,json=jsonDict, verify=False)
     #print ('''https://''' + url + ':' + port + '/services/collector/event''')
     d = eval(r1.text)
     r = (d["code"])
    except:
        r=777
    return r






