a = []
n = int(input('Enter the number'))
def logic(n):
    i = 0
    while i < n:
        if a[i] < a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
        i += 2
try:
    for _ in range(n):
       a.append(str(input('enter the number')))
    print('before sorting the array is \n',a)
    if n %2 == 0:
        logic(n)
    else:
        logic(n-1)
    print('after being sorted the array is \n',a)
except:
    print('Wrong Input')


'''
outout:

before sorting the array is 
 ['12', '13', '23', '24', '25', '76', '11', '26', '34', '46']
after being sorted the array is 
 ['13', '12', '24', '23', '76', '25', '26', '11', '46', '34']
'''