'''You are given two numbers a and b. Find the HCF and LCM of these two numbers and print them 
in a new line.
Note: Please see the below links for help,
• HCF
• LCM
Input:
• First-line will contain two space separated integers, a and b respectively 
Output:
Print the HCF and LCM in a new line separated by space.
Constraints
• 1≤a,b≤106
•
Sample Input 1:
2 3
Sample Output 1:
1 6
Sample Input 2:
4 8
Sample Output 2:
4 8
EXPLANATION:
• In the first example, HCF(2, 3) = 1, LCM(2, 3) = 6. 
• In the second example, HCF(4, 8) = 4, LCM(4, 8) = 8.'''
a , b = map(int,input().split())
i = 2
j = 1
while i<=min(a,b):
	if (a%i == 0 ) and (b%i == 0):
		j = i
		i+=1
	else:
		i+=1
print(j , (a*b)//j)
	