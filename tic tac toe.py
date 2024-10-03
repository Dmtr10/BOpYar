a1 = 0
a2 = 0
a3 = 0
b1 = 0
b2 = 0
b3 = 0
c1 = 0
c2 = 0
c3 = 0
X = 'X'
O = 'O'

#тут алісія робить "меню гри", тобто 'велкам ту тік так тоу' і тд, + дизайнить хочаб якось вибір клітинки
while a1+a2+a3+b1+b2+b3+c1+c2+c2 != 9:
 choice = str(input(('Player 1 - which action? (example: 1.1)')))
 current_player = X
 if choice == '1.1' and a1 == 0:
   a1 = current_player
 elif choice == '1.2' and a2 == 0:
        a2 = current_player
 elif choice == '1.3' and a3 == 0:
        a3 = current_player
 elif choice == '2.1' and b1 == 0:
        b1 = current_player
 elif choice == '2.2' and b2 == 0:
        b2 = current_player
 elif choice == '2.3' and b3 == 0:
        b3 = current_player
 elif choice == '3.1' and c1 == 0:
        c1 = current_player
 elif choice == '3.2' and c2 == 0:
        c2 = current_player
 elif choice == '3.3' and c3 == 0:
        c3 = current_player
 else:
  print("This cell is already taken or invalid input. Try again.")
  continue

 choice1 = str(input(('Player 2 - which action? (example: 1.1)')))
 current_player = O
 if choice1 == '1.1' and a1 == 0:
   a1 = current_player
 elif choice1 == '1.2' and a2 == 0:
        a2 = current_player
 elif choice1 == '1.3' and a3 == 0:
        a3 = current_player
 elif choice1 == '2.1' and b1 == 0:
        b1 = current_player
 elif choice1 == '2.2' and b2 == 0:
        b2 = current_player
 elif choice1 == '2.3' and b3 == 0:
        b3 = current_player
 elif choice1 == '3.1' and c1 == 0:
        c1 = current_player
 elif choice1 == '3.2' and c2 == 0:
        c2 = current_player
 elif choice1 == '3.3' and c3 == 0:
        c3 = current_player
 else:
  print("This cell is already taken or invalid input. Try again.")
  continue

# всі іфи виконують займання клітинки, Макс треба дописати так щоб у ігровому полі ставився Х або О,
# Aлісія, зроби ігрове поле, board = [
#         [a1, a2, a3],
#         [b1, b2, b3],
#         [c1, c2, c3]
#     ] -- як приклад

