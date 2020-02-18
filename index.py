
'''list0=[]
list1=[]
list2=[]
arr=[]
n1 =int( input("Enter number of elements of input1 : "))
for i in range(0, n1): 
    ele1 = input("enter element")
    list1.append(ele1) # adding the element 
n2 =int(input("Enter number of elements of input2 : "))
for i in range(0, n2): 
    ele2 = input("enter element")
    list2.append(ele2) # adding the element 
n = int(input("Enter number of elements  : "))
for i in range(0, n): 
    ele0 = input("enter element")
    list0.append(ele0) # adding the element '''
list0=['f','l','a','m','e','s']
list1=['j','a','m','e','e','l','a']
list2=['s','h','a','h','i','n','a']
arr=[]
count=0
for i in list1:
    if i not in list2:
        count = count+1
#print(count)
dup_count=len(list1)-count
elementscount_oflist2=len(list2)-dup_count
total_element_count= count+elementscount_oflist2
#print(total_element_count)

for i in range(0,len(list0)-1):
    length_list0=len(list0)
    c=total_element_count-length_list0

    while(not (c<=length_list0)):
        total_element_count=c
        c=total_element_count-length_list0
    total_element_count= count+elementscount_oflist2
    #print("removing index",c)
    rem_ele=c-1
    list0.pop(rem_ele)
    #print(list0)
    j=rem_ele
    for j in range(rem_ele,len(list0)):
        arr.append(list0[j])
    #print(arr)
    for i in range(0,rem_ele):
        arr.append(list0[i])
    #print(arr)
    list0.clear()
    #print(list0)
    for i in arr:
        list0.append(i)
    arr.clear()
   # print(list0)
print(list0) 



