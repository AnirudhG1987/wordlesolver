def uglynumber(n):
    if n<7:
        return n
    ugly_numbers = [2,3,5]
    index=0
    while(len(ugly_numbers)<20):
        for i in range(index+1):
            while True:
                ugly_numbers.append(ugly_numbers[index]*ugly_numbers[i])
        index+=1
    return ugly_numbers


#print(uglynumber(10))

def isPrime(n, primes):
    if n==1 or n==2:
        return True
    for p in primes:
        if n % p == 0:
            return False
    return True


def count_primes(n):

    
    if n <= 2:
        return 0
    no_of_primes = 1
    numbers = list(range(2, n, 1))
    primes = []
    index=0
    while index<(int(n**0.5)+1):
        num=numbers[index]
        index += 1
        if num==0:
            continue
        if isPrime(num, primes):
            #primes.append(num)
            # print(primes)
            no_of_primes += 1
            #print(num)
            #print(numbers)
            numbers[num*num-2:n:num] = [0]*(n//num-num+1)
    print(numbers)
    return n-2-numbers.count(0)

def numSquares(n: int) -> int:
    def helpernumSquares(n,p):

        dict_smallest ={}
        for i in range(p,0,-1):
            num=i**2
            if n%num==0:
                return {n:n//num}
            for j in range(n//num,0,-1):
                q = n-j*num
                dict_smallest.update(helpernumSquares(q,min(i-1,int(q**0.5))))
                dict_smallest[n]=j+dict_smallest[q]
                print(dict_smallest,n,i,q)
        return dict_smallest
    sq = int(n**0.5)
    d = helpernumSquares(n, sq)
    print(d)
    return d[n]

print(numSquares(13))
#print(count_primes(11))

#print(count_primes(2000))
#print(count_primes(200))