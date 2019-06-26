#33 サ変名詞
import joblib
a = joblib.load("100knock_30")
noun = []
for sentense in a:
    for i in range(len(sentense)):
        if sentense[i]['pos1'] == 'サ変接続':
            noun.append(sentense[i]['surface'])
print(noun)
