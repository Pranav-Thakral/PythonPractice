my_dict={"india":"delhi",
         "pakistan":"islamabad",
         "UAE":"Abu DAbhi"}
print(my_dict)
print(my_dict["pakistan"])
my_dict["india"]="new delhi"
print(my_dict)
my_dict["germany"]="berlin"
print(my_dict)
element=my_dict.pop("germany")
print(my_dict)
print(element)