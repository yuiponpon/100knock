#41 係り受け解析結果の読み込み（文節・係り受け）

from itertools import islice

class Morph:
    def __init__(self,surface,base,pos,pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

class Chunk:
    def __init__(self,dst):
        self.morphs = []
        self.dst = dst
        self.srcs = []
    def chunk(self):
        sur = ''
        for x in self.morphs:
            sur += x.surface
        #return "[chunk:{},dst:{},srcs:{}]".format(sur,self.dst,self.srcs)
        return sur,self.dst,self.srcs

def analyze():
    with open("/mnt/c/Users/yui/Documents/work/100knock/neko.txt.cabocha") as f:
        sentence = []       #一文単位で解析結果を格納するための配列
        all_sentences = []  #全文の解析結果を格納するための配列

        for line in islice(f,500):
        #for line in f:
            line = line.strip()
            if line.startswith('*'):
                r = line.split()
                dst = r[2][:-1]
                chunk = Chunk(dst)  #morphsとsrcsのからの配列[]が誕生
                sentence.append(chunk)
            elif line.startswith('EOS'):  #EOSでsrcsの中身も埋めてくよ
                # if sentence:      #空行分も一文と数えるならif文はコメントアウト
                for i,chunk1 in enumerate(sentence):
                    if int(chunk1.dst) > 0:
                        sentence[int(chunk1.dst)].srcs.append(i)
                all_sentences.append(sentence)
                sentence = []
            else:
                '''形態素の処理'''
                part = line.split('\t') #タブで区切る
                if len(part) == 2:
                    surface1 = part[0]
                    other = part[1].split(',')
                else:
                    surface1 = ' '
                    other = part[0].split(',')
                chunk.morphs.append(Morph(surface1,other[6],other[0],other[1]))
    return all_sentences

def main():
    all_sentences = analyze()
    for i,sentence1 in enumerate(all_sentences):
        if i == 7:
            j = 0
            for c in sentence1:
                #print("[{}]:{}".format(j,c.chunk()))
                x = c.chunk()
                print("[{}]:{}".\
                    format(j,"[chunk:{},dst:{},srcs:{}]".format(x[0],x[1],x[2])))
                j += 1

if __name__ == '__main__':
    main()

'''
[0]:[chunk:吾輩は,dst:5,srcs:[]]
[1]:[chunk:ここで,dst:2,srcs:[]]
[2]:[chunk:始めて,dst:3,srcs:[1]]
[3]:[chunk:人間という,dst:4,srcs:[2]]
[4]:[chunk:ものを,dst:5,srcs:[3]]
[5]:[chunk:見た。,dst:-1,srcs:[0, 4]]
'''
