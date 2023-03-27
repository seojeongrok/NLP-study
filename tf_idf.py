from kiwipiepy import Kiwi
from kiwipiepy.utils import Stopwords
# 데이터프레임 사용
import pandas as pd
# IDF 계산
from math import log


Stopwords = Stopwords()
# kiwi 객체 생성
kiwi = Kiwi(num_workers=2, load_default_dict=True, integrate_allomorph=True, model_type='sbg')


docs = [
    "유방암이란 무엇인가요?",
    "유방암의 원인은 무엇인가요?",
    "유방암 1기 증상은?"
]

vocab = set()

for i in range(len(docs)):
    tokens = kiwi.tokenize(docs[i])
    for j in range(len(tokens)):
        vocab.add(tokens[j].form)

setvocab = list(vocab)
print(setvocab)


# 총 문서의 수
N = len(docs)

def tf(t, d):
    return d.count(t)

def idf(t):
    df = 0
    for doc in docs:
        df += t in doc
    return log(N/(df+1))

def tfidf(t, d):
    return tf(t, d) * idf(t)


result = []


for i in range(N):
    result.append([])
    d = docs[i]
    for j in range(len(setvocab)):
        t = setvocab[j]
        result[-1].append(tf(t, d))

tf_ = pd.DataFrame(result, columns=setvocab)

print(tf_)

result = []
for j in range(len(setvocab)):
    t = setvocab[j]
    result.append(idf(t))

idf_ = pd.DataFrame(result, index=setvocab, columns=["IDF"])

print(id)