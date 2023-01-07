import json
jess = '{"name": "Jessica Wilkins", "hobbies": ["music", "watching TV", "hanging out with friends"]}'

jess_dict = json.loads(jess)

# print(jess_dict)
print(json.dumps(jess_dict, indent=4))
print(jess_dict['hobbies']) # Обратиться к конкретному ключу чтобы вывести значение



import json

with open('fcc.json', 'r') as fcc_file:
    fcc_data = json.load(fcc_file)
    print(fcc_data)