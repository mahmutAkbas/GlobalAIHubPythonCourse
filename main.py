odd_list=list(range(1,30,2))
even_list=list(range(0,30,2))
newList=[i**2 for i in (odd_list+even_list)]
for i in newList:
  print(type(i))