#35 名詞の連接
import joblib
from itertools import islice
a = joblib.load("100knock_30")
nouns = [] #「名詞の連接」の配列
noun = []  #連接する前の名詞の配列
for sentense in a:
    for i in range(len(sentense)):
        if sentense[i]['pos'] == '名詞':
            noun.append(sentense[i]['surface'])
        else:
            if len(noun) >= 2:
                nouns.append(''.join(noun))
            noun = []
    if len(noun) >= 2:  #sentenseの終わりが名詞だった場合，nounにはまだ名詞が入っているので
        nouns.append(''.join(noun))
        noun = []
print(nouns)
