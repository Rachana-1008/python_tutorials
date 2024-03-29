list1 =[1,2,3,4,5,6]

even= lambda num : num%2==0
even_list= list(filter(even,list1))
print("Even numbers in the list are: ", even_list)


list2 =[1,2,3,4,5,6]

square = lambda num : num **2
square_list= list(map(square,list2))
print(square_list)

import functools
list3 =[1,2,3,4,5,6]
small = functools.reduce(lambda x,y: x if x<y else y,list3)
print("the smallest num is:", small)

import functools
list4 =[1,2,3,4,5,6]
add = functools.reduce(lambda x,y: x+y,list4)
print("the addition is:", add)

