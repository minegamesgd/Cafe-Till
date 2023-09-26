bun = 0
coffee = 0
cake = 0
sandwich = 0
dessert = 0
repeat = "true"
while repeat == "true":
    order = input("ENTER ITEM: ")

    if order == "bun":
        bun=bun+1
    if order == "coffee":
        coffee=coffee+1
    if order == "cake":
        cake=cake+1
    if order == "sandwich":
        sandwich=sandwich+1
    if order == "dessert":
        dessert=dessert+1



    if order == "end" or order== "END":
        repeat = "false"


print("You have a total of",bun,"buns ordered")
print("You have a total of",coffee,"coffee ordered")
print("You have a total of",cake,"cake ordered")
print("You have a total of",sandwich,"sandwich ordered")
print("You have a total of",dessert,"desserts ordered")

    
