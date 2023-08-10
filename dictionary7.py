#how to update key in dictionary
sample_dict={
    "name":"kelly",
    "age":27,
    "salary":5000,
    "city":"new york"
}
sample_dict["location"]=sample_dict["city"]
sample_dict.pop("city")
print(sample_dict)