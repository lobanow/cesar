key=100#ключ для первичного вызова


b = input('ввести фразу:')#Ввод фразы

b=b.lower()
while(key>26 or key<0):#контроль приемлимости ключа
    print("введите смещение от 0 до 26")
    key = int(input('ввести ключ:'))#Ввод ключа

a=[]
ctrl=0#контроль ввода сивола
alph = "abcdefghijklmnopqrstuvwxyz"
alph1 = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"#второй алфавит для смещения

for i in range(len(b)): #перевод фразы в цифры
    a+=[0]

    for j in range(len(alph)-1):

        if (b[i]==alph[j]):
            a[i]=j
            ctrl=1
        elif (b[i]==" "):
            a[i]=" "
            ctrl=1
        

    if(ctrl!=1):
        print("используйте латиницу и пробел") #Вывод ошибки при неизветном символе
        a[0]=404
        break
    ctrl=0
    
    
out=""
print("зашифровано ")
for i in range(len(b)): #смещение+
    if (a[i]==" "):
        out+=" "
    elif (a[i]==404):
        print("ошибка")
        break
    else:
        out+=alph1[a[i]+key]#вывод текста
print(out)


out=""
print("дешифровано ")
for i in range(len(b)): #смещение -
    if (a[i]==" "):
        out+=" "
    elif (a[i]==404):
        print("ошибка")
        break
    else:
        out+=alph1[a[i]+26-key]#вывод текста
print(out)

c=input()#Заглушка, чтобы не закрывалось
