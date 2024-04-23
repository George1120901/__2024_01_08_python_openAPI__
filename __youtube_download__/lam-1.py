#匿名函數lambda


print('++++++++++++++++++++++++++')
#lam-1.py
#傳統函數 
def f(x, y, z):
	return x + y + z 
print("傳統函數處理") 
print(f(20, 30, 50)) 

#匿名函數
f = lambda x, y, z: x + y + z 
print("匿名函數處理") 
print(f(20, 30, 50))

print('++++++++++++++++++++++++++')
#lam-2.py
#匿名函數當作參數傳入 - 1
print("匿名函數當作參數傳入-1")
mz = (lambda a , b  , c  : a + b + c) 
print(mz('Wolfgang', ' Amadeus',' Mozart')) 

#lam-2.py

#匿名函數當作參數傳入-2
print("匿名函數當作參數傳入-2")
mz = (lambda a = 'Wolfgangus', b = ' Theophilus', c = ' Mozart': a + b + c) 
print(mz('Wolf', ' Amadeus')) 