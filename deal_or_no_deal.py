import random
boxes = [.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]
random.shuffle(boxes)
#choose a box to keep
my_choice = int(input("Choose a box to keep 1 throuh 26\n"))
my_box = boxes.pop(my_choice - 1)
boxes_left = len(boxes)
game_over = False
#choose a box
for i in range(1,14):
    my_choice = int(input(f"Choose a box to get rid of: 1 through {boxes_left}\n"))
    f_box = "${:,}".format(boxes[my_choice-1])
    print(f"You got rid of {f_box} dollars\n")
    boxes.pop(my_choice - 1)
    boxes_left = len(boxes)    
    if i % 3 == 0:
#offer from bankers
        offer = sum(boxes) / len(boxes)
        f_offer = "${:,.2f}".format(offer)
        print("Ringggg, Ringgggg")
        print("We have a call from the bankers.")
        print(f"They have offered you {f_offer} for your case")
        acceptance = input("Do you accept? Type 'Deal' or 'No Deal'\n").lower()
        if acceptance == "no deal":
            print("No deal, let's keep playing!\n")
            continue
        elif acceptance == "deal":
            print(f"Congratulations! You won {f_offer}!")
            game_over = True
            break
        else: 
            print("Invalid choice")
#endgame
if not game_over:
    print(f"You have 12 boxes left.\nYou can keep your box or\nchoose to keep one of the twelve boxes left on the board.")
    my_choice = input("Which will you choose?\nTo keep your box type 'my box'.\nOtherwise type a number between '1' and '12'\n")
    if my_choice == "my box":
        if my_box > 1000: 
            print(f"Congratulations! You kept your original box and ended up with ${my_box}!")
        else:
            print(f"Well, you only ended up with ${my_box}.\nI guess you should have quit while you were ahead!")
    else:
        my_choice = int(my_choice)
        if boxes[my_choice - 1] > 1000: 
            print(f"Congratulations! You chose box {my_choice} and ended up with ${boxes[my_choice - 1]}!")
        else:
            print(f"Well, you only ended up with ${boxes[(my_choice - 1)]}.\nMaybe you should've trusted what was in your own box!")
