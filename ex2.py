nr=25
bitNumber = 3
nr = nr | (1 << bitNumber)
print(nr)
bitNumber = 2
nr = nr | (1 << bitNumber)
print(nr)

Cum vom scrie un program care să seteze un anumit bit False?
de ex, numărul 25 se scrie în binar 000...0011001
dacă se cere setarea bitului 3, atunci numărul devine (10001) 17 
dacă se cere setarea bitului 2, atunci numărul devine (rămâne tot) 25