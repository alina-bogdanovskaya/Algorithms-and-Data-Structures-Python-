from collections import defaultdict

e_dict = defaultdict(int)
n = int(input('Please enter number of enterprises: '))

for i in range(n):
  a = input('Enter enterprise name: ')
  for j in range(4):
    b = int(input('Enter enterprise profit by quarter: '))
    e_dict[a] += b

print(e_dict)

avg = sum(e_dict.values())/n

above_avg = []
below_avg = []

for k, v in e_dict.items():
  if v > avg:
    above_avg.append(k)
  else:
    below_avg.append(k)

print(f'Average profit per year: {avg: .2f}; \nProfit above the average: {above_avg}; \nProfit below the average: {below_avg}')
