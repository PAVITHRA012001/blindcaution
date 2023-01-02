#from replit import clear

print(
    '''  |\                     /)
 /\_\\__               (_//
|   `>\-`     _._       //`)
 \ /` \\  _.-`:::`-._  //
  `    \|`    :::    `|/
        |     :::     |
        |.....:::.....|
        |:::::::::::::|
        |     :::     |
        \     :::     /
         \    :::    /
          `-. ::: .-'
   jgs     //`:::`\\
          //   '   \\
         |/         \\'''
)
list_of_bid={}
highest_bid=0
run=True
while run==True:
    name_of_the_player=input("Enter the name of the player: ")
    bid_price = int(input("enter the price: "))
    list_of_bid[name_of_the_player]=bid_price
    print(list_of_bid)
    user=input("Is there is naother user yes or no :").lower()
    if user=='yes':
        pass
    else:
        run=False
winner=""
for thing in list_of_bid:
    if list_of_bid[thing]>highest_bid:
        highest_bid=list_of_bid[thing]
        winner=thing
    else:
        pass

print(f"{highest_bid} is the {winner}")
