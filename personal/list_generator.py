import json

with open('./mks-settings/report-request-microservice.json', 'r') as json_file:
    json_data = json.load(json_file)

# Рекурсивный генератор, который будет сканировать структуру вложенного списка/словаря,
# как если бы вы загружали JSON в Python. Он показывает вам последовательность ключей словаря
# и индексов списка, связанных с каждым значением.
def show_indices(obj, indices):
    for k, v in obj.items() if isinstance(obj, dict) else enumerate(obj):
        if isinstance(v, (dict, list)):
            yield from show_indices(v, indices + [k])
        else:
            yield indices + [k], v

for keys, v in show_indices(json_data, []):
    print(keys, v)

# print(keys)

# Достк к любому элементу
keys = [0, 'version', 'hotfix', '0.6.1']
obj = json_data
for k in keys:
    obj = obj[k]
print(obj)

# Если хотим изменить элемент
keys = [0, 'version', 'hotfix', '0.6.1', 'from']
obj = json_data
for k in keys[:-1]:
    obj = obj[k]
obj[keys[-1]] = "some new thing"
print(json_data[1]['company'])