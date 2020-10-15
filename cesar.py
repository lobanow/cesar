b = input('ввести фразу:')
a=''


for i in range(len(b)): 
    if(b[i]=="a"):
        a=a+"b"
    elif(b[i]=="b"):
        a=a+"c"
    elif(b[i]=="c"):
        a=a+"d"
    elif(b[i]=="d"):
        a=a+"e"
    elif(b[i]=="e"):
        a=a+"f"
    elif(b[i]=="f"):
        a=a+"g"
    elif(b[i]=="g"):
        a=a+"h"
    elif(b[i]=="h"):
        a=a+"i"
    elif(b[i]=="i"):
        a=a+"j"
    elif(b[i]=="j"):
        a=a+"k"
    elif(b[i]=="k"):
        a=a+"l"
    elif(b[i]=="l"):
        a=a+"m"
    elif(b[i]=="m"):
        a=a+"n"
    elif(b[i]=="n"):
        a=a+"o"
    elif(b[i]=="o"):
        a=a+"p"
    elif(b[i]=="p"):
        a=a+"q"
    elif(b[i]=="q"):
        a=a+"r"
    elif(b[i]=="r"):
        a=a+"s"
    elif(b[i]=="s"):
        a=a+"t"
    elif(b[i]=="t"):
        a=a+"u"
    elif(b[i]=="u"):
        a=a+"v"
    elif(b[i]=="v"):
        a=a+"w"
    elif(b[i]=="w"):
        a=a+"x"
    elif(b[i]=="x"):
        a=a+"y"
    elif(b[i]=="y"):
        a=a+"z"
    elif(b[i]=="z"):
        a=a+"a"
    elif(b[i]==" "):
        a=a+" "
    else:
        print("ошибка ввода (используйте латиницу и пробел)") 
        a="ошибка"
        break
print("\nзашифровано")
print(a, "\n")
print("дешифровка")

a=''

for i in range(len(b)):
    if(b[i]=="a"):
        a=a+"z"
    elif(b[i]=="b"):
        a=a+"a"
    elif(b[i]=="c"):
        a=a+"b"
    elif(b[i]=="d"):
        a=a+"c"
    elif(b[i]=="e"):
        a=a+"d"
    elif(b[i]=="f"):
        a=a+"e"
    elif(b[i]=="g"):
        a=a+"f"
    elif(b[i]=="h"):
        a=a+"g"
    elif(b[i]=="i"):
        a=a+"h"
    elif(b[i]=="j"):
        a=a+"i"
    elif(b[i]=="k"):
        a=a+"j"
    elif(b[i]=="l"):
        a=a+"k"
    elif(b[i]=="m"):
        a=a+"l"
    elif(b[i]=="n"):
        a=a+"m"
    elif(b[i]=="o"):
        a=a+"n"
    elif(b[i]=="p"):
        a=a+"o"
    elif(b[i]=="q"):
        a=a+"p"
    elif(b[i]=="r"):
        a=a+"q"
    elif(b[i]=="s"):
        a=a+"r"
    elif(b[i]=="t"):
        a=a+"s"
    elif(b[i]=="u"):
        a=a+"t"
    elif(b[i]=="v"):
        a=a+"u"
    elif(b[i]=="w"):
        a=a+"v"
    elif(b[i]=="x"):
        a=a+"w"
    elif(b[i]=="y"):
        a=a+"x"
    elif(b[i]=="z"):
        a=a+"y"
    elif(b[i]==" "):
        a=a+" "
    else:
        a="ошибка"
        break

print(a) 
c=input()
