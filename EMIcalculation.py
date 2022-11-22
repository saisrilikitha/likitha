
#calculate EMI
'''
p=10000
t=3
r=10
'''
p=int(input('p:'))
t=int(input('time:'))
r=float(input('rate of interest'))
si=(p*t*r)/100
print('simple interest:',si)
emi=(p+si)*t
print('emi value',emi)
