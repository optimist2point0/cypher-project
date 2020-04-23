

#def remember_low_indexes (input_string):
#    index_list=[]
#    for i in range (len(input_string)):
#        if 97<= ord(input_string[i]) <=122:
#            index_list.append(i)
#    return index_list
            
                    



def get_ord_list (word):
    l=[]
    for i in word:
        l.append(ord(i))
    return l


def normolize_key (key):
#    if key > 0:
#        key=key%25
#    else:
#        key=key%26
#    return key
    return key%26

#def normolize_ord (input_list):
#    for i in range (len(input_list)):
#        if input_list[i]>90:              # >= 90 or >90 ?
#            input_list[i] = 64+(input_list[i]%90) #64  or 65
#        if input_list[i]<65 and input_list[i]!=32: #<= 65 or <65
#            input_list[i] = 91 - (65 - input_list[i]) #91 or 90




def modify_ord_list (input_list, key):
    for i in range (len(input_list)):
        if input_list[i]!=32:
            if (input_list[i] + key > 90  and input_list[i] <=90 ) or ((input_list[i] + key) > 122 and input_list[i] >= 97):
                input_list[i] -= 26

#            if input_list[i] + key > 122:
#                input_list[i] -= 26
            input_list[i]=input_list[i]+ key


def deparaphrase (input_list, key):
    for i in range(len(input_list)):
        if input_list[i]!=32:
            if((input_list[i] - key) < 65  and input_list[i] <=90)  or ((input_list[i] - key) < 97 and input_list[i] >= 97):
                input_list[i] += 26
            input_list[i]=input_list[i]-key






def get_string (input_list):
    s=''
    for i in input_list:
            s += chr(i)
    return s

'''#def get_final_string (input_list):
#   s=''
#    for i in range(len(input_list)):
 #       if i in low_index:
  #          s += chr(input_list[i]+32)
   #     else:
    #        s += chr(input_list[i])
    #return s'''

key = normolize_key(int(input('key=')))
test_phrase=input('test fraze =')

print (get_ord_list(test_phrase))

#low_index=remember_low_indexes(test_phrase)

""":returns encrypted string"""
def encrypt(string,key):
    return  get_string(modify_ord_list(get_ord_list(string),key))


def decrypt (string, key):
    return get_string(deparaphrase(get_ord_list(string), key))

test_list=get_ord_list(test_phrase)

modify_ord_list(test_list, key)

print(test_list)
print (get_string(test_list))
deparaphrase(test_list, key)
print (test_list)

'''result_strig=get_string(test_list)'''
print (get_string(test_list))




    
            
