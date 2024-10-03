a1 = None
a2 = None
a3 = None
b1 = None
b2 = None
b3 = None
c1 = None
c2 = None
c3 = None
X = 'X'
O = 'O'
turn = 0
#тут алісія робить "меню гри", тобто 'велкам ту тік так тоу' і тд, + дизайнить хочаб якось вибір клітинки
while turn != 9:
 choice = str(input(('Player 1 - which action? (example: 1.1)')))
 current_player = X
 if choice == '1.1' and a1 == None:
   a1 = current_player
   print("|", a1, a2, a3, "|")
   print("|", b1, b2, b3, "|")
   print("|", c1, c2, c3, "|")
   turn += 1
 elif choice == '1.2' and a2 == None:
        a2 = current_player
        print("|", a1, a2, a3, "|")
        print("|", b1, b2, b3, "|")
        print("|", c1, c2, c3, "|")
        turn += 1
 elif choice == '1.3' and a3 == None:
        a3 = current_player
        print("|", a1, a2, a3, "|")
        print("|", b1, b2, b3, "|")
        print("|", c1, c2, c3, "|")
        turn += 1
 elif choice == '2.1' and b1 == None:
        b1 = current_player
        print("|", a1, a2, a3, "|")
        print("|", b1, b2, b3, "|")
        print("|", c1, c2, c3, "|")
        turn += 1
 elif choice == '2.2' and b2 == None:
        b2 = current_player
        print("|", a1, a2, a3, "|")
        print("|", b1, b2, b3, "|")
        print("|", c1, c2, c3, "|")
        turn += 1
 elif choice == '2.3' and b3 == None:
        b3 = current_player
        print("|", a1, a2, a3, "|")
        print("|", b1, b2, b3, "|")
        print("|", c1, c2, c3, "|")
        turn += 1
 elif choice == '3.1' and c1 == None:
        c1 = current_player
        print("|", a1, a2, a3, "|")
        print("|", b1, b2, b3, "|")
        print("|", c1, c2, c3, "|")
        turn += 1
 elif choice == '3.2' and c2 == None:
        c2 = current_player
        print("|", a1, a2, a3, "|")
        print("|", b1, b2, b3, "|")
        print("|", c1, c2, c3, "|")
        turn += 1
 elif choice == '3.3' and c3 == None:
        c3 = current_player
        print("|", a1, a2, a3, "|")
        print("|", b1, b2, b3, "|")
        print("|", c1, c2, c3, "|")
        turn += 1
 else:
  print("This cell is already taken or invalid input. Try again.")
  continue

 choice1 = str(input(('Player 2 - which action? (example: 1.1)')))
 current_player = O
 if choice1 == '1.1' and a1 == None:
   a1 = current_player
   print("|", a1, a2, a3, "|")
   print("|", b1, b2, b3, "|")
   print("|", c1, c2, c3, "|")
   turn += 1
 elif choice1 == '1.2' and a2 == None:
        a2 = current_player
        print("|", a1, a2, a3, "|")
        print("|", b1, b2, b3, "|")
        print("|", c1, c2, c3, "|")
        turn += 1
 elif choice1 == '1.3' and a3 == None:
        a3 = current_player
        print("|", a1, a2, a3, "|")
        print("|", b1, b2, b3, "|")
        print("|", c1, c2, c3, "|")
        turn += 1
 elif choice1 == '2.1' and b1 == None:
        b1 = current_player
        print("|", a1, a2, a3, "|")
        print("|", b1, b2, b3, "|")
        print("|", c1, c2, c3, "|")
        turn += 1
 elif choice1 == '2.2' and b2 == None:
        b2 = current_player
        print("|", a1, a2, a3, "|")
        print("|", b1, b2, b3, "|")
        print("|", c1, c2, c3, "|")
        turn += 1
 elif choice1 == '2.3' and b3 == None:
        b3 = current_player
        print("|", a1, a2, a3, "|")
        print("|", b1, b2, b3, "|")
        print("|", c1, c2, c3, "|")
        turn += 1
 elif choice1 == '3.1' and c1 == None:
        c1 = current_player
        print("|", a1, a2, a3, "|")
        print("|", b1, b2, b3, "|")
        print("|", c1, c2, c3, "|")
        turn += 1
 elif choice1 == '3.2' and c2 == None:
        c2 = current_player
        print("|", a1, a2, a3, "|")
        print("|", b1, b2, b3, "|")
        print("|", c1, c2, c3, "|")
        turn += 1
 elif choice1 == '3.3' and c3 == None:
        c3 = current_player
        print("|", a1, a2, a3, "|")
        print("|", b1, b2, b3, "|")
        print("|", c1, c2, c3, "|")
        turn += 1
 else:
  print("This cell is already taken or invalid input. Try again.")
  continue

# всі іфи виконують займання клітинки, Макс треба дописати так щоб у ігровому полі ставився Х або О,
# Aлісія, зроби ігрове поле, board = [
#         [a1, a2, a3],
#         [b1, b2, b3],
#         [c1, c2, c3]
#     ] -- як приклад

