import re

code = (input())
code = re.sub('[a-zA-z,@!+#/|$%^&*_{}?>''₹<.;:()""`~]', "", code)
a = list(code)

if a[0] == '-':
    c = a[0]
    d = a[1:]
    str2 = ""
    for ele in d:
        str2 += ele
    str2 = re.sub('[-]', "", str2)
    h = c+str2
    print(h)
else:
    print(code)
