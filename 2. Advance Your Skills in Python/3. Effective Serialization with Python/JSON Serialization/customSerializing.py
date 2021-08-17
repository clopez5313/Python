import json
from event import event
from custom import default, pairs_hook

data = json.dumps(event, default=default)
print(json.loads(data))
print(json.loads(data, object_pairs_hook=pairs_hook))
