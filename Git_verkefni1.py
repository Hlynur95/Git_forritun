#hlynur Smári Gyðuson
#Git Verkefni
#27.1.2017

svar = "ja"

while svar == "ja": #while likkja yfir öll dæmin

    print("veldur 1,2,3 fyrir dæmi. 4 til að hætta")
    val = int(input("sláðu in 1-4 fyrir hvað þú vilt gera: ")) #læta notandan velja hvað hann vill gera

    if val == 1:
        summa1 = 0 #gildi til að finna samantals talnana
        summa2 = 1 #gildi til að finna margföldun talnana

        for x in range(2): #for lykkja sem bíður um 2 stafi
            tala = int(input("sláðu inn tölu: ")) #skrifar in stafina
            summa1 = summa1 + tala # leggja saman stafina
            summa2 = summa2 * tala # margfalda stafina saman

        print("saman lagt",summa1)
        print("margfaldað",summa2)


    if val == 2:
        fornarn = input("sláðu in fornarn: ") #slá in nafn
        eftirnafn = input("sláðu in eftirnarn: ") #slá in eftir nafni
        print("Hállo",fornarn,eftirnafn) #printa út nöfnin saman og seygja hallo


    if val == 3:
        texti = input("sláðu inn texta: ") #slá in texta
        storstafur = 0
        litilstafur = 0
        eftirstafur = 0

        for x in range(len(texti)): #fer yfir texti ein staf í einu
            if texti [x].isalpha() and texti[x].isupper(): # ef stafur [X] er i (texti) og er alpa og upper þá plusar hann við 1
                storstafur = storstafur + 1 #plús ein fyrir hvern upper staff
                if x!= len(texti)-1: #ef X er ekki komið á loka staf i (texti) þá heldur hann afram
                    if texti[x+1].islower(): #ef stafur er lower a eftir (x) sem er stor þá plúsar ein við
                        eftirstafur = eftirstafur + 1 #plúsar ein við
            if texti[x].isalpha() and texti[x].islower(): #ef orð í texti er alpha og lower þá plús ein
                litilstafur = litilstafur + 1

        print("það eru",storstafur,"storir stafir",litilstafur,"litlir stafir og",eftirstafur,"lágstafir a eftir hástafi")

    if val == 4: #hætta
        break






