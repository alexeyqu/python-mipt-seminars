import time

N = 10000000

# I intentionally wrote really simple code :)

a = time.time()
my_list = []
for x in range(N):
    my_list.append(x ** 2)
b = time.time()
print('append version: {}'.format(b - a))

a = time.time()
my_list = [0] * N
for x in range(N):
    my_list[x] = x ** 2
b = time.time()
print('no extra allocations: {}'.format(b - a))

a = time.time()
x = [x ** 2 for x in range(N)]
b = time.time()
print('list comprehension: {}'.format(b - a))

