import json

strings = {"query" : "json_query"}

loads_str = json.dumps(strings)

str_lo = json.loads(loads_str)

print(str_lo)