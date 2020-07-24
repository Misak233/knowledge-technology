import nltk, re, sys
def interp(word, dic):
    for i in range(2,len(word)-2):
        a,b = word[:i],word[i:]
        if a in dic and b in dic:
            return True
    return False

def repeat_words(w):
    return re.search("([a-zA-Z])\\1{3,}",w)

b=open("candidates.txt")
d=open("dict.txt")
f=open("blend_source2.txt",'w')
m=[]
for line in d.readlines():
    for word in line.split():
        m.append(word)
dic=list(set(m))

w=[]
for line in b.readlines():
    for word in line.split():
        w.append(word)
words=list(set(w))

num=0
blends=[i for i in words if \
            not repeat_words(i) and \
            len(i)>2 and
            interp(i,dic) and
            len(i)<15]
for i in blends:
    f.write(i)
    f.write('\n')



