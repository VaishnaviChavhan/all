N=1234567
d1=(N//1000000)%10
d2=(N//100000)%10
d3=(N//10000)%10
d4=(N//1000)%10
d5=(N//100)%10
d6=(N//10)%10
d7=N%10

M=(d1*1000000+d2*100000+d3*10000+d4*1000+d7*100+d6*10+d5)
print(M)
