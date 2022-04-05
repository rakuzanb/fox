#Rakuzanb
from random import randint  
ar = [] 
ar2 = [] 
ar3 = [] 
for i in range (12): 
    ar.append ([]) 
    ar2.append ([]) 
    ar3.append ([]) 
    for j in range (12): 
        ar[i].append  (0) 
        ar2[i].append (0) 
        ar3[i].append (0) 
        if (randint(1,20) == 1) and ar[i][j] == 0: 
            ar[i][j] = 1 
        if (randint(1,7) == 1) and ar[i][j] == 0: 
            ar[i][j] = 2 
        if (randint(1,5) == 1) and ar[i][j] == 0: 
            ar[i][j] = 3 
   
for i in range (12): 
    ar[0][i] = -1 
    ar[11][i] = -1 
    ar[i][0] = -1 
    ar[i][11] = -1 
for i in range (1,11): 
    for j in range (1,11): 
        print (ar[i][j] , end = " ") 
    print () 
 
while int (input()) == 1: 
    for i in range (1,11): 
        for j in range (1,11): 
            if ar3[i][j] == 0:                 
                if ar[i][j] == 1:  # fox
                    if ar[i-1][j-1] == 2 and ar3[i-1][j-1] == 0: 
                        ar[i-1][j-1] = 1 
                        ar[i][j] = 0 
                        ar3[i][j] = 1 
                        ar3[i-1][j-1] = 1 
                    elif ar[i-1][j] == 2 and ar3[i-1][j] == 0: 
                        ar[i-1][j] = 1 
                        ar[i][j] = 0 
                        ar3[i][j] = 1 
                        ar3[i-1][j] = 1 
                    elif ar[i-1][j+1] == 2 and ar3[i-1][j+1] == 0: 
                        ar[i-1][j+1] = 1 
                        ar[i][j] = 0 
                        ar3[i][j] = 1 
                        ar3[i-1][j+1] = 1 
                    elif ar[i][j+1] == 2 and ar3[i][j+1] == 0: 
                        ar[i][j+1] = 1 
                        ar[i][j] = 0 
                        ar3[i][j] = 1 
                        ar3[i][j+1] = 1 
                    elif ar[i+1][j+1] == 2 and ar3[i+1][j+1] == 0: 
                        ar[i+1][j+1] = 1 
                        ar[i][j] = 0 
                        ar3[i][j] = 1 
                        ar3[i+1][j+1] = 1 
                    elif ar[i+1][j] == 2 and ar3[i+1][j] == 0: 
                        ar[i+1][j] = 1 
                        ar[i][j] = 0 
                        ar3[i][j] = 1 
                        ar3[i+1][j] = 1 
                    elif ar[i+1][j-1] == 2 and ar3[i+1][j-1] == 0: 
                        ar[i+1][j-1] = 1 
                        ar[i][j] = 0 
                        ar3[i][j] = 1 
                        ar3[i+1][j-1] = 1 
                    elif ar[i][j-1] == 2 and ar3[i][j-1] == 0: 
                        ar[i][j-1] = 1 
                        ar[i][j] = 0 
                        ar3[i][j] = 1 
                        ar3[i][j-1] = 1 
                    elif ar[i-1][j-1] == 1 and ar3[i-1][j-1] == 0: #pop
                        if ar[i-1][j] == 0 and ar3[i-1][j] == 0 : 
                            ar[i-1][j] = 1 
                            ar3[i-1][j-1] = 1 
                            ar3[i-1][j] = 1 
                            ar3[i][j] = 1 
                        elif ar[i][j-1] == 0 and ar3[i][j-1] == 1: 
                            ar[i][j-1] = 1 
                            ar3[i-1][j-1] = 1 
                            ar3[i][j] = 1 
                            ar3[i][j-1] = 1 
                             
                    elif ar[i-1][j] == 1 and ar3[i-1][j] == 0: 
                        if ar[i-1][j-1] == 0 and ar3[i-1][j-1] == 0: 
                            ar[i-1][j-1] = 1 
                            ar3[i-1][j] = 1 
                            ar3[i][j] = 1 
                            ar3[i-1][j-1] = 1 
                        elif ar[i][j-1] == 0 and ar3 [i][j-1] == 0: 
                            ar[i][j-1] = 1 
                            ar3[i][j] = 1 
                            ar3[i][j-1] = 1 
                            ar3[i-1][j] = 1 
                        elif ar[i-1][j+1] == 0 and ar3[i-1][j+1] == 0: 
                            ar[i-1][j+1] = 1 
                            ar3[i][j] = 1 
                            ar3[i-1][j] = 1 
                            ar3[i-1][j+1] = 1
                        elif ar[i][j+1] == 1 and ar3[i][j+1] == 0: 
                            ar[i][j+1] = 1 
                            ar3[i][j+1] = 1 
                            ar3[i][j] = 1 
                            ar3[i][j+1] = 1 
                     
                    elif ar[i-1][j+1] == 1 and ar3[i-1][j+1] == 0: 
                        if ar[i-1][j] == 0 and ar3[i-1][j] == 0: 
                            ar[i-1][j] = 1 
                            ar3[i-1][j] = 1 
                            ar3[i][j] = 1 
                            ar3[i-1][j+1] = 1 
                        elif ar[i][j+1] == 0 and ar3[i][j+1] == 0: 
                            ar[i][j+1] = 1 
                            ar3[i][j+1] = 1 
                            ar3[i][j] = 1 
                            ar[i-1][j+1] = 1 
                    elif ar[i][j+1] == 1 and ar3[i][j+1] == 0: 
                        if ar[i-1][j] == 0 and ar3[i-1][j] == 0: 
                            ar[i-1][j] = 1 
                            ar3[i-1][j] = 1 
                            ar3[i][j] = 1 
                            ar3[i][j+1] = 1 
                        elif ar[i-1][j+1] == 0 and ar3[i-1][j+1] == 0: 
                            ar[i-1][j+1] = 1 
                            ar3[i-1][j+1] = 1 
                            ar3[i][j]= 1 
                            ar3[i][j+1] = 1 
                        elif  ar[i+1][j] == 0 and ar3[i+1][j] == 0:
                            ar[i+1][j] = 1
                            ar3[i+1][j] = 1
                            ar3[i][j] = 1
                            ar3[i][j+1] = 1
                        elif ar[i+1][j+1] == 0 and ar3[i+1][j+1] == 0:
                            ar[i+1][j+1] = 1
                            ar3[i+1][j+1] = 1
                            ar3[i][j] = 1
                            ar3[i][j+1] = 1
                    elif ar[i+1][j+1] == 1 and ar3[i+1][j+1] == 0:
                        if ar[i][j+1] == 0 and ar3[i][j+1] == 0:
                            ar[i][j+1] = 1
                            ar3[i][j+1] = 1
                            ar3[i][j] = 1
                            ar3[i+1][j+1] = 1
                        elif ar[i+1][j] == 0 and ar3 [i+1][j] == 0:
                            ar[i+1][j] = 1
                            ar3[i+1][j] = 1
                            ar3[i][j] = 1
                            ar3[i+1][j+1] = 1
                    elif ar[i+1][j] == 1 and ar3[i+1][j] == 0: 
                        if ar[i][j+1] == 0 and ar3[i][j+1] == 0:
                            ar[i][j+1] = 1
                            ar3[i][j+1] = 1
                            ar3[i][j] = 1
                            ar3[i+1][j] = 1
                        elif ar[i+1][j+1] == 0 and ar3[i+1][j+1] == 0:
                            ar[i+1][j+1] = 1
                            ar3[i+1][j+1] = 1
                            ar3[i][j] = 1
                            ar3[i+1][j] = 1
                        elif ar[i][j-1] == 0 and ar3[i][j-1] == 0:
                            ar[i][j-1] = 1
                            ar3[i][j-1] = 1
                            ar[i][j] = 1
                            ar[i+1][j] = 1
                        elif ar[i+1][j-1] == 0 and ar3[i+1][j-1] == 0:
                            ar[i+1][j-1] = 1
                            ar3[i+1][j-1] = 1
                            ar3[i][j] = 1
                            ar3[i+1][j] = 1
                    elif ar[i+1][j-1] == 1 and ar3[i+1][j-1] == 0: 
                        if ar[i][j-1] == 0 and ar3[i][j-1] == 0:
                            ar[i][j-1] = 1
                            ar3[i][j-1] = 1
                            ar3[i][j] = 1
                            ar3[i+1][j-1] = 1
                        elif ar[i+1][j] == 0 and ar3[i+1][j] == 0:
                            ar [i+1][j] = 1
                            ar3[i+1][j] = 1
                            ar3[i][j] = 1
                            ar3[i+1][j-1] = 1
                    elif ar[i][j-1] == 1 and ar3[i][j-1] == 0:
                        if ar[i-1][j] == 0 and ar3[i-1][j] == 0: 
                            ar[i-1][j] = 1 
                            ar3[i-1][j] = 1 
                            ar3[i][j] = 1 
                            ar3[i][j+1] = 1 
                        elif ar[i-1][j-1] == 0 and ar3[i-1][j-1] == 0: 
                            ar[i-1][j-1] = 1 
                            ar3[i-1][j-1] = 1 
                            ar3[i][j]= 1 
                            ar3[i][j-1] = 1 
                        elif  ar[i+1][j] == 0 and ar3[i+1][j] == 0:
                            ar[i+1][j] = 1
                            ar3[i+1][j] = 1
                            ar3[i][j] = 1
                            ar3[i][j+1] = 1
                        elif ar[i+1][j-1] == 0 and ar3[i+1][j-1] == 0:
                            ar[i+1][j-1] = 1
                            ar3[i+1][j-1] = 1
                            ar3[i][j] = 1
                            ar3[i][j-1] = 1
                
            
    #df
    for i in range (1,11): 
        for j in range (1,11): 
            if ar3[i][j] == 0:                 
                
                if ar[i][j] == 2: #rab
                    if ar[i-1][j-1] == 3 and ar3[i-1][j-1] == 0: 
                        ar[i-1][j-1] = 2 
                        ar[i][j] = 0 
                        ar3[i][j] = 1 
                        ar3[i-1][j-1] = 1 
                    elif ar[i-1][j] == 3 and ar3[i-1][j] == 0: 
                        ar[i-1][j] = 2 
                        ar[i][j] = 0 
                        ar3[i][j] = 1 
                        ar3[i-1][j] = 1 
                    elif ar[i-1][j+1] == 3 and ar3[i-1][j+1] == 0: 
                        ar[i-1][j+1] = 2 
                        ar[i][j] = 0 
                        ar3[i][j] = 1 
                        ar3[i-1][j+1] = 1 
                    elif ar[i][j+1] == 3 and ar3[i][j+1] == 0: 
                        ar[i][j+1] = 2 
                        ar[i][j] = 0 
                        ar3[i][j] = 1 
                        ar3[i][j+1] = 1 
                    elif ar[i+1][j+1] == 3 and ar3[i+1][j+1] == 0: 
                        ar[i+1][j+1] = 2 
                        ar[i][j] = 0 
                        ar3[i][j] = 1 
                        ar3[i+1][j+1] = 1 
                    elif ar[i+1][j] == 3 and ar3[i+1][j] == 0: 
                        ar[i+1][j] = 2 
                        ar[i][j] = 0 
                        ar3[i][j] = 1 
                        ar3[i+1][j] = 1 
                    elif ar[i+1][j-1] == 3 and ar3[i+1][j-1] == 0: 
                        ar[i+1][j-1] = 2 
                        ar[i][j] = 0 
                        ar3[i][j] = 1 
                        ar3[i+1][j-1] = 1 
                    elif ar[i][j-1] == 3 and ar3[i][j-1] == 0: 
                        ar[i][j-1] = 2 
                        ar[i][j] = 0 
                        ar3[i][j] = 1 
                        ar3[i][j-1] = 1 
                    elif ar[i-1][j-1] == 2 and ar3[i-1][j-1] == 0: #pop
                        if ar[i-1][j] == 0 and ar3[i-1][j] == 0 : 
                            ar[i-1][j] = 2 
                            ar3[i-1][j-1] = 1 
                            ar3[i-1][j] = 1 
                            ar3[i][j] = 1 
                        elif ar[i][j-1] == 0 and ar3[i][j-1] == 1: 
                            ar[i][j-1] = 2 
                            ar3[i-1][j-1] = 1 
                            ar3[i][j] = 1 
                            ar3[i][j-1] = 1 
                             
                    elif ar[i-1][j] == 2 and ar3[i-1][j] == 0: 
                        if ar[i-1][j-1] == 0 and ar3[i-1][j-1] == 0: 
                            ar[i-1][j-1] = 2 
                            ar3[i-1][j] = 1 
                            ar3[i][j] = 1 
                            ar3[i-1][j-1] = 1 
                        elif ar[i][j-1] == 0 and ar3 [i][j-1] == 0: 
                            ar[i][j-1] = 2 
                            ar3[i][j] = 1 
                            ar3[i][j-1] = 1
                            ar3[i-1][j] = 1 
                        elif ar[i-1][j+1] == 0 and ar3[i-1][j+1] == 0: 
                            ar[i-1][j+1] = 2 
                            ar3[i][j] = 1 
                            ar3[i-1][j] = 1 
                            ar3[i-1][j+1] = 1 
                        elif ar[i][j+1] == 1 and ar3[i][j+1] == 0: 
                            ar[i][j+1] = 2 
                            ar3[i][j+1] = 1 
                            ar3[i][j] = 1 
                            ar3[i][j+1] = 1 
                     
                    elif ar[i-1][j+1] == 2 and ar3[i-1][j+1] == 0: 
                        if ar[i-1][j] == 0 and ar3[i-1][j] == 0: 
                            ar[i-1][j] = 2 
                            ar3[i-1][j] = 1 
                            ar3[i][j] = 1 
                            ar3[i-1][j+1] = 1 
                        elif ar[i][j+1] == 0 and ar3[i][j+1] == 0: 
                            ar[i][j+1] = 2 
                            ar3[i][j+1] = 1 
                            ar3[i][j] = 1 
                            ar[i-1][j+1] = 1 
                    elif ar[i][j+1] == 2 and ar3[i][j+1] == 0: 
                        if ar[i-1][j] == 0 and ar3[i-1][j] == 0: 
                            ar[i-1][j] = 2 
                            ar3[i-1][j] = 1 
                            ar3[i][j] = 1 
                            ar3[i][j+1] = 1 
                        elif ar[i-1][j+1] == 0 and ar3[i-1][j+1] == 0: 
                            ar[i-1][j+1] = 2 
                            ar3[i-1][j+1] = 1 
                            ar3[i][j]= 1 
                            ar3[i][j+1] = 1 
                        elif  ar[i+1][j] == 0 and ar3[i+1][j] == 0:
                            ar[i+1][j] = 2
                            ar3[i+1][j] = 1
                            ar3[i][j] = 1
                            ar3[i][j+1] = 1
                        elif ar[i+1][j+1] == 0 and ar3[i+1][j+1] == 0:
                            ar[i+1][j+1] = 2
                            ar3[i+1][j+1] = 1
                            ar3[i][j] = 1
                            ar3[i][j+1] = 1
                    elif ar[i+1][j+1] == 2 and ar3[i+1][j+1] == 0:
                        if ar[i][j+1] == 0 and ar3[i][j+1] == 0:
                            ar[i][j+1] = 2
                            ar3[i][j+1] = 1
                            ar3[i][j] = 1
                            ar3[i+1][j+1] = 1
                        elif ar[i+1][j] == 0 and ar3 [i+1][j] == 0:
                            ar[i+1][j] = 2
                            ar3[i+1][j] = 1
                            ar3[i][j] = 1
                            ar3[i+1][j+1] = 1
                    elif ar[i+1][j] == 2 and ar3[i+1][j] == 0: 
                        if ar[i][j+1] == 0 and ar3[i][j+1] == 0:
                            ar[i][j+1] = 2
                            ar3[i][j+1] = 1
                            ar3[i][j] = 1
                            ar3[i+1][j] = 1
                        elif ar[i+1][j+1] == 0 and ar3[i+1][j+1] == 0:
                            ar[i+1][j+1] = 2
                            ar3[i+1][j+1] = 1
                            ar3[i][j] = 1
                            ar3[i+1][j] = 1
                        elif ar[i][j-1] == 0 and ar3[i][j-1] == 0:
                            ar[i][j-1] = 2
                            ar3[i][j-1] = 1
                            ar3[i][j] = 1
                            ar3[i+1][j] = 1
                        elif ar[i+1][j-1] == 0 and ar3[i+1][j-1] == 0:
                            ar[i+1][j-1] = 2
                            ar3[i+1][j-1] = 1
                            ar3[i][j] = 1
                            ar3[i+1][j] = 1
                    elif ar[i+1][j-1] == 2 and ar3[i+1][j-1] == 0: 
                        if ar[i][j-1] == 0 and ar3[i][j-1] == 0:
                            ar[i][j-1] = 2
                            ar3[i][j-1] = 1
                            ar3[i][j] = 1
                            ar3[i+1][j-1] = 1
                        elif ar[i+1][j] == 0 and ar3[i+1][j] == 0:
                            ar [i+1][j] = 2
                            ar3[i+1][j] = 1
                            ar3[i][j] = 1
                            ar3[i+1][j-1] = 1
                    elif ar[i][j-1] == 2 and ar3[i][j-1] == 0: 
                        if ar[i-1][j] == 0 and ar3[i-1][j] == 0: 
                            ar[i-1][j] = 2 
                            ar3[i-1][j] = 1 
                            ar3[i][j] = 1 
                            ar3[i][j+1] = 1 
                        elif ar[i-1][j-1] == 0 and ar3[i-1][j-1] == 0: 
                            ar[i-1][j-1] = 2 
                            ar3[i-1][j-1] = 1 
                            ar3[i][j]= 1 
                            ar3[i][j-1] = 1 
                        elif  ar[i+1][j] == 0 and ar3[i+1][j] == 0:
                            ar[i+1][j] = 2
                            ar3[i+1][j] = 1
                            ar3[i][j] = 1
                            ar3[i][j+1] = 1
                        elif ar[i+1][j-1] == 0 and ar3[i+1][j-1] == 0:
                            ar[i+1][j-1] = 2
                            ar3[i+1][j-1] = 1
                            ar3[i][j] = 1
                            ar3[i][j-1] = 1
    for i in range (1 , 11):
        for j in range (1 ,11):
            print (ar[i][j] , end = " ")
            ar3[i][j] = 0
            if ar[i][j] == 0:
                if (randint(1,5) == 1): 
                    ar[i][j] = 3 
        print ("")
    print ()
    print ()
