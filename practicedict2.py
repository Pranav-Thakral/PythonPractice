dict1={'ten':10,'twenty':20,'thirty':30}
dict2={'thirty':30,'fourty':40,'fifty':50}
dict1.update(dict2)
print(dict1)


#using function ,creating another dictionary
def merge(dict1,dict2):
    get={**dict1,**dict2}
    return get
dict1={'ten':10,'twenty':20,'thirty':30}
dict2={'thirty':30,'fourty':40,'fifty':50}
dict3=merge(dict1,dict2)
print(dict3)

#using kewrg (**)
dict1={'ten':10,'twenty':20,'thirty':30}
dict2={'thirty':30,'fourty':40,'fifty':50}
dict4={**dict1,**dict2}
print(dict4)