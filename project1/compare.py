f=open("blends4.txt")
f2=open("result_ngram.txt")
import re
def remove_punctuation(line):
    rule = re.compile("[^a-zA-Z0-9]")
    line = rule.sub('',line)
    return line

m=[]
for line in f.readlines():
    for word in line.split():
        m.append(word)
blend=list(set(m))

M=[]
for line in f2.readlines():
    for word in line.split():
        word2=remove_punctuation(word)
        M.append(word2)
blends=list(set(M))

count=0
for i in blend:
    for j in blends:
        if i==j:
            count=count+1
print("recall",(count-30)/(len(blend)-30))
print("precision", (count-30)/(len(blends)-30))


	

			


