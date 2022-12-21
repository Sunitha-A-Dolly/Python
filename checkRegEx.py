import re

emaillist = "My email id is sun_light@gmail.com and another id is sunselfinsight.2022@gmail.com"
# p = "[\w\.]*\@\w*\.\w{2,3}"
p = "\w{10,20}"
print(re.findall(p, emaillist))
res = re.search(p, emaillist)
print(res.group())

#sample = re.finditer(p, emaillist)
#print(sample.)