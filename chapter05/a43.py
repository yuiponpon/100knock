#43
from a41 import Morph,Chunk
from a41 import analyze

def chunk_num(chunk):
    i = 0  #チャンクに名詞が含まれているか判定(含まれていたら1)
    for morph in chunk.morphs:
        if morph.pos == '名詞':
            i = 1
    return i

def chunk_verb(chunk):
    j = 0  #チャンクに動詞が含まれているか判定(含まれていたら1)
    for morph in chunk.morphs:
        if morph.pos == '動詞':
            j = 1
    return j

def cds(sentence): #一文分のc_d_s_listを返す(a42_another_ansのcdsに「チャンクに名詞，動詞が含まれるかどうかの判定」も追加したver)
    c_d_s_list = []  #一文分のchunk，dst，srcsが格納される配列
    for c in sentence:
        i = chunk_num(c)   #名詞の有無判定
        j = chunk_verb(c)  #動詞の有無判定
        x = c.chunk()
        x_0 = ''
        for morph in c.morphs:  #ひとチャンク中から，ひと単語分のmorphを取り出す(各単語に含まれる記号を取り除く処理)
            if morph.pos != '記号':
                x_0 += morph.surface
        c_d_s_list.append([x_0,x[1],x[2],i,j])
    return c_d_s_list

def main():
    all_sentences = analyze()
    all_c_d_s_list = [] #全文ver
    for i,sentence1 in enumerate(all_sentences):
        x = cds(sentence1)
        for cds_1chunk in x:
            if int(cds_1chunk[1]) != -1 and cds_1chunk[0] != '' :  #記号，空白などのチャンクは空欄''になってるはずなので表示しない
                if int(cds_1chunk[3]) == 1 and x[int(cds_1chunk[1])][4] == 1: #名詞を含む文節が，動詞を含む文節に係るかどうか
                    d = x[int(cds_1chunk[1])][0]
                    print("{}\t{}".format(cds_1chunk[0],d))

if __name__ == '__main__':
    main()

'''
どこで	生れたか
見当が	つかぬ
所で	泣いて
ニャーニャー	泣いて
いた事だけは	記憶している
吾輩は	見た
ここで	始めて
ものを	見た
あとで	聞くと
我々を	捕えて
'''
