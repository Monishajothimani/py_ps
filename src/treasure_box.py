
#treasure box#

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
choice = input("you are at the cross road, where you want to go? Left or Right ?" )

LEFT = "Left".lower()
RIGHT="Right".lower()

if(choice == LEFT):
  print(" you reached escape door")
  color = input("which door you will choose? Blue or Yellow?")
  BLUE = "Blue".lower()
  YELLOW ="Yellow".lower()
  if(color == YELLOW):
    print(" you reached open space")
    place = input("which path you choose? River or Cave? ")
    RIVER = "River".lower()
    CAVE ="Cave".lower()
    if(place == RIVER):
      print("you landed on the island"),
      girls = input("there are two girls, which one you choose? White or Black?")
      WHITE = "White".lower()
      BLACK = "Black".lower()
      if(girls == WHITE):
        print("she is your guard")
        home = input("we reached the house,there are boxes.which one you want? Brown or Orange?")
        BROWN = "Brown".lower()
        ORANGE = "Orange".lower()
        if(home == BROWN):
          print("you won")
        else:
          print("game over - attacked by snake")
      else:
        print("game over - she is the killer ")
    else:
      print("game over - you killed by Lion")
  else:
    print("game over - you killed by toxic gas")
else:
  print("game over - you are attacked")

# if(choice == RIGHT):
  