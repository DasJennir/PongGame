"""def mandioca(x, y):


    if x == y or x > y :
        for b  in range (0, 20, 2):
            print(b)
    elif y > x :
            mandioca = True

    else:

            print('crl boracha')


mandioca = True
while mandioca == True:
        resposta = input('Say Something = ')
        if resposta == 'mori':
                mandioca = False
                break


bavareges = ['coke', 'water', 'pepsi']

for options in bavareges:

        if options == "water":
                print('That is Water')
        else:
                print('This is not water')

bavaregess = ['coke', 'water', 'pepsi', 2, 23]

for v in range(len(bavaregess)):
        if bavaregess[v] == "coke":
                print(bavaregess[v])
        else:
                print('This is not coke'.strip())


text = input('Saw something now !!!')
print(text.upper())"""


def nameProcess(namee, feeling):

        pergunta = input('Input Your Name:')
        print('Hello There How may I help you')

        pergunta()

        if namee == "":
                print('Input Your Name')
                pergunta()
        elif feeling == "":
                print('Input your mood')
        else:
                print('Nice')
