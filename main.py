print ("Welcome to Treasure Island.\nYour mission is to find the treasure")
cross_road = input("You are at a cross road. Where do you want to go.Type 'left' or 'right'\n")
if cross_road == "left":
  print ("\nYou have come to a lake. There is an island in the middle of the lake.")
  lake  = input ("Type  'wait' to wait for a boat. Type 'swim' to swimm across\n")
  if lake == "wait":
    print ("\nYou arrive at the island safely. Now there is a house with 3 doors. One red, one yellow and one blue.")
    door = input ("which color door will you chose to get the treasure ?\nType 'red' or 'yellow' or 'blue'\n")
    if door == "red":
      print ("\nYou have entered to room of fire.You are burned by fire. GAME OVER!")
    elif door == "blue":
      print ("\nYou have entered to a room of beasts. You are eaten by beasts. GAME OVER!")
    else:
      print ("\nYou have found the treasure. YOU WIN !")
  else:
    print ("\nYou have been attacked by trout. GAME OVER !")
else:
  print ("\nYou fell into a hole. GAME OVER !")
