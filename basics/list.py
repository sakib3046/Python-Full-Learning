#............... List important Methods..................#

numberList = [5,7,3,2]
print("The initial list is:",numberList)

#reversing list

numberList.reverse()
print("After reverse the list is:",numberList)

#appending element 

numberList.append(1)
print("After appending the list is:",numberList)

#sorting element

numberList.sort()
print("After sorting the list is:",numberList)


#reverse sorting element

numberList.sort(reverse=True)
print("After reverse sorting the list is:",numberList)


#inserting element to the specific index

numberList.insert(1,5)
print("After inserting 1 to the 2nd index the list is:",numberList)

#remove elment occurrence of element

numberList.remove(1)
print("After removing the last element of the list is:",numberList)


#remove elment by index

numberList.pop(2)
print("After removing the 3rd index element of the list is:",numberList)
