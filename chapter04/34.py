#34 AのB
import joblib
a = joblib.load("100knock_30")
AB = []
for sentense in a:
    for i in range(len(sentense)):
        if sentense[i]['surface'] == 'の' and sentense[i - 1]['pos'] == '名詞' and sentense[i + 1]['pos'] == '名詞':
            AB.append(sentense[i-1]['surface'] + sentense[i]['surface'] + sentense[i+1]['surface'])
print(AB)
