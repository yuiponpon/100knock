#44

#42番を再利用
from a41 import Morph,Chunk
from a41 import analyze
from graphviz import Digraph

def cds(sentence): #一文分のc_d_s_listを返す
    c_d_s_list = []  #一文分のchunk，dst，srcsが格納される配列
    for c in sentence:
        x = c.chunk()
        x_0 = ''
        for morph in c.morphs:  #ひとチャンク中から，ひと単語分のmorphを取り出す(各単語に含まれる記号を取り除く処理)
            if morph.pos != '記号':
                x_0 += morph.surface
        c_d_s_list.append([x_0,x[1],x[2]])
    return c_d_s_list

def main():
    all_sentences = analyze()
    all_s = []  #全文分の係り元と係り先の文節を格納する
    for i,sentence1 in enumerate(all_sentences):
        s = []  #一文分の係り元と係り先の文節を格納する
        x = cds(sentence1)
        for cds_1chunk in x:
            if int(cds_1chunk[1]) != -1 and cds_1chunk[0] != '' :  #記号，空白などのチャンクは空欄''になってるはずなので表示しない
                d = x[int(cds_1chunk[1])][0]
                s.append([cds_1chunk[0],d])
                #print("{}\t{}".format(cds_1chunk[0],d))
        if s != []:
            all_s.append(s)
        #print()
    # print(all_s[9])

    # formatはpngを指定(他にはPDF, PNG, SVGなどが指定可)
    G = Digraph(format='png')
    G.attr('node', shape='circle')

    s_1 = all_s[9]  #（空欄数えない）５文目の文の係り受け木を表示する
    N = len(s_1)    # ノード数

    for i in s_1:
        G.edge(i[0], i[1])

    # print()でdot形式で出力
    print(G)

    # dg44.pngで保存
    G.render('dg44')

if __name__ == '__main__':
    main()
