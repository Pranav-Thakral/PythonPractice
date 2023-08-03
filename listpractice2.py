#case sensetive sorting
names=['terry','Graham','John','eric','Terry','michel']
a=sorted(names)
print(a)
names.sort(key=str.casefold)
print(names)