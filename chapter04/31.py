#31

from itertools import islice
with open("/mnt/c/Users/yui/Documents/work/100knock/neko.txt.mecab") as f:
    for line in islice(f,30):
    #for line in f:
        line = line.rstrip()
        surface_other = line.split("\t")
        #print(surface_other)
        if len(surface_other) > 1:
            #print(surface_other[1].split(",")[0])
            if surface_other[1].split(",")[0] == "動詞":
                print(surface_other[0])
