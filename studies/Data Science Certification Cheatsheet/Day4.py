###############Question1###########################
import re

sent = input("enter a string with or without z to check for the validity of the regular exp\n")

condition = '\Bz\B'
if re.search(condition,sent):
    print("This sentence is Valid")
else:
    print("This sentence is not Valid")

###################Question2###########################
print("")
print("number 2")
print("")
words = ["example (.com)", "summitworks", "github (.com)", "stackoverflow (.com)"]
pattern = r'\([^)]+\)'

for word in words:
    print(re.sub(pattern,"",word))

###################Question 3########################
print("")
print("number 3")
print("")
split_terms = ';|,|/|\s'
inp = "this is a (same!ple of h;wo/rds"
print(re.split(split_terms,inp))

###################Question 4########################
print("")
print("number 4")
print("")
text = '<p>Contents :</p><a href="https://summitworks.com">Python january 2021 batch<a href="http://github.com">'
urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)

print(urls, end="")