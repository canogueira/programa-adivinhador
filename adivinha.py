print("pense em um numero de 0 a 10")
p1 = input(" o numero é maior ou igual a 5 (sim/nao): ").lower()
if p1 == "sim"  :

    p2 = input("o numero é par ? (sim/nao): ").lower()
    if p2 == "sim":
     
        p3 = input("o numero é maior ou igual 8 ? (sim/nao) ").lower()
        if p3 == "sim":
            p4 = input("o numero é maior que 9?").lower()
            if p4 == "sim":
                print("o numero é 10")
            elif p4 == "nao":
                print("o número é 8")
            else:
                print("erro digite corratamente")
        elif p3 == "nao":
            print("seu numero é 6")
    elif p2 == "nao":
            p5 = input("o numero é maior ou igual a 7?")
            if p5 == "sim":
                p6 = input("é maior que 8?")
                if p6 == "sim":
                    print("seu numero é 9")
                elif p6 == "nao":
                    p7 = input("o numero é maior que 6 ?") 
                    if p7 == "sim":
                        print("seu numero é 7 ")
                    elif p7 == "nao":
                        print("seu numero é 5 ")  
            elif p5 =="nao":
                        print("seu numero é 5")   
elif p1 == "nao":
        p8 = input("seu numero é par ?")
        if p8 == "sim":
            p9 = input("seu numero é maior ou igual a 2 ?")
            if p9 =="sim":
                p10 = input("o numero é maior que 3?")
                if p10 =="sim":
                    print("seu numero é 4")
                elif p10 == "nao":
                    print("seu numero é 2 ")
            elif p9 == "nao":
                    print("seu numero é 0")
        elif p8 == "nao":
                    p11 = input("é maior que 2? ")
                    if p11 == "sim":
                        print("seu numero é 3 ")
                    elif p11 == "nao":
                        print("seu numero é 1 ")







