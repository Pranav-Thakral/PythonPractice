#how to get minimum values in dictionary
dict={"physics":82,
      "math":65,
      "history":75
     }
temp=min(dict.values())
res = [key for key in dict if dict[key] == temp]
print(res)
