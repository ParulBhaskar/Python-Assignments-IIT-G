#To create a list of length 15 and sort in ascending order

List = [22,12,34,52,21,67,32,1,4,87,65,89,23,56,76]

for j in range(len(List)):
    #initially swapped is false
    swapped = False
    i = 0
    while i<len(List)-1:
        #comparing adjacent elements
        if List[i]> List[i+1]:
            #Swapping adjacent values in ascending order
            List[i],List[i+1] = List[i+1],List[i]
            swapped = True
        i = i+1
    #swap till end of loop
    if swapped == False:
        break
print (List)
