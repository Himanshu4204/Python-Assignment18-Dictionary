# Q8.Write a python program to convert two lists into a dictionary in a way that item from list1 is the key 
#    and item from list2 is the value.?
list1=["Name","Age","Gender","Profession"]
list2=["Himanshu",20,"Male","Student"]
d1={list1[i]:list2[i] for i in range(len(list1))}
print(d1)