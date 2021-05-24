'''You are given a number N and check if this number is a prime pr not. If this 
number is prime the print 1, otherwise print 0
.
Input:
• First-line will contain the number N
• . 
Output:
Print the answer in the new line.
Constraints
• 1≤N≤109
•
Sample Input 1:
6
Sample Output 1:
0
Sample Input 2:
5
Sample Output 2:
1
EXPLANATION:
• In the first example, 6 is not a prime. 
• In the second example, 5 is a prime.'''
n = int(input())
i = 2
while i*i<= n:
	if n%i !=0:
		i+=1
	else:
		print(0)
		exit()
print(1)
	
