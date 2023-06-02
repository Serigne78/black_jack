import random



cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

users = []
computers = []

end = False
while end == False:
       descision = input("Type y if yant play or n if you dont wanna play: ")
       if descision == "y":
              users.append(cards[random.randint(0, len(cards)-1)])
              users.append(cards[random.randint(0, len(cards)-1)])
              
              computers.append(cards[random.randint(0, len(cards)-1)])
              
              for computer in computers:
                     result_computer = sum(computers) 

              for user in users:
                     result_user = sum(users)
              
              print(f"Your cards: {users}, current score: {result_user}")
              print(f"Computer's first card: {computers[0]}")
              pioche ="y"
              while pioche == "y":
                     pioche = input("Type 'y' to get another card, type 'n' to pass : ")
                     if pioche ==  "y":
                            users.append(cards[random.randint(0, len(cards) -1)])
                            computers.append(cards[random.randint(0, len(cards) -1)])

                            for computer in computers:
                                   result_computer = sum(computers) 
                            
                            for user in users:
                                   result_user = sum(users)
                            if result_user > 21:
                                   print("computer win")
                                   break
                            if result_computer > 21:
                                   print("user loose")
                                   break
                            print(f"Your cards: {users}, final score: {result_user}")
                            print(f"Computer's first hand:{computers},final score {result_computer}")
                            
                          
                            
                            
                     else:
                            computers.append(cards[random.randint(0, len(cards)-1)])
                            
                            for computer in computers:
                                   result_computer = sum(computers) 
                                   
                                  

                            if result_user > result_computer :
                                   print(f"You win the user have {result_user} gg user")
                                   if result_user > 21:
                                          print("user loose")
                                          break
                            
                            if result_user < result_computer:
                                   print(f"computer win have {result_computer} gg computer ")
                                   break
                                   if result_computer > 21:
                                          print("computer loose")
                                          break  

                            if result_user == result_computer:
                                   print(f"Equal user = {result_user} and computer = {result_computer}")
                                   break

                     end = True
              end = True
