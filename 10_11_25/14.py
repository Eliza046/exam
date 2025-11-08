from string import printable
a = printable[:9]
summa = []

for x in a:
    for y in a:
        s = int('88'+x+'4'+y, 9)+int('7'+ x + '44'+y, 11)
        if s % 61 ==0:
            summa.append(s)
print(min(summa)//61)