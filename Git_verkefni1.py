#hlynur Smári Gyðuson
#Git Verkefni
#27.1.2017

svar = "ja"

while svar == "ja":

    print("veldur 1,2,3 fyrir dæmi. 4 til að hætta")
    val = int(input("sláðu in 1-4 fyrir hvað þú vilt gera: "))

    if val == 1:
        summa1 = 0
        summa2 = 1

        for x in range(2):
            tala = int(input("sláðu inn tölu: "))
            summa1 = summa1 + tala
            summa2 = summa2 * tala

        print("saman lagt",summa1)
        print("margfaldað",summa2)


    if val == 2:
        fornarn = input("sláðu in fornarn: ")
        eftirnafn = input("sláðu in eftirnarn: ")
        print("Hállo",fornarn,eftirnafn)





    if val == 3:
        texti = input("sláðu inn texta: ")
        storstafur = 0
        litilstafur = 0
        eftirstafur = 0

        for x in range(len(texti)):
            if texti [x].isalpha() and texti[x].isupper():
                storstafur = storstafur + 1
                if (texti[x+1].islower()):
                    eftirstafur = eftirstafur + 1
            if (texti[x].isalpha() and texti[x].islower()):
                litilstafur = litilstafur + 1

        print("það eru",storstafur,"storir stafir",litilstafur,"litlir stafir og",eftirstafur,"lágstafir a eftir hástafi")




    if val == 4:
        break






