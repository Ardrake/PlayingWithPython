str1 = 'this is a sample string.'
print('original string>>', str1,'\n\n')

print('atfer usig capitalising>>',str1.capitalize())

#this prints two instances of 'is' because is in this as well
print('using count method for "is" in the given string>>', str1.count('is'))

print('\n\n')

print('looking fo specfic string literal with spaces>>', str1.count(' is '),'\n')

print('using find method for "amp" in the string>>', str1.find('amp'),'\n')

print('checkin if sring.isupper()>>',str1.isupper(),'\n')

print(bin(255)) #prints in binary

stru = str1.upper()

print('making string upper case>>',stru,'\n\n')
print('now testing new string.isupper()>>', stru.isupper(),'\n\n')

print(str1.upper().isupper())

print('lower string "',stru.lower(),'"')

print('\n\nTitle method', str1.title())

##working with spaces in the string

str2 = '     five taps of the SPACEBAR     '

print('\n\n',str2)

print('using s.lstrip() to remove all the whitespaces from the left\n\
', str2.lstrip(),'\n')

print('now on the right\n', str2.rstrip(),'next letter \n')

print('this is about removing whitespaces from both sides\n',str2.strip())

# replacing text in a string

print(str1.replace('sample', 'testing')) #replaces the first instance in the string

#splitting string into a list

str3 = str1.split(' ')
print(str3)

#joining it back together
str4 = ' '.join(str3) #because lists don't have join() method quoted string is necessary

print(str4)
##formatting a string
## there are two ways to do that

s = '%s is %d years old' % ('Harry', 29) #old c style still supported by python3
print(s)

t= '{0} is {1} years old and can pass {2} string data'.format('Harry', 29, 'third')
print(t)
