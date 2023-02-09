myDict={
    "name":"nyno",
    "age":"22",
    "antherdict":{
         "name":"nyno2",
         "age":[21]
    },
     "antherdict1":{
         "name":"nyno2",
         "age":[21]
    }
}

print(myDict["age"])
print(myDict["name"])
print(myDict["antherdict"]["age"])
print(myDict["antherdict1"]["age"])