#Name:Dan-Ha Le
#Last edit:
# - Jul 5

#Modules:
import threading

#Helper functions:

#Chunks a list into n sublists, returns list of sublist
def chunk(lst, n):
    sublists = []
    length = len(lst)//n
    for i in range(0, len(lst), len(lst)//n):
        sublists.append[i, i+length]
    return sublists

#Calculates the n-th fibonacci number, returns the number
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

#Problem 1: Sum of all multiples of 3 or 5 below 1000:
#Does that mean we are not counting multiples of 3 AND 5?
def problem1 (n):
    sum = 0
    for i in range (1, n):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

#Problem 2: Find the sum of even valued terms
def problem2 (n): 
    results =0
    sum = 1
    prev = 0

    while sum < n:
        if sum%2==0:
            results+= sum
        sum, prev = sum+prev, sum
        
    return results
    
#Problem 3:
#Find the largest prime factor of a number
def problem3(n):
    results = [1]
    Prime = [2]
    while True:
        start = 0
        #The program checks if the number has finished being divided:
        if n == 1:
            break
        else: 
            found = False
            for i in range(start, len(Prime)):
                if n % Prime[i] == 0:
                    found = True
                    print(Prime[i])
                    results.append(Prime[i])
                    n = n/Prime[i]
            #If we went through all the found primes and nothing showed up, add new prime
            if not found:
                start = len(Prime)-1
                adder = Prime[start]
                while True:
                    adder += 1
                    for i in range(1, adder):
                        if adder%i==0:
                            next
                    break
                Prime.append(adder)
    return sorted(results, reverse=True)[0]

            

def main ():
    #print("Problem 1: Sum of multiples of 3 or 5 below 1000 is", problem1(1000))
    #print("Problem 2: Sum of even valued fibonacci number under 4 000 000", problem2(4000000))
    print ("Problem 3: Highest prime factor of a number:", problem3(600851475143))

    


if __name__ == "__main__":
    main()