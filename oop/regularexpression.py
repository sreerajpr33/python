a='wElcome'
import re
# print(re.sub('w','W',a))

# print(re.split('e',a))
# print(re.split('e',a,1))

# print(re.sub('w','W',a))

# print(re.search('w',a))

# if re.search('[a-z]',a):
#     print('a-z used')
#     if re.search('[1-9]',a):
#         print('numbers used')
#     else:
#         print('add numbers!')
# else:
#     print('no')
# a='abcd'
# print(re.search('a...',a))
# print(re.search('b.*',a))
# print(re.search('c.+',a))
# print(re.search('b.?',a))

print(re.search('[A-Z].*',a))
print(re.search('[a-z].?',a))
print(re.search('[a-z].+',a))
print(re.search('[a-z]..',a))
print(re.search('[a-z].',a))