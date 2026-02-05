import re

pattern = r"p\w{4}"
match = re.search(pattern,"my phone is a super phone")
#search matches the first instance only. not all.
print(match) #<re.Match object; span=(3, 8), match='phone'>
print(match.span()) #(3, 8)
print(match.start()) #3
print(match.end()) #8
print(match.string) #my phone is a super phone
print(match.group()) #return actual matched text - phone

#To find all matches use findall method
match_all = re.findall(pattern,"my phone is a super phone")
print(match_all) # print phone phone

# to get entire match object instead of just matched string use finditer
for match in re.finditer(pattern,"my phone is a super phone"):
    print(match.group()) # print phone twice
