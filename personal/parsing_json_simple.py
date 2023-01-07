import json

with open('./mks-settings/report-request-microservice.json', 'r') as json_file:
    json_data = json.load(json_file)

# print(json_data[0]['version']['release']) #обратиться к словарю внутри списка

versions = json_data[0]['version']
print(json.dumps(versions, indent=4))
for i in versions:
    print(i)
