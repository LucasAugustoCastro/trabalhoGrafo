f=open('9')
lines=f.readlines()
linha1  = lines[2][6:].replace('\n', '')
linha2  = lines[3][4:].replace('\n', '')
f.close()



print(linha1)
print(linha2)
