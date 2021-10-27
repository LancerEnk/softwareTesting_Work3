# Task 2: wrong_5_010
def fun(input):  
    n, m, a=map(int, input.split(" "))     
    surRect = n*m
    surFt = a*a
    needed = (surRect//surFt)     
    if surRect%surFt != 0:
        needed += surFt / (surRect%surFt*needed)
    return(needed)
