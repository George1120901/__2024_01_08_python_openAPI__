#匿名函數lambda

#傳統函數 
def f(x, y, z):
	return x + y + z 
print("傳統函數處理") 
print(f(20, 30, 50)) 

#匿名函數
f = lambda x, y, z: x + y + z 
print("匿名函數處理") 
print(f(20, 30, 50))