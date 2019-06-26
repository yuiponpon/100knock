#30
import joblib
from itertools import islice
with open("/mnt/c/Users/yui/Documents/work/100knock/neko.txt.mecab") as f:
    new_line = []
    new_lines = []
    for line in islice(f,5000):
    #for line in f:
        if len(line.strip().split('\t'))<2:
            new_line = []
        else:
            line = line.strip()
            #print(line)        #吾輩    名詞,代名詞,一般,*,*,*,吾輩,ワガハイ,ワガハイ
            surface = line.split('\t')
            #print(surface)     #['吾輩', '名詞,代名詞,一般,*,*,*,吾輩,ワガハイ,ワガハイ']
            other = surface[1].split(',')
            word = {'surface':surface[0],'base':other[6],'pos':other[0],'pos1':other[1]}
            new_line.append(word)
            if word['pos1'] == '句点':
                new_lines.append(new_line)
                #print(new_lines)
                #exit()
                joblib.dump(new_lines,"100knock_30")
                new_line = []
a = joblib.load("100knock_30")
print(a)
