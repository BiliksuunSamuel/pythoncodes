# implementing the principle or idea of buble sorting in python
# sorting by descending order and ascending order

def sortAs(list):
    for i in range(len(list)//2):
        for j in range(len(list)//2-1):
            if(list[j]>list[j+1]):
                t=list[j]
                list[j]=list[j+1]
                list[j+1]=t
    print("the sorted list in ascending order is\n",list)    

# sorting the list by descending order
def sortDe(list):
    for i in range(len(list)//2):
        for j in range(len(list)//2-1):
            if(list[j]<list[j+1]):
                t=list[j]
                list[j]=list[j+1]
                list[j+1]=t
    print("the sorted list in descending order of magnitude is \n ",list)   

#sorting by selection of the list of unsorted values
def sortSel(list):
    for i in range(len(list)):
        minpos=i
        for j in range(i,len(list)):
            if(list[j]<list[minpos]):
                minpos=j
        t=list[i]
        list[i]=list[minpos]
        list[minpos]=t
    #printing the results of the sorting
    print("the results of sorting the elements by selection method is\n",list)                         

# declaring my list of the unsorted data
lst=[5,8,12,100,0,4,6,9,2];

#sortDe(lst)      
#sortAs(lst)      
#print(max(lst))
sortSel(lst)