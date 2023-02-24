j_data1 = {
    "key1":"data1",
    "key2":"data2",
    "key3":"data3",
    "key4":["in_data1", "in_data2"]
}
j_data2 = {
    "key4":"data1",
    "key5":"data2",
    "key6":"data3",
    "key7":[100, "data"]
}
#all_data=j_data1+j_data2

import json

with open("data.json", "w") as f:
    json.dump(j_data1, f)
    json.dump(j_data2, f)