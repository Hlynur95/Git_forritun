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





    #if val == 3:




    #if val == 4:





