import random

class Gamebot:

    def __init__(self, play_hand, stack):
        self.play_hand = play_hand                  # a reference to the player's hand
        self.stack = stack                          # a reference to the stack
        self.count_deck = [['b',1],['b',1],['b',1],['b',2], # a list to count the remaining
                           ['b',2],['b',3],['b',3],['b',4], # cards in the deck
                           ['w',1],['w',1],['w',1],['w',2],
                           ['w',2],['w',3],['w',3],['w',4]]
        for card in play_hand:                      # bot has already seen the player's hand,so it knows
            self.update_count_deck(card)            # that those cards are not in the deck anymore.
        self.hand = [['!',-1],['!',-1],['!',-1]]    # bot's hand. '!' indicates unknown color,
                                                    # -1 indicates unknown value

    def get_tip(self, tip):
        self.tip=tip
        tip_side=self.tip[:-1]
        tip_=self.tip[-1]
        if tip_!="w":
          if tip_!="b":
            tip_=int(tip_)
          else:
            tip_="b"
        else:
          tip_="w"    
        count=0
        for i in tip_side:
          if count%2==0:
            if tip_=="w":
              self.hand[int(i)-1][0]=tip_
            elif tip_=="b":
              self.hand[int(i)-1][0]=tip_
            else:
              self.hand[int(i)-1][1]=tip_
          count+=1
        # input: tip: a string entered by the player in the form of "loc1,loc2*,loc3*,tip"
        # where * indicates optionality and tip is either a value or a color.
        # e.g. "1,2,w" or "2,3" or "1,2,3,2"
        # output: none
        # The tip is processed and the information about the bot's hand is updated.
        

    def update_count_deck(self,card):
        self.card=card
        self.count_deck.remove(card)
        # input: card to be removed
        # output: none
        # card is removed from the count_deck of the bot.
        

    def update_hand(self,num):
        self.num=num
        if len(self.count_deck)>0:
          self.hand[self.num]=['!',-1]
          self.count_deck.pop(0)
        else:
          self.hand.pop(self.num)

        # input: num: location of the card to be removed from the bot's hand
        # output: none
        # A card is removed from the bot's hand according to the given input and a new one is appended.


    def give_tip(self):
        count_for_1=0
        count_for_2=0
        count_for_3=0
        count_for_4=0
        count_for_w=0
        count_for_b=0
        indexes_for_1=[]
        indexes_for_2=[]
        indexes_for_3=[]
        indexes_for_4=[]
        indexes_for_w=[]
        indexes_for_b=[]
        count=0
        for card in play_hand:
          if card[0]=="w":
            count_for_w+=1
            indexes_for_w.append(count+1)
          elif card[0]=="b":
            count_for_b+=1
            indexes_for_b.append(count+1)
          if card[1]==1:
            count_for_1+=1
            indexes_for_1.append(count+1)
          elif card[1]==2:
            count_for_2+=1
            indexes_for_2.append(count+1)
          elif card[1]==3:
            count_for_3+=1
            indexes_for_3.append(count+1)
          elif card[1]==4:
            count_for_4+=1
            indexes_for_4.append(count+1)
          count+=1
        shown_tip=max(count_for_1,count_for_2,count_for_3,count_for_w,count_for_b)
        if shown_tip==count_for_1:
          indexes_for_1=str(indexes_for_1)
          print(indexes_for_1[1:len(indexes_for_1)-1],",",1)
        elif shown_tip==count_for_2:
          indexes_for_2=str(indexes_for_2)
          print(indexes_for_2[1:len(indexes_for_2)-1],",",2)
        elif shown_tip==count_for_3:
          indexes_for_3=str(indexes_for_3)
          print(indexes_for_3[1:len(indexes_for_3)-1],",",3)
        elif shown_tip==count_for_4:
          indexes_for_4=str(indexes_for_4)
          print(indexes_for_4[1:len(indexes_for_4)-1],",",4)
        elif shown_tip==count_for_w:
          indexes_for_w=str(indexes_for_w)
          print(indexes_for_w[1:len(indexes_for_w)-1],",","w")
        elif shown_tip==count_for_b:
          indexes_for_b=str(indexes_for_b)
          print(indexes_for_b[1:len(indexes_for_b)-1],",","b")
        # input: none
        # output: a string created by the bot in the form of "loc1,loc2*,loc3*,tip"
        # where * indicates optionality and tip is either a value or a color.
        # e.g. "1,2,w" or "2,3" or "1,2,3,2"
        # The bot checks the player's hand and finds a good tip to give. Minimal requirement for this
        # function is that bot gives the tip for maximum possible number of cards.
        # BONUS: Smarter decision-making algorithms can be implemented.

    def pick_stack(self):
        if self.stack[0]==[] and self.stack[1]==[] and ['!',1] in self.hand:
          return self.hand.index(['!',1]) 
        elif self.stack[0]==[] and ['b',1] in self.hand:
          return self.hand.index(['b',1])
        elif self.stack[0]==[['b',1]] and ['b',2] in self.hand:
          return self.hand.index(['b',2])
        elif self.stack[0]==[['b',1],['b',2]] and ['b',3] in self.hand:
          return self.hand.index(['b',3])
        elif self.stack[0]==[['b',1],['b',2],['b',3]] and ['b',4] in self.hand:
          return self.hand.index(['b',4])
        elif self.stack[1]==[] and ['w',1] in self.hand:
          return self.hand.index(['w',1])
        elif self.stack[1]==[['w',1]] and ['w',2] in self.hand:
          return self.hand.index(['w',2])
        elif self.stack[1]==[['w',1],['w',2]] and ['w',3] in self.hand:
          return self.hand.index(['w',3])
        elif self.stack[1]==[['w',1],['w',2],['w',3]] and ['w',4] in self.hand:
          return self.hand.index(['w',4])
        else:
          return -1
        # input: none
        # output: If possible, the location of the card to be placed in the stack, otherwise -1. Minimal
        # the requirement for this function is to find the card to be stacked with 100% certainty.
        # BONUS: Smarter decision-making algorithms can be implemented.
        
    def pick_discard(self):
      unknown_counter=[]
      for i in self.hand:
        if i in stack[0] or i in stack[1]:
          unknown_counter.append(3)
        elif i[0]=="!" and i[1]==-1:
          unknown_counter.append(2)
        elif i[0]=="!" or i[1]==-1:
          unknown_counter.append(1)
        else:
          unknown_counter.append(0)
      will_be_discarded=max(unknown_counter)
      return unknown_counter.index(will_be_discarded)
        # input: none
        # output: The location of the card to be discarded. Minimal requirement for this function is that,
        # if possible, the bot picks the card that is already in the stack. If this is not the case,
        # the bot picks the card of which it has minimum information.
        # BONUS: Smarter decision-making algorithms can be implemented.

def shuffle(deck):
  x=len(deck)
  for i in range(x):
    y=random.randint(0,x-1)
    z=deck[y]
    deck.append(z)
    deck.remove(z)
  #I shuffled the list for x times(the length of deck). My algorithm first generates a #random number in range x, then finds the element at index deck[x]. Appends it to the #end of the list and removes same element from the list so that it will be shuffled.

    # input: deck to be shuffled
    # output: none
    # shuffle the deck
    # you are free to choose the algorithm you want
    # explain your shuffle algorithm in a comment
    


def print_menu():
    print("Hit 'v' to view the status of the game.")
    print("Hit 't' to spend a tip.")
    print("Hit 's' to try and stack your card.")
    print("Hit 'd' to discard your card and earn a tip.")
    print("Hit 'h' to view this menu.")
    print("Hit 'q' to quit.")

def update_hand(hand,deck,num):
    print("Removed card:",hand[num])
    if len(deck)>0:
      hand[num]=deck[0]
      deck.pop(0)
    else:
      hand.pop(num)
    # input: hand to be updated,current deck and the location of the card to be removed
    # output: removed card
    # This function is called when a card is played (either stacked or discarded). It removes
    # the played card from the hand. If there are any cards left in the deck, the top card
    # in the deck is drawn and appended to the hand.
    

def try_stack(card,stack,trash,lives):
    if card[0]=='b':
      if len(stack[0])==0:
        if card!=['b',1]:
          trash.append(card)
          lives=lives-1
          return lives
        else:
          stack[0].append(card)
          return lives
      elif stack[0]==[['b',1]]:
        if card!=['b',2]:
          trash.append(card)
          lives=lives-1
          return lives
        else:
          stack[0].append(card)
          return lives
      elif stack[0]==[['b',1],['b',2]]:
        if card!=['b',3]:
          trash.append(card)
          lives=lives-1
          return lives
        else:
          stack[0].append(card)
          return lives
      elif stack[0]==[['b',1],['b',2],['b',3]]:
        if card!=['b',4]:
          trash.append(card)
          lives=lives-1
          return lives
        else:
          stack[0].append(card)
          return lives
      else:
        trash.append(card)
        lives=lives-1
        return lives
    elif card[0]=='w':
      if len(stack[1])==0:
        if card!=['w',1]:
          trash.append(card)
          lives=lives-1
          return lives
        else:
          stack[1].append(card)
          return lives
      if stack[1]==[['w',1]]:
        if card!=['w',2]:
          trash.append(card)
          lives=lives-1
          return lives
        else:
          stack[1].append(card)
          return lives
      if stack[1]==[['w',1],['w',2]]:
        if card!=['w',3]:
          trash.append(card)
          lives=lives-1
          return lives
        else:
          stack[1].append(card)
          return lives
      if stack[1]==[['w',1],['w',2],['w',3]]:
        if card!=['w',4]:
          trash.append(card)
          lives=lives-1
          return lives
        else:
          stack[1].append(card)
          return lives
      else:
        trash.append(card)
        lives=lives-1
        return lives
    # input: the card to be stacked, current stack, current trash, number of lives
    # output: updated number of lives
    # This function tries to place the card in the stack. If successful, the card is appropriately
    # added to the stack and the updated stack is printed. Otherwise, the card is appended to the
    # trash, the trash is sorted for better viewing and number of lives is decreased by 1. A warning
    # and the current number of lives are printed.
    

def discard(card,trash,tips):
    trash.append(card)
    trash=sorted(trash)
    print("Trash:",trash)
    return tips+1
    # input: the card to be discarded, the current trash, number of tips
    # output: updated number of tips
    # This function appends the card to the trash, re-sorts it and increases the number of tips by 1.
    # The updated trash and the number of tips are printed.
    

print("Welcome! Let's play!")
print_menu()
deck = [['b',1],['b',1],['b',1],['b',2],['b',2],['b',3],['b',3],['b',4],
        ['w',1],['w',1],['w',1],['w',2],['w',2],['w',3],['w',3],['w',4]]
stack = [[],[]] #0 means black, 1 means white
trash = []
lives = 2
tips = 3
shuffle(deck)
# First hands are dealt.
comp_hand = deck[0:3]
play_hand = deck[3:6]
del deck[0:6]
bot = Gamebot(play_hand,stack)  # Gamebot object is created.
turn = 0                        # 0 means player, 1 means computer. So for each game, the player starts.
while True:
    if turn == 0:
        inp = input("Your turn:")
        if inp == 'v':
            print("Computer's hand:", comp_hand)
            print("Number of tips left:", tips)
            print("Number of lives left:", lives)
            print("Current stack:")
            print("Black:", stack[0])
            print("White:", stack[1])
            print("Current trash:", trash)
        elif inp == "t":
            if tips > 0:
                turn = 1        # Switch turns.
                # Take a tip from the player, give it to the bot, update and print the number of tips.
                give_tip_to_bot=input("Give tip:")
                bot.get_tip(give_tip_to_bot)
                tips=tips-1
                print("Remaining tips:",tips)
                
            else:
                print("Not possible! No tips left!")
        elif inp == "s":
            turn = 1        # Switch turns.
            # Take the location of the card to be stacked from the player,
            # update hands and bot's count_deck and try to stack the selected card.
            print("Which card do you want to stack? You have",len(play_hand),"cards left.")
            location=int(input("Enter card number:"))
            card=play_hand[location-1]
            lives=try_stack(card,stack,trash,lives)
            update_hand(play_hand,deck,location-1)
            print("Remaining lives:",lives)
            print("Stack:",stack)
            
        elif inp == "d":
            turn = 1        # Switch turns.
            # Take the location of the card to be discarded from the player,
            # update hands and bot's count_deck and discard the selected card.
            print("Which card do you want to discard? You have",len(play_hand),"cards left.")
            location=int(input("Enter card number:"))
            card=play_hand[location-1]
            update_hand(play_hand,deck,location-1)
            tips=discard(card,trash,tips)
            
        elif inp == "h":
            print_menu()
        elif inp == "q":
            break
        else:
            print("Please enter a valid choice (v,t,s,d,h,q)!")
    else:
        # A minimal strategy of the bot is given.
        # BONUS: Smarter rule sets can be implemented.
        if tips > 1  and len(play_hand)>0:
            # Take a tip from the bot. Update the number of tips. Print both
            # the given tip by the bot and the updated number of tips.
                bot.give_tip()
                tips=tips-1
                print("Remaining tips:",tips)
        else:
          if bot.pick_stack()!=-1:
            num=bot.pick_stack()
            lives=try_stack(comp_hand[num],stack,trash,lives)
            update_hand(comp_hand,deck,num)
            bot.update_hand(bot.pick_stack())
          else:
            tips=discard(comp_hand[bot.pick_discard()],trash,tips)
            print("Remaining tips:",tips)
            update_hand(comp_hand,deck,bot.pick_discard())
            bot.update_hand(bot.pick_discard())
            # Check if bot can pick a card to stack.
            # If yes, update comp_hand, bot's hand and bot's count_deck and try to stack the selected card.
            # If no, make bot pick a card to discard. Update comp_hand, bot's hand and bot's count_deck
            # and discard the selected card.
            
        turn = 0        # Switch turns.
    score = sum([len(d) for d in stack])
    if lives==0:
        print("No lives left! Game over!")
        print("Your score is", score)
        break
    if len(comp_hand+play_hand)==0:
        print("No cards left! Game over!")
        print("Your score is", score)
        break
    if score == 8:
        print("Congratulations! You have reached the maximum score!")
        break

