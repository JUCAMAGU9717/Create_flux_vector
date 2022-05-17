#Reaccion de ejemplo
RXN="2 A1 + A2 + 1.5 B1 <==> A3 + 0.5 A4 + B2"
#Metabolitos de ejemplo
MET=['A1','A2','A3','A4','A5','B1','B2', 'B3']

def Create_flux_vector(RXN, MET):
    import numpy as np
    RXN=RXN.split()
    init=[]
    non=[]
    for i in range(1,len(RXN)):
        for j in range(len(MET)):
            if RXN[i]==MET[j]:
                init.append(RXN[i-1])
                non.append(RXN[i])

    for i in range(len(init)):
        if init[i]=='-->' or init[i]=='<==>':
            for j in range(0,i):
                if init[j]=='+':
                    init[j]=-1
                else:
                    init[j]=str(-float(init[j]))

    for i in range(len(init)):
        if init[i]=='+' or init[i]=='-->' or init[i]=='<==>':
            init[i]='1'

    p=[]
    for i in range(len(MET)):
        if MET[i] not in non:
            p.append(i-1)

    [init.append(0) for i in range(len(p))]
    init=[float(init[i]) for i in range(len(init))]
    init=np.array(init)
    flux_vect=np.matrix(init).T

    return flux_vect
