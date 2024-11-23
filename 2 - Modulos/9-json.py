import json

# 1 - Strings para Dicionários
person = '{"name":"Daniel", "languagens":["Python", "Java"]}'
person_dict = json.loads(person)
print(person_dict)  # {'name': 'Daniel', 'languagens': ['Python', # 'Java']}
print(person_dict['languagens']) 

# 2 - Convertendo dicionário para JSON
person_json = json.dumps(person_dict)
print(person_json)  # {"name": "Daniel", "languagens": ["Python", # "Java"]}
print(type(person_json))
print(type(person_dict))

# 3 - Formatando JSON
print(json.dumps(person_dict, indent=4, sort_keys=True))

# 4 - Salvando json em txt
with open('person.json', 'w') as json_file:
    json.dump(person_dict, json_file)
    
# 5 - Lendo json externo
with open('person.json', 'r') as f:
    data = json.load(f)
    print(data)  # {'name': 'Daniel', 'languagens': ['Python', #