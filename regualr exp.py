import re

code=input()

code=re.sub('[a-zA-z,@!#$%^&*_{}?>''<.:()" "]',"",code)
print(code)
