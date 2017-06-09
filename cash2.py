resto100 = 0
resto50 = 0
resto20 = 0
resto10 = 0
resto5 = 0
resto2 = 0
q100 = 0
q50 = 0
q20 = 0
q10 = 0
q5 = 0
q2 = 0


num = int(input("digite o valor que deseja sacar"))
resto100 = num % 100
q100 = (num - resto100) / 100

resto50 = resto100 % 50
q50 = (resto100 - resto50) / 50

resto20 = resto50 % 20
q20 = (resto50 - resto20) / 20

resto10 = resto20 % 10
q10 = (resto20 - resto10) / 10

resto5 = resto10 % 5
q5 = (resto10 - resto5) / 5

resto2 = resto5 % 2
q2 = (resto5 - resto2) / 2


if(resto2 != 0):
    if(q5 > 0):
        q5 = (q5-1)
        q2 = (q2+3);
    elif(q5 == 0):
        if(q10 > 0):
            q10 = (q10-1)
            q5 = (q5+1)
            q2 = (q2+3);
        elif(q10 == 0):
            if(q20 > 0):
                q20 = (q20-1)
                q10 = (q10+1)
                q5 = (q5+1)
                q2 = (q2+3);
            elif(q20 == 0):
                if(q50 > 0):
                    q50 = (q50-1)
                    q20 = (q20+2)
                    q5 = (q5+1)
                    q2 = (q2+3);
                elif(q50 == 0):
                    q100 = (q100-1)
                    q50 = (q50+1)
                    q20 = (q20+2)
                    q5 = (q5+1)
                    q2 = (q2+3);                
        

if(q100 > 0):
        print(q100,"notas de 100");
if(q50 > 0):
        print(q50,"notas de 50");
if(q20 > 0):
        print(q20,"notas de 20");
if(q10 > 0):
        print(q10,"notas de 10");
if(q5 > 0):
        print(q5,"notas de 5");
if(q2 > 0):
        print(q2,"notas de 2");
