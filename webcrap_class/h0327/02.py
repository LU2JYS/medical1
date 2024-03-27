
with open('c:/workspace/medical1/h0327/aaa/member2.csv','r',encoding='utf8') as f:
        while True:
            txt = f.readline()
            if txt == "": break
            mem = txt.split(",")
            print(mem[0],mem[1])
                

    