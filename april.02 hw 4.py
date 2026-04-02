a= 132  #Ob10000100
b=45  #Ob00101101
fmt0='{:<10}'
fmt1='Ob{:08b} 0x{:02x} {:3}'
n=30

print("bitwise AND:")
print(fmt0.format('a'),fmt1.format(a,a,a))
print(fmt0.format('b'),fmt1.format(b,b,b))
print('-'*n)
print(fmt0.format('a&b'),fmt1.format(a&b,a&b,a&b))
