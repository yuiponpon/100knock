#40  係り受け解析結果の読み込み（形態素）
from itertools import islice

class Morph:
    def __init__(self,surface,base,pos,pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1
    def print_ans(self):
        print("[surface:{},base:{},pos:{},pos1:{}]".format(self.surface,self.base,self.pos,self.pos1))

def analyze():
    with open("/mnt/c/Users/yui/Documents/work/100knock/neko.txt.cabocha") as f:
        sentence = []       #一文単位で解析結果を格納するための配列
        all_sentences = []  #全文の解析結果を格納するための配列
        for line in islice(f,50):
            line = line.strip() #１行区切りにする
            if line.startswith('EOS'):
                all_sentences.append(sentence)
                sentence = []  #EOSでsentenceの中身を空にする
            elif line.startswith('*'):
                continue
            else:
                part = line.split('\t') #タブで区切る
                if len(part) == 2:
                    surface = part[0]
                    other = part[1].split(',')
                else:
                    surface = ' '
                    other = part[0].split(',')
                sentence.append(Morph(surface,other[6],other[0],other[1]))
    return all_sentences

def main():
    all_sentences = analyze()
    for i,sentense1 in enumerate(all_sentences):
        if i == 2:
            for word in sentense1:
                word.print_ans()

if __name__ == '__main__':
    main()

"""
$ python3 40.py
[surface: ,base:　,pos:記号,pos1:空白]
[surface:吾輩,base:吾輩,pos:名詞,pos1:代名詞]
[surface:は,base:は,pos:助詞,pos1:係助詞]
[surface:猫,base:猫,pos:名詞,pos1:一般]
[surface:で,base:だ,pos:助動詞,pos1:*]
[surface:ある,base:ある,pos:助動詞,pos1:*]
[surface:。,base:。,pos:記号,pos1:句点]
"""
