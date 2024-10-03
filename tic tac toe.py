a1 = '-'
a2 = '-'
a3 = '-'
b1 = '-'
b2 = '-'
b3 = '-'
c1 = '-'
c2 = '-'
c3 = '-'
t1 = 0
t2 = 0
t3 = 0
t4 = 0
t5 = 0
t6 = 0
t7 = 0
t8 = 0
t9 = 0
X = 'X'
O = 'O'
turn = 0

print('Hello, welcome to tic tac toe game! Here is your game scheme:')
print('')
print("     1   2   3")
print("1 "," ---|---|---")

print("2 "," ---|---|---")

print("3 "," ---|---|---")
print('')
print('')
while turn != 9:
 choice = str(input(('Player 1 - which action? (example: 1.1)')))
 current_player = X


 def check():
    if a1 == 'X' and a2 == 'X' and a3 == 'X':
     print('PLAYER 1 WON!!!')
     exit()


    if a1 == 'X' and b2 == 'X' and c3 == 'X':
         print('PLAYER 1 WON!!!')
         exit()



    if a3 == 'X' and b2 == 'X' and c1 == 'X':
         print('PLAYER 1 WON!!!')
         exit()


    if b1 == 'X' and b2 == 'X' and b3 == 'X':
         print('PLAYER 1 WON!!!')
         exit()


    if c1 == 'X' and c2 == 'X' and c3 == 'X':
         print('PLAYER 1 WON!!!')
         exit()


    if a1 == 'X' and b1 == 'X' and c1 == 'X':
         print('PLAYER 1 WON!!!')
         exit()


    if a2 == 'X' and b2 == 'X' and c2 == 'X':
         print('PLAYER 1 WON!!!')
         exit()


    if a3 == 'X' and b3 == 'X' and c3 == 'X':
         print('PLAYER 1 WON!!!')
         exit()




    if a1 == 'O' and a2 == 'O' and a3 == 'O':
         print('PLAYER 2 WON!!!')
         exit()


    if a1 == 'O' and b2 == 'O' and c3 == 'O':
         print('PLAYER 2 WON!!!')
         exit()


    if a3 == 'O' and b2 == 'O' and c1 == 'O':
         print('PLAYER 2 WON!!!')
         exit()


    if b1 == 'O' and b2 == 'O' and b3 == 'O':
         print('PLAYER 2 WON!!!')
         exit()


    if c1 == 'O' and c2 == 'O' and c3 == 'O':
         print('PLAYER 2 WON!!!')
         exit()


    if a1 == 'O' and b1 == 'O' and c1 == 'O':
         print('PLAYER 2 WON!!!')
         exit()


    if a2 == 'O' and b2 == 'O' and c2 == 'O':
         print('PLAYER 2 WON!!!')
         exit()


    if a3 == 'O' and b3 == 'O' and c3 == 'O':
         print('PLAYER 2 WON!!!')
         exit()


    if turn == 9:
         print('DRAW!! GG!')
         exit()




 if choice == '1.1' and a1 == '-' and t1 == 0:
   a1 = current_player
   print("|", a1, a2, a3, "|")
   print("|", b1, b2, b3, "|")
   print("|", c1, c2, c3, "|")
   turn += 1
   t1+=1
   check()
 elif choice == '1.2' and a2 == '-' and t2 == 0:
        a2 = current_player
        print("|", a1, a2, a3, "|")
        print("|", b1, b2, b3, "|")
        print("|", c1, c2, c3, "|")
        turn += 1
        t2 += 1
        check()
 elif choice == '1.3' and a3 == '-' and t3 == 0:
        a3 = current_player
        print("|", a1, a2, a3, "|")
        print("|", b1, b2, b3, "|")
        print("|", c1, c2, c3, "|")
        turn += 1
        t3 += 1
        check()
 elif choice == '2.1' and b1 == '-' and t4 == 0:
        b1 = current_player
        print("|", a1, a2, a3, "|")
        print("|", b1, b2, b3, "|")
        print("|", c1, c2, c3, "|")
        turn += 1
        t4 += 1
        check()
 elif choice == '2.2' and b2 == '-' and t5 == 0:
        b2 = current_player
        print("|", a1, a2, a3, "|")
        print("|", b1, b2, b3, "|")
        print("|", c1, c2, c3, "|")
        turn += 1
        t5 += 1
        check()
 elif choice == '2.3' and b3 == '-' and t6 == 0:
        b3 = current_player
        print("|", a1, a2, a3, "|")
        print("|", b1, b2, b3, "|")
        print("|", c1, c2, c3, "|")
        turn += 1
        t6 += 1
        check()
 elif choice == '3.1' and c1 == '-' and t7 == 0:
        c1 = current_player
        print("|", a1, a2, a3, "|")
        print("|", b1, b2, b3, "|")
        print("|", c1, c2, c3, "|")
        turn += 1
        t7 += 1
        check()
 elif choice == '3.2' and c2 == '-' and t8 == 0:
        c2 = current_player
        print("|", a1, a2, a3, "|")
        print("|", b1, b2, b3, "|")
        print("|", c1, c2, c3, "|")
        turn += 1
        t8 += 1
        check()
 elif choice == '3.3' and c3 == '-' and t9 == 0:
        c3 = current_player
        print("|", a1, a2, a3, "|")
        print("|", b1, b2, b3, "|")
        print("|", c1, c2, c3, "|")
        turn += 1
        t9 += 1
        check()
 else:
  print("This cell is already taken or invalid input. Try again.")
  continue

 choice1 = str(input(('Player 2 - which action? (example: 1.1)')))
 current_player = O
 if choice1 == '1.1' and a1 == '-' and t1 == 0:
   a1 = current_player
   print("|", a1, a2, a3, "|")
   print("|", b1, b2, b3, "|")
   print("|", c1, c2, c3, "|")
   turn += 1
   t1 += 1
   check()
 elif choice1 == '1.2' and a2 == '-' and t2 == 0:
        a2 = current_player
        print("|", a1, a2, a3, "|")
        print("|", b1, b2, b3, "|")
        print("|", c1, c2, c3, "|")
        turn += 1
        t2 += 1
        check()
 elif choice1 == '1.3' and a3 == '-' and t3 == 0:
        a3 = current_player
        print("|", a1, a2, a3, "|")
        print("|", b1, b2, b3, "|")
        print("|", c1, c2, c3, "|")
        turn += 1
        t3 += 1
        check()
 elif choice1 == '2.1' and b1 == '-' and t4 == 0:
        b1 = current_player
        print("|", a1, a2, a3, "|")
        print("|", b1, b2, b3, "|")
        print("|", c1, c2, c3, "|")
        turn += 1
        t4 += 1
        check()
 elif choice1 == '2.2' and b2 == '-' and t5 == 0:
        b2 = current_player
        print("|", a1, a2, a3, "|")
        print("|", b1, b2, b3, "|")
        print("|", c1, c2, c3, "|")
        turn += 1
        t5 += 1
        check()
 elif choice1 == '2.3' and b3 == '-' and t6 == 0:
        b3 = current_player
        print("|", a1, a2, a3, "|")
        print("|", b1, b2, b3, "|")
        print("|", c1, c2, c3, "|")
        turn += 1
        t6 += 1
        check()
 elif choice1 == '3.1' and c1 == '-' and t7 == 0:
        c1 = current_player
        print("|", a1, a2, a3, "|")
        print("|", b1, b2, b3, "|")
        print("|", c1, c2, c3, "|")
        turn += 1
        t7 += 1
        check()
 elif choice1 == '3.2' and c2 == '-' and t8 == 0:
        c2 = current_player
        print("|", a1, a2, a3, "|")
        print("|", b1, b2, b3, "|")
        print("|", c1, c2, c3, "|")
        turn += 1
        t8 += 1
        check()
 elif choice1 == '3.3' and c3 == '-' and t9 == 0:
        c3 = current_player
        print("|", a1, a2, a3, "|")
        print("|", b1, b2, b3, "|")
        print("|", c1, c2, c3, "|")
        turn += 1
        t9 += 1
        check()


 else:
  print("This cell is already taken or invalid input. Try again.")
  continue




