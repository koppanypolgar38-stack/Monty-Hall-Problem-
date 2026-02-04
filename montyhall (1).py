""" E programot magam kódoltam, nem másoltam vagy írtam át más kódját, és nem adtam át másnak! Polgár Koppány """


from random import randint  
def monty_func(x,y,z):
    suc1=0
    suc2=0
    suc3=0
    fail=0
    #musorvezeto: amely ajtót a műsorvezető kinyitja
    #jatekos= amley ajtrja a játkékos rámutat
    #nyeremeny: amely ajtó mögött a nyeremény van
    for i in range(x):
        nyeremeny=randint(0,2)
        l=[0,0,0]
        l_eredeti=l.copy()
        l[nyeremeny]=1
        l_nyeremeny=l.copy()
        jatekos=randint(0,2)
        l[jatekos]=2
        l_jatekos=l.copy()
        for i in range(0,3):
            if l.count(0)==1:
                for k in range(0,3):
                    if l[k]==0:
                        musorvezeto=k
                        break
            else:
                showman=[]
                for k in range(0,3):
                    if l[k]==0:
                        showman.append(k)
                sh=randint(0,1)
                musorvezeto=showman[sh]
                            
        
        
        for j in range(1):
            jatekos_dontes2=jatekos
            if jatekos_dontes2==nyeremeny:
                suc1+=1
            else:
                continue
        #print(l,nyeremeny,jatekos,musorvezeto)
   
    for i in range(y):
        nyeremeny2=randint(0,2)
        
       
        l=[0,0,0]
        l_eredeti=l.copy()
        l[nyeremeny2]=1
        l_nyeremeny2=l.copy()
        jatekos=randint(0,2)
        l[jatekos]=2
        l_jatekos=l.copy()
        for j in range(0,3):
            if l.count(0)==1:
                for k in range(0,3):
                    if l[k]==0:
                        musorvezeto=k
                        
                    else:
                        continue
                        
            else:
                showman=[]
                for k in range(0,3):
                    if l[k]==0:
                        showman.append(k)
                    else:
                        continue
                sh=randint(0,1)
                musorvezeto=showman[sh]
                            
        
        #második döntes
        used_numbers=[]
        used_numbers.append(jatekos)
        used_numbers.append(musorvezeto)
        for j in range(3):
            if j in used_numbers:
                continue
            else:
                dontes2=j
                if dontes2==nyeremeny2:
                    suc2+=1
                    break
    #print(used_numbers,nyeremeny2,jatekos,musorvezeto,dontes2) 
        
            
        
            
    
        #print([nyeremeny2, jatekos,musorvezeto],non_used_number,dontes2,suc2)
        for i in range(z):
            used_numbers=[]
            valasztas2=[]
            dontesi_lehetoseg=[]
            nyeremeny=randint(0,2)
            jatekos=randint(0,2)
            used_numbers.append(nyeremeny)
            used_numbers.append(jatekos)
            if nyeremeny==jatekos:
                musorvezeto_values=[]
                for k in range(3):
                    if k not in used_numbers:
                        musorvezeto_values.append(k)
                    else:
                        continue
                sh=randint(0,1)
                musorvezeto=musorvezeto_values[sh]
            else:
                for k in range(3):
                    if k not in used_numbers:
                        musorvezeto=k
                    else:
                        continue
            #3. stratégia:
            valasztas2.append(musorvezeto)
            valasztas2.append(jatekos)
            for j in range(3):
                if j not in valasztas2:
                    dontesi_lehetoseg.append(j)
                    dontesi_lehetoseg.append(jatekos)
                    sh=randint(0,1)
                    dontes2=dontesi_lehetoseg[sh]
                    if dontes2==nyeremeny:
                        suc3+=1
                    else:
                        suc3=suc3
                else:
                    continue
            
    print(f"{'Marad a kiválsztott ajtó:'} {suc1/x:.3f}")
    print(f"{'Másik ajtót választ:'}      {suc2/y:.3f}")
    print(f"{'Mindegy:'}                  {suc3/1000000:.3f}")
    
monty_func(1000,1000,1000)
if __name__=="__monty_func__":
    monty_func(1000,1000,1000)

                
                
            
            
                    
                
                    
                    
                    
                    
