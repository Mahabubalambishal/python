#dictionary te kono item change kora
dictionary={
    "mahabub":{
        "name":"mahabub",
        "profession":"student",
        "religion":"islam",
        "distric":"dinajpur"
    },
    "saikat":{
        "name":"saikat",
        "roll":3,
        "class":"five",
        "thana":"parbotipur"
    }
}
dictionary["distric"]="rangpur"
#print(dictionary)
#print(dictionary["distric"])

#update method use kore
dictionary={
    "mahabub":{
        "name":"mahabub",
        "profession":"student",
        "religion":"islam",
        "distric":"dinajpur"
    },
    "saikat":{
        "name":"saikat",
        "roll":3,
        "class":"five",
        "thana":"parbotipur"
    }
}
dictionary.update({"name":"bishal"})
print(dictionary["name"])