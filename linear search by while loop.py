#python code to linearly search for a number and return it's index using a while loop

pos = 0
def search(list, n):

    i = 0
    while i < len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i += 1
    return False


list = [4, 6, 3, 5, 2, 9]
n = 5

if search(list,n):
    print('found at index ', pos)
else:
    print('not found')
