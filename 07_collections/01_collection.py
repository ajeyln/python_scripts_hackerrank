''' Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay xi amount of money only if they get the shoe of their desired size.
Your task is to compute how much money Raghu earned.'''

# input method
''' The first line contains X, the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains N, the number of customers.
The next N lines contain the space separated values of the shoe size desired by the customer and xi, the price of the shoe.'''

import collections

x = int(input("Enter the number of shoes: "))
shoes = collections.Counter(map(int,input("Enter the shoe sizes: ").split()))
n = int(input("Enter the number of shoes required:"))

income = 0
print("Enter the size and price of the shoes")
for i in range(n):
    size, price = map(int, input().split())
    if shoes[size]: 
        income += price
        shoes[size] -= 1

print(f'The ammount need to pay is {income}')