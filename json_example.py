#conver from json to python dict

import json
json_string = '{"name": "John", "age": 30, "city": "New York"}'
python_dict = json.loads(json_string)
print(python_dict)

#conver from python dict to json
import json
python_dict = {"name": "John", "age": 30, "city": "New York"}
json_string = json.dumps(python_dict)
print(json_string)

