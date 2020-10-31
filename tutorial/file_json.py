# json: javascript object notation
import json

p = [
    {"id": "1", "name": "shoes", "publish": True},
    {"id": "2", "name": "cloth", "publish": False}
]

# Serialize
my_str = json.dumps(p)
print(my_str, type(my_str))

# Deserialize
my_obj = json.loads(my_str)
print(my_obj, type(my_obj))

# with open("category1.json", "w") as f:
#     json.dump(p, f)

# with open("category1.json") as f:
#     data  = json.load(f)
#     print(data)
