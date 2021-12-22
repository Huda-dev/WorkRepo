

f= open("primery.txt", "w")
for i in range(1, 251):
    if i > 1:
        for j in range(2, i):
            if(i % j == 0):
                break
        else:
            f.write(str(i) +"\n")
f.close()