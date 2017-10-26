def return_zero():
    return 0
def double(x):
    return 2*x

#Hand in 2
def triple(x):
    return 3*x

def if1(x):
    if x==0:
        return 'zero'
    if x>0:
        return 'positive'
    if x<0:
        return 'negative'

    #hand in 3
def if2(x):
    if x==0:
        return 'zero'
    elif x>0:
        return 'positive'
    elif x<0:
        return 'negative'

def loop1(x):
    result = 0
    for n in range(1,x+1):
        result = result + 1
    return(result)
        

#Hand In 4
def loop_sum(x):
    result = 0
    for n in range(1,x+1):
        result = result + n
    return(result)

#Hand in 5.

def myjoin(l,sep):
    rstring = ""
    
    for i in l[0:len(l)-1]:
        rstring = rstring + i + sep
    rstring = rstring + l[len(l)-1]
    return rstring
