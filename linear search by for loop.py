#python code to linearly search a number and return it's index using a for loop
pos = 0
def search(list, n):

    j = 0
    for j in range(len(list)):
        
        for i in list:
            if i == n:
                globals()['pos'] = j
                return True
            j += 1
        return False


list = [4, 6, 3, 5, 2, 9]
n = 9

if search(list,n):
    print('found at index ', pos)
else:
    print('not found')
