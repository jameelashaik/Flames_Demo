your_name=input("enter your name")
partner_name=input("enter partner name")
flames="flames"
empty_array=[]
#string to list conversion
def stringtolist(word): 
    return list(word) 
flames_inlist=stringtolist(flames)
your_name_inlist=stringtolist(your_name)
partner_name_inlist=stringtolist(partner_name)
count_ofyourname=0
for i in your_name_inlist:
    if i not in partner_name_inlist:
        count_ofyourname=count_ofyourname+1
duplicate_count=len(your_name_inlist)-count_ofyourname
elementscount_of_partner_name=len(partner_name_inlist) - duplicate_count
total_element_count= count_ofyourname + elementscount_of_partner_name
for i in range(0,len(flames_inlist)-1):
     length_flames=len(flames_inlist)
     removing_number=total_element_count - length_flames
     while(not (removing_number<=length_flames)):
             total_element_count=removing_number
             removing_number=total_element_count - length_flames
     total_element_count= count_ofyourname+elementscount_of_partner_name
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
    
     
     
     
