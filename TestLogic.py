
def Shuffle(cards, process):

    while (0 < len(process)):
        if (process[0].isnumeric()):
            for i in range(len(process)):
                if not (process[i].isnumeric()):
                    break;

            num=int(process[0:i])
            for j in range(num-1):
                print(process[i])
        else:
            print(process[0])

        process=process[1:]



Shuffle("aa", "2C5R7C3R")