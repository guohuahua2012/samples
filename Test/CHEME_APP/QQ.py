
list1 = ['a','b']
list2 = ['c','d','r',['o']]
list3 = []

list3.extend(list1)
list3.extend(list2)

list3.append('e')
print(list3)