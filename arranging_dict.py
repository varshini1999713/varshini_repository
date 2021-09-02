num = int(input())
res = {}
print('{',end = '')
for i in range(0, num+1):
    if i==num:
        print('{0}:{1}'.format(i, i*i), end='')
    else:
        print('{0}:{1}, '.format(i, i * i), end='')

print('}')

