print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')

def find_highest():
  highest = 0
  for name in bid_dictionary:
    price = bid_dictionary[name]
    if price > highest:
      highest = name 
    print(f"The winner is {highest} with a bid of ${bid_dictionary[highest]}")


continue_bid = True
while continue_bid:
  bid_dictionary = {}
  name = input("What is your name?")
  bid = int(input("What is your bid price?"))
  bid_dictionary[name] = bid 
  choice = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if choice == "no":
    continue_bid = False
    find_hightest()
  

                

