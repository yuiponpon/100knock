#32 動詞の原型
import joblib
a = joblib.load("100knock_30")
base = []
for sentense in a:
    for i in range(len(sentense)):
        if sentense[i]['pos'] == '動詞':
            base.append(sentense[i]['base'])
print(base)
