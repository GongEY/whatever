import json

#incoding
'''
customer = {
    'id': 152352,
    'name': '강진수',
    'history':[
        {'date': '2015-03-11', 'item': 'iPhone'},
        {'date': '2016-02-23', 'item': 'Monitor'},
    ]
}

jsonString = json.dumps(customer)

print(jsonString)
print(type(jsonString))
'''

#decoding
jsonString = '{"name": "강진수", "id": 152352, "history": [{"date": "2015-03-11", "item": "iPhone"}, {"date": "2016-02-23", "item": "Monitor"}]}'

dict = json.loads(jsonString)

print(dict['name'])
for h in dict['history']:
    print(h['date'], h['item'])