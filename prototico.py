import os
import time
import random
#=============================
corp='#'
corp2='◘'
#movimentação=============================
es=10 #basi
di=10 #basi
es1=0
di1=0
dir=30 #basi
di2=0
#combate=============================
nivel=1
aparece=0
print('')
print('\033[0;37;40m Quando estiver sobe ataque aparecera um numero no \n canto direito superior da tela \n se a relação for (termo 1 > termo 2) você pode abater \n seu inimigo usado teclas "t"e"d" juntas.\n mas se relação for contraria é GAME OVER \napos 20 segundos o jogo é iniciado')
print('')
time.sleep(20)
os.system('cls')
while True:
    #===========
    spaw=int(random.random()*5)
    #===========
    if nivel==5 and aparece==1:
        print('\033[0;33;40m agora digitando palavra " menu " voçê pode receber\n informação diversificadas do jogo')
        time.sleep(10)
        aparece=0
        os.system('cls')
    print('\033[0;37;40m ')#1
    print(' ')#2
    print(' ')#3
    print(' ')#4
    print(' ')#5
    print(' ')#6
    print(' ')#7
    print(' ')#8
    print(' ')#9
    print(' ')#10
    print(' ')#11
    print(' ')#12
    print(' ')#13
    print(' ')#14
    print(' ')#15
    print(' ')#16
    print(' ')#17
    print(' ')#18
    print(' ')#19
    print(' ')#20
    print(' ')#21
    print(' ')#22
    print(' '*es1,'    {}'.format(corp),' '*di1)
    print(' '*es1,'  {}'.format(corp),'{}'.format(corp),'{}'.format(corp),' '*di1)
    print(' '*es1,' {}'.format(corp),' {}'.format(corp),' {}'.format(corp),' '*di1)
    print(' '*es1,' {}'.format(corp),' {}'.format(corp),' {}'.format(corp),' '*di1)
    print(' '*es1,' {}'.format(corp),' {}'.format(corp),' {}'.format(corp),' '*di1)
    print(' '*es1,'    {}'.format(corp),' '*di1)
    print(' '*es1,'  {}'.format(corp),'  {}'.format(corp),' '*di1)
    print(' '*es1,'  {}'.format(corp),'  {}'.format(corp),' '*di1)
    print(' '*es1,'  {}'.format(corp),'  {}'.format(corp),' '*di1)
    print(' '*es1,'  {}'.format(corp),'  {}'.format(corp),' '*di1)
    cont=str(input('>'))
    if cont=='d':
        es1=es=es+1 
        di1=di=di-1
    elif cont=='a':
        es1=es=es-1
        di1=di=di+1
    if cont=='a'or'd':
        time.sleep(0.01)
        os.system('cls')
# soco//////////////////////////////////////
    if cont=='e':
        print(' ')#1
        print(' ')#2
        print(' ')#3
        print(' ')#4
        print(' ')#5
        print(' ')#6
        print(' ')#7
        print(' ')#8
        print(' ')#9
        print(' ')#10
        print(' ')#11
        print(' ')#12
        print(' ')#13
        print(' ')#14
        print(' ')#15
        print(' ')#16
        print(' ')#17
        print(' ')#18
        print(' ')#19
        print(' ')#20
        print(' ')#21
        print(' ')#22
        print(' '*es1,'    {}'.format(corp),' '*di1)
        print(' '*es1,'  {}'.format(corp),'{}'.format(corp),'{}'.format(corp),'{}'.format(corp),'{}'.format(corp),'{}'.format(corp),' '*di1)
        print(' '*es1,' {}'.format(corp),' {}'.format(corp))
        print(' '*es1,' {}'.format(corp),' {}'.format(corp))
        print(' '*es1,' {}'.format(corp),' {}'.format(corp))
        print(' '*es1,'    {}'.format(corp),' '*di1)
        print(' '*es1,'  {}'.format(corp),'  {}'.format(corp),' '*di1)
        print(' '*es1,'  {}'.format(corp),'  {}'.format(corp),' '*di1)
        print(' '*es1,'  {}'.format(corp),'  {}'.format(corp),' '*di1)
        print(' '*es1,'  {}'.format(corp),'  {}'.format(corp),' '*di1) 
        time.sleep(0.3)   
        os.system('cls')
    if cont=='q':
        print(' ')#1
        print(' ')#2
        print(' ')#3
        print(' ')#4
        print(' ')#5
        print(' ')#6
        print(' ')#7
        print(' ')#8
        print(' ')#9
        print(' ')#10
        print(' ')#11
        print(' ')#12
        print(' ')#13
        print(' ')#14
        print(' ')#15
        print(' ')#16
        print(' ')#17
        print(' ')#18
        print(' ')#19
        print(' ')#20
        print(' ')#21
        print(' ')#22
        print(' '*es1,f'        {corp}',' '*di1)
        print(' '*es1,f'{corp}',f'{corp}',f'{corp}',f'{corp}',f'{corp}',f'{corp}',' '*di1)
        print(' '*es1,f'        {corp}',f' {corp}',' '*di1)
        print(' '*es1,f'        {corp}',f' {corp}',' '*di1)
        print(' '*es1,f'        {corp}',f' {corp}',' '*di1)
        print(' '*es1,f'        {corp}',' '*di1)
        print(' '*es1,f'      {corp}',f' {corp}',' '*di1)
        print(' '*es1,f'      {corp}',f' {corp}',' '*di1)
        print(' '*es1,f'      {corp}',f' {corp}',' '*di1) 
        print(' '*es1,f'      {corp}',f' {corp}',' '*di1) 
        time.sleep(0.3)   
        os.system('cls')
# comfroto nivel 1 a 5 ////////////////////////////////
    if spaw==nivel:
        di2=dir
        while dir > 0:
            print("seu poder",di1,'poder do inimigo',di2)
            #00000
            print(' ')#5
            print(' ')#6
            print(' ')#7
            print(' ')#8
            print(' ')#9
            print(' ')#10
            print(' ')#11
            print(' ')#12
            print(' ')#13
            print(' ')#14
            print(' ')#15
            print(' ')#16
            print(' ')#17
            print(' ')#18
            print(' ')#19
            print(' ')#20
            print(' ')#21
            print(' ')#22
            print(' ')#23
            print(' ')#24
            print(' ')#25
            print(' '*es1,'    {}'.format(corp),' '*di1)
            print(' '*es1,'  {}'.format(corp),'{}'.format(corp),'{}'.format(corp),' '*di1,' '*di2,'{}{}{}{}{}'.format(corp,corp,corp,corp,corp),' '*es1)
            print(' '*es1,' {}'.format(corp),' {}'.format(corp),' {}'.format(corp),' '*di1,' '*di2,'{}{}{}{}'.format(corp,corp2,corp2,corp),' '*es1)
            print(' '*es1,' {}'.format(corp),' {}'.format(corp),' {}'.format(corp),' '*di1,' '*di2,'{}{}{}{}'.format(corp,corp,corp,corp),' '*es1)
            print(' '*es1,' {}'.format(corp),' {}'.format(corp),' {}'.format(corp),' '*di1,' '*di2,'{}{}{}{}'.format(corp,corp,corp,corp),' '*es1)
            print(' '*es1,'    {}'.format(corp),' '*di1)
            print(' '*es1,'  {}'.format(corp),'  {}'.format(corp),' '*di1,)
            print(' '*es1,'  {}'.format(corp),'  {}'.format(corp),' '*di1,)
            print(' '*es1,'  {}'.format(corp),'  {}'.format(corp),' '*di1,)
            print(' '*es1,'  {}'.format(corp),'  {}'.format(corp),' '*di1,) 
            cont=str(input('>'))
            if cont=='d':
                es1=es=es+1 
                di1=di=di-1
                di2=dir=dir-1
            elif cont=='a':
                es1=es=es-1
                di1=di=di+1
                di2=dir=dir-1
            if di2 <= 0:
                print(' THE END voçê agora esta nivel 5 \n voçê zerou o poder do inimigo')
                nivel=5
                aparece=1
                time.sleep(10)
                os.system('cls')
                break
            elif cont =='td' and  di1 > di2:
                print(' ')#1
                print(' ')#2
                print(' ')#3
                print(' ')#4
                print(' ')#5
                print(' ')#6
                print(' ')#7
                print(' ')#8
                print(' ')#9
                print(' ')#10
                print(' ')#11
                print(' ')#12
                print(' ')#13
                print(' ')#14
                print(' ')#15
                print(' ')#16
                print(' ')#17
                print(' ')#18
                print(' ')#19
                print(' ')#20
                print(' ')#21
                print(' ')#22
                print(' ')#23
                print(' ')#24
                print(' ')#25
                print(' '*es1,'    {}'.format(corp),' '*di1)
                print(' '*es1,'  {}'.format(corp),'{}'.format(corp),'{}'.format(corp),'{}'.format(corp),'{}'.format(corp),'{}'.format(corp),' '*di1,' '*di2,'{}{}{}{}{}'.format(corp,corp,corp,corp,corp),' '*es1)
                print(' '*es1,' {}'.format(corp),' {}'.format(corp),' '*di2,'{}{}{}{}'.format(corp,corp2,corp2,corp),' '*es1)
                print(' '*es1,' {}'.format(corp),' {}'.format(corp),' '*di2,'{}{}{}{}'.format(corp,corp,corp,corp),' '*es1)
                print(' '*es1,' {}'.format(corp),' {}'.format(corp),' '*di2,'{}{}{}{}'.format(corp,corp,corp,corp),' '*es1)
                print(' '*es1,'    {}'.format(corp),' '*di1)
                print(' '*es1,'  {}'.format(corp),'  {}'.format(corp),' '*di1)
                print(' '*es1,'  {}'.format(corp),'  {}'.format(corp),' '*di1)
                print(' '*es1,'  {}'.format(corp),'  {}'.format(corp),' '*di1)
                print(' '*es1,'  {}'.format(corp),'  {}'.format(corp),' '*di1)
                di=di1-di2
                dir=di1-di2
                time.sleep(0.3)   
                os.system('cls')
                break
            if di1 < di2 and cont=='td':
                os.system('cls')
                print(' '*20,'GAME OVER',' '*20)
                di1=8
                es1=4
                time.sleep(6)
                os.system('cls')
                break
            if cont=='a'or'd':
                time.sleep(0.001)
                os.system('cls')         
#menu////////////////////////////////////////
    if cont=='menu' and nivel==5:
        print('\033[0;33;40m')
        print('     #     #      ####       #       #  #     #           ')
        print('    # #   # #     #         # #     #   #     #           ')
        print('   #   # #   #    ####     #   #   #    #     #           ')
        print('  #     #     #   #       #     # #      #   #            ')
        print(' #             #  ####   #       #        ###             ')
        print('                                                          ')
        print('posição esquerda {} posição direita {}'.format(di1,es1))
        print('nivel {}'.format(nivel))
        cont=str(input('digiti " ok " para fechar o menu > '))
        if cont =='ok':
            os.system('cls')
#resulução de bug//////////////////////////////////////////////////////////////////////////
    if es==172 and di <=-152:
        di=20
        es=0


