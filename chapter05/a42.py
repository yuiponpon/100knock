#42 after
from a41 import Morph,Chunk
from a41 import analyze

def main():
    all_sentences = analyze()
    all_c_d_s_list = [] #全文ver
    for i,sentence1 in enumerate(all_sentences):
        c_d_s_list = []  #一文分のchunk，dst，srcsが格納される配列
        for c in sentence1:
            #c_d_s_list.append(c.chunk().replace("[chunk:","").replace("dst:","").replace("srcs:","").split(","))
            x = c.chunk()
            x_0 = ''
            for morph in c.morphs:  #ひとチャンク中から，ひと単語分のmorphを取り出す(各単語に含まれる記号を取り除く処理)
                if morph.pos != '記号' :
                    x_0 += morph.surface
            c_d_s_list.append([x_0,x[1],x[2]])
        all_c_d_s_list.append(c_d_s_list)

    for cds_1sentence in all_c_d_s_list:
        x = cds_1sentence
        for cds_1chunk in cds_1sentence:
            if int(cds_1chunk[1]) != -1 and cds_1chunk[0] != '':  #記号，空白などのチャンクは空欄''になってるはずなので表示しない
                d = x[int(cds_1chunk[1])][0]
                print("{}\t{}".format(cds_1chunk[0],d))
        print()
            # else:
            #     print("{}".format(cds_1chunk[0]))


if __name__ == '__main__':
    main()
