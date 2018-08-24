#define the gen_primes function here
def is_prime(n):
	for i in range(2,n):
		if n % i == 0:
			return False
		return True
def genPrimes():
    num = 2
    while True:
    	if is_prime(num):
    		yield num
    	num += 1

def main():
	data=input()
	l=data.split()
	a=int(l[0])
	b=int(l[1])
	primeGenerator = genPrimes()
	for i in range(a):
	    p=primeGenerator.__next__()
	    if(i%b==0):
	        print(p)
	
if __name__== "__main__":
	main()