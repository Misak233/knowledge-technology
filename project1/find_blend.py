import re,nltk
import editdistance
from nltk.corpus import wordnet as wn
from pyjarowinkler import distance
import ngram
stemmer=nltk.stem.PorterStemmer()
f=open("result.txt",'w')

b=open("blends3.txt")
d=open("dict.txt")
m=[]
for line in d.readlines():
    for word in line.split():
        m.append(word)

dic=list(set(m))
w=[]
for line in b.readlines():
    for word in line.split():
        w.append(word)
word=list(set(w))

#prefix
def find_prefix(a1,a2):
    a=0
    while a<len(a1) \
        and a<len(a2) \
        and a1[a]==a2[a]:
        a=a+1
    return a1[:a]
#suffix
def find_suffix(k1,k2):
    w1=''.join(list(reversed(k1)))
    w2=''.join(list(reversed(k2)))
    pre=find_prefix(k1,k2)
    suff=''.join(list(reversed(pre)))
    return suff
#calculate dis
def cal_dis1(I,w1):
    a1=100000
    a2=100000
    r=0
    for i in I:
        a2=editdistance.eval(w1,i)
        if a1>=a2:
            r=i
            a1=a2
    return r

def cal_dis2(i,j):
    d=0
    i1=0
    j1=0
    for I in i:
        I1=wn.synset(I+'.a.0')
        for J in j:
            J1 = wn.synset(J+'.a.0')
            score=I1.path_similarity(J1)
            if d<=score:
                d=score
                i1=I
                j1=J
    return set((i1,j1))

def cal_dis3(I,J):
    d=0
    loc1=0
    for i in I:
        n=ngram.NGram.compare(i,J,N=3)
        if d<=n:
            loc1=i
            d=n
    return loc1

def cal_dis4(I,J):
    d=0
    loc1=0
    for i in I:
        n=distance.get_jaro_distance(i,J,winkler=True,scaling=0.1)
        if d<=n:
            loc1=i
            d=n
    return loc1
#search blend1
def find_blend(word,dic):
    w3=[]
    w2=[]
    w=[]
    w1=word
    word_stem=stemmer.stem(w1)
    dic1=[x for x in dic if \
                not stemmer.stem(x)==w1 \
                and not x==w1 and not stemmer.stem(x)==word_stem  \
                and not x==word_stem
                ]
    w1s=set([x for x in dic1 if \
             x.startswith(w1[:2]) and not w1 in x])
# This w1s and w2s ideas come from Cook, P., & Stevenson, S. (2010). Automatically identifying the source words of lexical blends in English. Computational Linguistics, 36(1), 129-149.
    w2s=set([x for x in dic1 if \
                x.endswith(w1[-2:]) and not w1 in x])

    for i in w1s:
        pre=find_prefix(i,w1)
        for k in w2s:
            suff=find_suffix(k,w1)
            if len(pre)+len(suff)>=len(w1)\
                and len(pre)<len(suff) \
                and not i+k==word and not i==k\
                and not k.startswith(i)and not i.endswith(k):
                w3.append(i)
                w2.append(k)

    w.append((cal_dis1(w2,word),cal_dis1(w3,word)))
    return w

S=[]
k=[]
for i in word:
    blends=find_blend(i,dic)
    print("1")
    for j in blends:
        S.append((i,j))


for i in S:
    f.write(str(i))
    f.write('\n')





