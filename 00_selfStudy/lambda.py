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

print('+++++++++++++++++++++++++++')
try1 = [lambda x: x ** 2, lambda x: x ** 3,lambda x: x ** 4] 
print(try1.__class__) 
for f in try1:
	print(f.__class__)
	print(f(3))
 
 #try1[0] 是try 此list第一個位址值 lambda x: x ** 2
print(try1[0](10))

print('+++++++++++++++++++++++++++')
#lam-3a.py 
#<class 'function'>

print("一般函數處理") 
def f1(x):
	return x ** 2 

def f2(x):
	return x ** 3 

def f3(x):
	return x ** 4 

try2 = [f1, f2, f3] 

for ff in try2:
	print(ff.__class__)
	print(ff(3)) 

print(try2[0](3))


print('+++++++++++++++++++++++++++')
