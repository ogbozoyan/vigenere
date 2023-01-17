import string
eng = 26
rus = 33
def encrypt(text,key,m):
    c = 0
    space = ' '
    encrypted = ''
    for j in range(len(text)):
        if m == 26:
            if (text[j].isalpha()):
                if(text[j].islower()):
                    key = key.lower()
                    c = (((ord(text[j])-97)+(ord(key[j])-97))%m)+97
                    encrypted += chr(c)
                elif(text[j].isupper()):
                    key = key.upper()
                    c = (((ord(text[j])-65)+(ord(key[j])-65))%m)+65
                    encrypted += chr(c)
            elif(text[j] == ' '):
                encrypted += space
        elif m == 33:
            if (text[j].isalpha()):
                if(text[j].islower()):
                    key = key.lower()
                    c = (((ord(text[j])-1072)+(ord(key[j])-1072))%m)+1072
                    encrypted += chr(c)
                elif(text[j].isupper()):
                    key = key.upper()
                    c = (((ord(text[j])-1040)+(ord(key[j])-1040))%m)+1040
                    encrypted += chr(c)
            elif (text[j] == ' '):
                encrypted += space
                
    return encrypted
def decrypt(text,key,m):
    c = 0
    space = ' '
    decrypted = ''
    for j in range(len(text)):
        if m == 26:
                if (text[j].isalpha()):
                    if(text[j].islower()):
                        key = key.lower()
                        c = (((ord(text[j])-97+m)-(ord(key[j])+m-97))%m)+97
                        decrypted += chr(c)
                    elif(text[j].isupper()):
                        key = key.upper()
                        c = (((ord(text[j])-65+m)-(ord(key[j])+m-65))%m)+65
                        decrypted += chr(c)
                elif(text[j] == ' '):
                    decrypted += space
        elif m == 33:
                if (text[j].isalpha()):
                    if(text[j].islower()):
                        key = key.lower()
                        c = (((ord(text[j])+m-1072)-(ord(key[j])+m-1072))%m)+1072
                        decrypted += chr(c)
                    elif(text[j].isupper()):
                        key = key.upper()
                        c = (((ord(text[j])+m-1040)-(ord(key[j])+m-1040))%m)+1040
                        decrypted += chr(c)
                elif (text[j] == ' '):
                    decrypted += space
                
    return decrypted
def key_fix(key):
    w = 0 #interator for key 
    space = ' '
    key = key.split()#spliting specially for cleaning spaces 
    key = "".join(key)# making list -> str 
    lenkey = len(key) #that's for %calculatiion
    k = ['0']*len(text)#making enmpty k for future filling area 
    for i in range(len(k)):
        if(text[i].isalpha()):
            k.append(key[w%lenkey])#cicling our key
            w+=1
        elif(text[i] == ' '):
            k.append(space) # if we got space in text we fill key with space's and don't interate our key
    k = "".join(k)#transofmation list to str
    return k.strip('0')
print("Made by @ogbozoyan_13 - inst ")
print("This's Vigenère cipher works on 2 languages")
print("Choose your language : eng - e , rus - r ")
while 1:
    mode = input("Language : ")
    if mode == 'e':
        print("what do you want enc - e or dec - d: ")
        mode1 = input("Mode ")
        if mode1 == 'e':
            text = input('Input Your text: ')
            key = input("Key: ")
            k = key_fix(key)
            res = encrypt(text,k,eng)
            print(res)
        elif mode1 == 'd':
            text = input('Input Your text: ')
            key = input("Key: ")
            k = key_fix(key)
            res = decrypt(text,k,eng)
            print(res)
        else:
            print("Wrong operation")
    elif mode == 'r':
        print("Что вы хотите сделать зашифровать - e или расшифровать - d: ")
        mode1 = input("Режим: ")
        if mode1 == 'e':
            text = input('Введите ваш текст: ')
            key = input("Ключ: ")
            k = key_fix(key)
            res = encrypt(text,k,rus)
            print(res)
        elif mode1 == 'd':
            text = input('Введите ваш текст: ')
            key = input("Ключ: ")
            k = key_fix(key)
            res = decrypt(text,k,rus)
            print(res)
        else:
            print("Неправильная операция")
    else:
        print("Wrong mode")
