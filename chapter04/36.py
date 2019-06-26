#36　単語の出現頻度
import collections
import joblib
from itertools import islice
a = joblib.load("100knock_30")
words = [] #単語の要素surfaceだけを抽出した配列
for sentense in a:
    for word in sentense:
        words.append(word['surface'])
c = collections.Counter(words)
print(c.most_common())
