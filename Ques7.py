# Q7. Write a python program to create three dictionaries, then create one dictionary that will contain the other three dictionaries.?
d1={"Name":"Himanshu"}
d2={"Age":20}
d3={"Gender":"Male"}
d={}
d.update(d1)
d.update(d2)
d.update(d3)
print(d)
