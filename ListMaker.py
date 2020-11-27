import csv

print("""

 _       _________ _______ _________ _______  _______  _        _______  _______ 
( \      \__   __/(  ____ \\__   __/(       )(  ___  )| \    /\(  ____ \(  ____ )
| (         ) (   | (    \/   ) (   | () () || (   ) ||  \  / /| (    \/| (    )|
| |         | |   | (_____    | |   | || || || (___) ||  (_/ / | (__    | (____)|
| |         | |   (_____  )   | |   | |(_)| ||  ___  ||   _ (  |  __)   |     __)
| |         | |         ) |   | |   | |   | || (   ) ||  ( \ \ | (      | (\ (   
| (____/\___) (___/\____) |   | |   | )   ( || )   ( ||  /  \ \| (____/\| ) \ \__
(_______/\_______/\_______)   )_(   |/     \||/     \||_/    \/(_______/|/   \__/
                                                                                 
 ______              _        _______ __________________                         
(  ___ \ |\     /|  ( (    /|(  ___  )\__    _/\__   __/                         
| (   ) )( \   / )  |  \  ( || (   ) |   )  (     ) (                            
| (__/ /  \ (_) /   |   \ | || (___) |   |  |     | |                            
|  __ (    \   /    | (\ \) ||  ___  |   |  |     | |                            
| (  \ \    ) (     | | \   || (   ) |   |  |     | |                            
| )___) )   | |     | )  \  || )   ( ||\_)  )  ___) (___                         
|/ \___/    \_/     |/    )_)|/     \|(____/   \_______/                         
                                                                                 

""")

print("\n")

list = []
print(f"""
Welcome to make your own list!

You can add things to your list by typing, "append"
You can remove items by typing, "pop"

So far your list has {len(list)} items.
""")

print("\n")

Input = input('Type "append" if you want to add an item or type "pop" to remove an item. ')
#Function to append an item. Uses the ItemAdd input if you type append for the Input input (lol)
def Add(ItemAdd):
	list.append(ItemAdd)
#Function to remove an item. Uses the ItemRemove input if you type pop for the Input input
def Remove(ItemRemove):
	list.pop(int(ItemRemove))
#Function to prompt user for the item to append. Gives a decision to append, pop or put list into a file.
def AddLoop():
	ItemAdd = input("What item do you want to append?: ")
	Add(ItemAdd)
	print(list)
	print("\n")
	print(f"Your list so far has {len(list)} item(s) on it. Would you like to continue adding or removing from your list or save it to a file? Press A to append, press P to remove an item or press F to save your list to a file. ")
	Decision = input("")
	if (Decision == "A") or (Decision == "a"):
		AddLoop()
	elif (Decision == "P") or (Decision == "p"):
		RemoveLoop()
	elif (Decision == "F") or (Decision == "f"):
		with open("ListOfItems.csv", "w") as f:
			writer = csv.writer(f)
			writer.writerows(list)
	else:
		print("Something went wrong, try again.")
#Function to prompt user for the item to remove. Gives a decision to append, pop or put list into a file.
def RemoveLoop():
	ItemRemove = input("What item do you want to remove? (Type in the number that the item is in the list): ")
	Remove(ItemRemove)
	print(list)
	print("\n")
	print(f"Your list so far has {len(list)} item(s) on it. Would you like to continue adding or removing from your list or save it to a file? Press A to append, press P to remove an item or press F to save your list to a file. ")
	Decision = input("")
	if (Decision == "A") or (Decision == "a"):
		AddLoop()
	elif (Decision == "P") or (Decision == "p"):
		RemoveLoop()
	elif (Decision == "F") or (Decision == "f"):
		with open("ListOfItems.csv", "w") as f:
			writer = csv.writer(f)
			writer.writerows(list)
	else:
		print("Something went wrong, try again.")

#Main loop, if original Input input equals append or pop it'll move to that function.	
while True:
	if (Input == "append") or (Input == "Append"):
		AddLoop()
		break
	elif (Input == "Pop") or (Input == "pop"):
		RemoveLoop()
		break
	else:
		print("Something went wrong, please try again.")
		break
