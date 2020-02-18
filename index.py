your_name=input("enter your name : ")
partner_name=input("enter partner name : ")
flames="flames"
empty_array=[]
#string to list conversion
def stringtolist(word): 
    return list(word) 
flames_inlist=stringtolist(flames)
your_name_inlist=stringtolist(your_name)
partner_name_inlist=stringtolist(partner_name)
count_ofyourname=0
if (len(partner_name_inlist)<len(your_name_inlist)):
    small_length_amongname=len(partner_name_inlist)
    small_name=partner_name_inlist
    large_length_amongname=len(your_name_inlist)
    large_name=your_name_inlist
else:
    large_length_amongname=len(partner_name_inlist)
    large_name=partner_name_inlist
    small_length_amongname=len(your_name_inlist)
    small_name=your_name_inlist
duplicate_count=0
count=0
for i in small_name:
    if i in large_name:
        duplicate_count=duplicate_count+1
remaining_smallname=small_length_amongname - duplicate_count
remaining_largename=large_length_amongname-duplicate_count
total_element_count= remaining_largename+remaining_smallname
for i in range(0,len(flames_inlist)-1):
     length_flames=len(flames_inlist)
     if(total_element_count<=6):
         removing_number=total_element_count
     else:
         removing_number=total_element_count - length_flames
     while(not (removing_number<=length_flames)):
             total_element_count=removing_number
             removing_number=total_element_count - length_flames
     total_element_count= remaining_largename+remaining_smallname
     removing_index = removing_number - 1
     flames_inlist.pop(removing_index)
     for element in range(removing_index,len(flames_inlist)):
         empty_array.append(flames_inlist[element])
     for element in range(0,removing_index):
         empty_array.append(flames_inlist[element])
     flames_inlist.clear()
     for element in empty_array:
         flames_inlist.append(element)
     empty_array.clear()
flames_dictionary={'f':'friend','l':'love','a':'affection','m':'marriage','e':'enemy','s':'sister'}
index=flames_inlist[0]
print("your relation  :",flames_dictionary.get(flames_inlist[0]))
    
     
     
     
