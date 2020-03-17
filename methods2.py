from tkinter import *

root = Tk()
root.geometry ('800x500')

var = IntVar ()
var.set (0)








def get_ord_list(word):
    l = []
    for i in word:
        l.append(ord(i))
    return l


def normolize_key(key):
    #    if key > 0:
    #        key=key%25
    #    else:
    #        key=key%26
    #    return key
    return key % 26


# def normolize_ord (input_list):
#    for i in range (len(input_list)):
#        if input_list[i]>90:              # >= 90 or >90 ?
#            input_list[i] = 64+(input_list[i]%90) #64  or 65
#        if input_list[i]<65 and input_list[i]!=32: #<= 65 or <65
#            input_list[i] = 91 - (65 - input_list[i]) #91 or 90


def modify_ord_list(input_list, key):
    for i in range(len(input_list)):
        if input_list[i] != 32:
            if (input_list[i] + key > 90 and input_list[i] <= 90) or (
                    (input_list[i] + key) > 122 and input_list[i] >= 97):
                input_list[i] -= 26

            #            if input_list[i] + key > 122:
            #                input_list[i] -= 26
            input_list[i] = input_list[i] + key
    return input_list

def deparaphrase(input_list, key):
    for i in range(len(input_list)):
        if input_list[i] != 32:
            if ((input_list[i] - key) < 65 and input_list[i] <= 90) or (
                    (input_list[i] - key) < 97 and input_list[i] >= 97):
                input_list[i] += 26
            input_list[i] = input_list[i] - key
    return input_list

def get_string(input_list):
    s = ''
    for i in input_list:
        s += chr(i)
    return s

""":returns encrypted string"""
def encrypt(string,key):
    return  get_string(modify_ord_list(get_ord_list(string), normolize_key(key)))


def encrypt_button ():
    s = encrypt(entry_the_text.get(), int(entry_the_key.get()))
    insert_the_code.insert(0, s)


def decrypt(string, key):
    return get_string(deparaphrase(get_ord_list(string), normolize_key(key)))

def decrypt_button ():
    s = decrypt(entry_the_code.get(), int(entry_the_key.get()))
    insert_the_original.insert(0, s)



#Titles
enter_the_text = Label(text='Enter your text:',font="Arial 14")
enter_the_text.place(x=180, y=100)

enter_the_key = Label(text='Enter your key:',font="Arial 14")
enter_the_key.place(x=320, y=10)

choose_the_method = Label(text='Choose the method', bg='black', fg='white', font="Arial 14")
choose_the_method.place(x=10, y=10)

ciphered_text = Label(text='Your new ciphered text:',font="Arial 14")
ciphered_text.place(x=180, y=230)

enter_the_ciphered_text = Label(text='Enter some ciphered text:',font="Arial 14")
enter_the_ciphered_text.place(x=180, y=300)

original_text = Label(text='Your original text:',font="Arial 14")
original_text.place(x=180, y=410)




#Input fields
entry_the_text = Entry (width=50, font='Arial 16')
entry_the_text.place(x=180, y=130)

entry_the_key= Entry (width=10, font='Arial 17')
entry_the_key.place(x=320, y=40)

insert_the_code= Entry (width=50, font='Arial 16')
insert_the_code.place(x=180, y=260)

entry_the_code= Entry (width=50, font='Arial 16')
entry_the_code.place(x=180, y=330)

insert_the_original= Entry (width=50, font='Arial 16')
insert_the_original.place(x=180, y=440)

entry_the_key2 = Entry (width=10, font='Arial 17')
entry_the_key2.place(x=420, y=40)

#Methods
cesar = Radiobutton(text='Cesar method',  variable=var, value = 0, font='18')
cesar.place(x=10, y=40)

method2 = Radiobutton(text='method2', variable=var, value = 1, font='18')
method2.place(x=10, y=60)

method3 = Radiobutton(text='method3', variable=var, value = 2, font='18')
method3.place(x=10, y=80)

method4 = Radiobutton(text='method4', variable=var, value = 3, font='18')
method4.place(x=10, y=100)




#Buttons
b_encrypt = Button(text='Encrypt', width=10, height=1, bg='red', font='Arial 14', command=encrypt_button)
b_encrypt.place(x=400, y=170)

b_decrypt = Button(text='Decrypt', width=10, height=1, bg='green', font='Arial 14', command=decrypt_button)
b_decrypt.place(x=400, y=370)





root.mainloop()
