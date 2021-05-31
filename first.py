# my first python file
number = 5
print(type(number))
number = "hello world"
print(type(number))


names = ['john', 'jacob', 'anabel', 'jonathan', 'jack', 'tabita', 'winifred', 
'jalang']
# return true for name begins with "j" else return false
for j in names:
    if j[0] == 'j':
        print('its {} that {} begins with a "j"'.format(True,j))
    else:
        print('its {} that {} did not begin with a "j"'.format(False, j))  
 # finding the lenght of all name in a list        
for x in names:
    print(x)
    print(len(x))
# loop and displace the longest strings in a list         

longest_name = max(names, key=len)
print('{} is the longest  string'.format(longest_name,x)) 
#sorting names in a list
names.sort()
print('sorted list:', names)
#displaying each name with its index(position)   
for y in names:
    print(y)
    p = names.index(y)
    print(p)
# returning whether the length are even or old number    
for a in names:
    if len(a)%2== 0:
        print(a)
    else:
        print('a is old') 
           

