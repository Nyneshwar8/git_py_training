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
    },
    1:2
}

print( list(myDict.keys())) #print the key of the dict and convert in list 
print(type(myDict.keys()))   #print the type of dict
print(myDict.values())    #print the value of dict
print(myDict.items())     #print the key and value of the dict
updatedict={
 "run":"250km",
}                            #update the element of dict 
myDict.update(updatedict)
print(myDict)
update1={
    "name":"ugale"               #updates the value also we have alredy given
}
myDict.update(update1)
print(myDict)