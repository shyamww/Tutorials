import random
import json

def fn_d():
    return 5

def fn_topic():
    topic_list = ["TEMPERATURE", "HUMIDITY", "GENERAL"]
    return random.choice(topic_list)

x =  { 
        "Topic": fn_topic(),
        "Data": fn_d()
    }
print(type(x))
print(x["Topic"])
print(x)
# jsonObj = json.loads(x) #string to json

y=json.dumps(x) # json to string
print(type(y))





#  # Python program to update
# # JSON


# import json

# # JSON data:
# x = { "organization":"GeeksForGeeks",
# 		"city":"Noida",
# 		"country":"India"}

# # python object to be appended
# y = {"pin":110096}

# # parsing JSON string:
# z = json.loads(x)

# # appending the data
# z.update(y)

# # the result is a JSON string:
# print(json.dumps(z))
