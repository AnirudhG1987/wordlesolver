def isValid( s: str) -> bool:
    l = []

    for c in s:
        if c == '(' or c == '{' or c == '[':
            l.append(c)
        else:
            if l[-1] == c:
                l.pop(-1)
            else:
                return False
        print(l)
    if len(l) == 0:
        return True
    else:
        return False

def longestValidParentheses( s: str) -> int:

    max_global =0
    l = []

    for i,c in enumerate(s):
        if c == '(':
            l.append(c)
        else:
            if len(l)==0:
                l.append(c)
                continue
            if l[-1]=='(':
                l.pop(-1)
                l.append(2)
            elif l[-1]==')':
                l.append(c)
            else:
                flag = True
                for j in range(len(l)-2,-1,-1):
                    if l[j]=='(':
                        l[j]=2
                        flag = False
                        break
                if flag:
                    print("this is c",c)
                    l.append(c)
    print(l,i,c)
    max_local = 0
    for i in l:

        if i == '(' or i == ')' and max_local != 0:
            if max_local > max_global:
                max_global = max_local
            max_local = 0
        elif i == 2:
            max_local += 2
        print(i, max_global, max_local)

    return max(max_global,max_local)

def removingstuff(n):
    arr = (range(1, n + 1))
    index = 0
    l=n
    while l > 1:

        if index % 2 == 0:
            arr = (x for i, x in enumerate(arr) if i % 2 == 1)


        else:
            if l % 2 == 0:
                arr = (x for i, x in enumerate(arr) if i % 2 == 0)


            else:
                arr = (x for i, x in enumerate(arr) if i % 2 == 1)

        l_arr = list(arr)
        print(l_arr)
        l=len(l_arr)
        arr=iter(l_arr)
        index += 1
        #print(index)



    return next(arr)

from math import factorial
def getPermutation( n: int, k: int) -> str:
    l = list(range(1, n))
    s = ""
    factorial = factorial(n)
    while n != 0:
        factorial = factorial / n
        index = int(k // factorial)
        print(index)
        s += str(l[index])
        k = k - index * factorial
        n = n - 1
        print(s)
    return s

def permulationslist(nums):
    l = len(nums)
    output = [[nums[0]]]
    if l == 1:
        return output
    else:

        for i in range(1, l):
            output = [row[:] for row in output for k in range((i+1))]

            #print(output,output[0],nums[i])
            for j in range(len(output)):
                item = [x for x in output[j]]
                item.insert(j % (i + 1), nums[i])
                print(item,output)
                if item not in output:
                    output[j].insert(j % (i + 1), nums[i])
                else:
                    output.pop(j)
        print(output)
    return output

def nextPermulation(nums):
    l=len(nums)
    if l==1:
        return nums
    a=l-1
    b=l-2
    while b>=0 :
        #print(a,b)
        if nums[a]>nums[b]:
            print(a,b)
            temp = nums[a]
            nums[a]=nums[b]
            nums[b]=temp

            for i in range(b+1,l - 1):
                min_index = i
                for j in range(i + 1, l):
                    if (nums[j] < nums[min_index]):
                        min_index = j
                temp = nums[i]
                nums[i] = nums[min_index]
                nums[min_index] = temp
            print("hi",nums)
            break

        else:
            if a-b==1:
                b-=1
                a=l-1
            else:
                a-=1
    if b<0:
        return sorted(nums)
    return nums

def combinations_creator(n,k):

    output=[[]]
    for i in range(1, min(k + 1,n-k+1)):
        if i!=1:
            output = [x + [j] for k, x in enumerate(output) for j in range(max(x)+1, n + 1) if j not in x]
        else:
            output = [x + [j] for k, x in enumerate(output) for j in range(i , n + 1) if j not in x]
        print(output)

    if k>=(n+1)//2:
        return ([[y for y in range(1, n + 1) if y not in x]  for x in output])
    return output

#print(combinations_creator(10,3))

def permutations_creator(nums):

    output=[[]]
    dict_nums = {x:nums.count(x) for x in set(nums)}
    print(dict_nums)
    for i in range(len(nums)):
        output = [x + [j] for x in output for j in dict_nums.keys() if dict_nums[j] > x.count(j)]
        print(output)

    #if k>=(n+1)//2:
    #    return ([[y for y in range(1, n + 1) if y not in x]  for x in output])
    return output

def permutations_square_creator(nums):
    def issquare(x):
        val=(x)**0.5
        return int(val)==val
    output=[[]]
    dict_nums = {x: nums.count(x) for x in set(nums)}
    output=[x+[j] for x in output for j in dict_nums.keys() ]
    print(output)
    print(dict_nums)
    for i in range(len(nums)-1):
        output = [x + [j] for x in output for j in dict_nums.keys() if dict_nums[j] > x.count(j) and issquare(x[-1]+j)]
        print(output)

    #if k>=(n+1)//2:
    #    return ([[y for y in range(1, n + 1) if y not in x]  for x in output])
    return output

def isPalindrome(n):
    str_n = str(n)
    l=len(str_n)
    return str_n[:l//2]==str_n[:(l-1)//2:-1]

def largestPalindrome(n):
    flag = False
    lst=[]
    max = 10**n
    b=a= 1
    while a!=9 or b!=9:
        lst.append(((max-a)*(max-b),max-a,max-b))
        a-=1
        b-=1
        if b==0:
            pass



    return sorted(lst,reverse=True)

def combinationSum(nums,target):
    nums = sorted([x for x in nums if x<=target],reverse=True)
    output = []
    if len(nums)==0  or sum(nums)<target:
        return output
    if sum(nums)==target:
        if len(nums)>3:
            return output
        return [nums]

    for i,c in enumerate(nums):
        if target-c==0:
            output.append([c])
            continue
        temp_nums = [x for x in nums[i:] if x<=c ]
        item = combinationSum(temp_nums,target-c)
        print("tthis is item",item)
        print("tthis is output", output)
        if len(item)!=0 and len(output)<=3:
            for d in item:
                temp = d+[c]
                if temp not in output:
                    output += [temp]
    return output

#print(combinationSum([0,1,2,3,4,5], 8))
#print(combinationSum([1,1,2,2,2,2],5))

#print(combinationSum([1,1,2,2,2,2], 5))

def combinationSum2(nums,target):
    def helper_func(nums,target):
        nums = sorted([x for x in nums if x<=target],reverse=True)
        #print(nums,"after sorting")
        output = []
        if len(nums)==0:
            return output

        for i,c in enumerate(nums):
            if target==c:
                output.append([c])
                continue
            temp_nums = [x for x in nums if x<=c ]
            #print(temp_nums,c,target-c)
            item = helper_func(temp_nums,target-c)
            if len(item)!=0:
                for d in item:
                    temp = d+[c]
                    if temp not in output:
                        output += [temp]

        return output
    output = helper_func(nums,target)
    counter =0
    for item in output:
        l=len(item)
        dict_item = [item.count(x) for x in set(item)]
        temp=factorial(l)
        for val in dict_item:
            temp = temp//factorial(val)
        counter+=temp
    return counter

#print(combinationSum2([1,1,2,2,3,3,4,4,5,5], 8))

#print(unique_stuff([10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,360,370,380,390,400,410,420,430,440,450,460,470,480,490,500,510,520,530,540,550,560,570,580,590,600,610,620,630,640,650,660,670,680,690,700,710,720,730,740,750,760,770,780,790,800,810,820,830,840,850,860,870,880,890,900,910,920,930,940,950,960,970,980,990,111]))


def combinationSum4(nums,target):
    def unique_stuff(l):
        l.sort()
        q = []
        while len(l) != 0:
            q.append(l[0])
            l = [x for x in l if x % l[0] != 0]
        return q
    def helper_func(nums, target):
        output = []
        nums = [x for x in nums if x <= target]
        #print(nums,"after sorting")

        if len(nums) == 0:
            return output
        if len(nums)==1:
            if target%nums[0]!=0:
                return output
        if target%2==1 and all([x%2==0 for x in nums]):
            return output
        if len(unique_stuff(nums))==1:
            if target%nums[0]!=0:
                #print(target,nums[0])
                return output
        #print(nums,"this is nums")
        for i, c in enumerate(nums):
            for j in range(1,target//c+1):
                temp_nums = [x for x in nums if x < c]
                new_target=target - c*j
                if new_target==0:
                    output.append({c:j})
                    #print(output)
                    continue
                item = helper_func(temp_nums, new_target)
                #print(item,"This is item")
                if len(item) != 0:
                    for d in item:
                        d.update({c:j})
                        #print(d,"this is dic")
                        #if temp not in output:
                        output += [d]
            #print(output,c,"this is output",nums,"target",target)
        return output

    nums = sorted([x for x in nums if x <= target],reverse=True)
    output = helper_func(nums, target)
    counter = 0
    for item in output:
        temp = factorial(sum(item.values()))
        for val in item.values():
            temp = temp // factorial(val)
        counter += temp

    return counter
#print(combinationSum4([1,1,2,2,3,3,4,4,5,5], 8))

def combinations_target(k,target):
    n=9
    output=[[]]
    #if k>=(n+1)//2:
    #    target = n*(n+1)/2-target
    #    print(target)

    for i in range(1, k + 1):
        if i!=1 and i<k:
            output = [x + [j] for k, x in enumerate(output) for j in range(max(x)+1, n + 1) if j not in x and sum(x)+j<target]
            #print(output)
        elif i==1:
            output = [x + [j] for k, x in enumerate(output) for j in range(i , n + 1) if j not in x and j<target]
            #print(output)
        else:
            output = [x + [j] for k, x in enumerate(output) for j in range(max(x)+1 , n + 1) if j not in x and sum(x)+j==target]
     #       print(output)


    #print(output)
    #if k>=(n+1)//2:
    #    return ([[y for y in range(1, n + 1) if y not in x]  for x in output])
    return output

def combinationSum41(nums, target: int) -> int:
    def helper(s, d):
        if target == s:
            return 1

        if s > target:
            return 0

        if s in d:
            return d[s]

        c = 0
        for i in range(len(nums)):
            c += helper(nums[i] + s, d)


        d[s] = c
        print(d)
        return c

    return helper(0, {})
from time import time

def checkValid(matrix) -> bool:
    l = len(matrix)
    cols = list(zip(*matrix))
    # reference = list(range(1,l+1))
    for i in range(l):
        print(matrix[i],len(set(matrix[i])))
        print(cols[i],len(set(cols[i])))
        if len(set(matrix[i])) != l:
            return False
        if len(set(matrix[:][i])) != l:
            return False
    return True

def isValidSudoku(board) -> bool:
    col_fil = [[y for y in x if y != '.'] for x in zip(*board)]
    # col_bool = all([len(x)==len(set(x)) for x in col_fil])
    row_fil = [[y for y in x if y != '.'] for x in board]
    # row_bool = all([len(x)==len(set(x)) for x in row_fil])
    box_fil = [sum([[x for x in board[3 * k + i][j * 3:3 * (j + 1)] if x != '.'] for i in range(3)], []) for j in
               range(3) for k in range(3)]
    box_bool = all([len(col_fil[i]) == len(set(col_fil[i])) and len(row_fil[i]) == len(set(row_fil[i])) and len(
        box_fil[i]) == len(set(box_fil[i])) for i in range(len(board))])
    return box_bool
        # print(col_bool,row_bool,box_bool)

def countPrimes( n: int) -> int:
    def isPrime(n,primes):
        for p in primes:
            if n%p==0:
                return False
        return True
    sorted()
    if n <= 2:
        return 0
    #no_of_primes = 1
    numbers = list(range(3, n, 2))
    # print(numbers)
    primes = []
    # while len(numbers)>1:
    while numbers[0] < n//2:
        # print([numbers[0]%x==0 for x in primes])
        if isPrime(numbers[0],primes):
            primes.append(numbers[0])
            #print(primes)
            #no_of_primes += 1
            numbers = [x for x in numbers if x % numbers[0] != 0]
            #print(numbers)
            # print(primes)
    return len(primes)+len(numbers)



start = time()
print(countPrimes(499979))
end = time()
print(end-start)
    
