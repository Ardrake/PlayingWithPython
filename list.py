a = int(25)
b = float(3.147)
c = 'love'
d = 500

lst=[a,b,c,d]
print('Initial List',lst,'\n\n')

lst.append('another value')

print('Here is the appended list',lst,'\n')

lst.insert(1,int(76))

print('Here is the list after inserting integer 76 at 1 position',lst,'\n')

print('This is l.index() function \nIndexing the position of "love" in the list\
 \nThe position is', lst.index('love'))

print('\nRemving a value from the list\n')
e = int(input('Please enter only an Integer to delete form the list: '))
lst.remove(e)

print('\nHere is the list with removed value of ',e,lst)

