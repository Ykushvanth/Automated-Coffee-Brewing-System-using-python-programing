def total_income(total_income_value,rupees,price):
    if(rupees == price):
        total_income_value += rupees
    else:
        value = rupees - price
        print("The refund amount:"+str(value))
        total_income_value += price
    return total_income_value
    


def make_coffee(total_income_value,coffe_beens_req,water_req,coffe_beens,water,milk,milk_req,Price):
    if(coffe_beens >= coffe_beens_req and water >=water_req and ((milk_req == 0) or (milk >= milk_req and milk_req !=0))):
        coffe_price=Price
        print("price:"+str(coffe_price))
        rupeesss = "enter an amount:"
        print(rupeesss)
        rupees =int(input())
        if(rupees >= coffe_price):
            value = total_income(total_income_value,rupees,Price)
            coffe_beens = coffe_beens - coffe_beens_req
            water = water - water_req
            milk -= milk_req
            print("Your coffee is ready!")
            print("------------------------")
        else:
            print("Sorry insufficient money")
    else:
        print("Sorry insufficient resources")
    return coffe_beens,water,value,milk

Dictionary={"Espresso":({"coffe_beens":10,"water":1.5,"milk":0,"price":20}),"Americano":({"coffe_beens":14,"water":2,"milk":12,"price":30})}
total_income_value=0
coffe_beens = 50
water =200
milk=100
i=1
while i >0:
    print("Hello,Select your coffee")
    List=["1.Espresso","2.Americano","3.Check_Income","4.Check_resourse","5.Exit"]
    for i in List:
        print(i)
    user_input = input()
    if(user_input == "1"):
        Value = Dictionary["Espresso"]
        coffe_beens_req = Value["coffe_beens"]
        water_req = Value["water"]
        milk_req =Value["milk"]
        Price=Value["price"]
        Operation=make_coffee(total_income_value,coffe_beens_req,water_req,coffe_beens,water,milk,milk_req,Price)
        coffe_beens_rem,water_rem,money_received,milk_rem= Operation
        total_income_value = money_received
        coffe_beens = coffe_beens_rem
        water = water_rem
        milk = milk_rem
    if(user_input == "2"):
        Value = Dictionary["Americano"]
        coffe_beens_req = Value["coffe_beens"]
        water_req = Value["water"]
        milk_req=Value["milk"]
        Price=Value["price"]
        Operation=make_coffee(total_income_value,coffe_beens_req,water_req,coffe_beens,water,milk,milk_req,Price)
        coffe_beens_rem,water_rem,money_received,milk_rem= Operation
        total_income_value = money_received
        coffe_beens = coffe_beens_rem
        water = water_rem
        milk = milk_rem
    if(user_input == "3"):
        print("Todays income is:"+str(total_income_value))
        print("-----------------------------------------")
    if(user_input == "4"):
        print("water:"+str(water))
        print("coffee_beens:"+str(coffe_beens))
        print("Milk:"+str(milk))
        print("----------------------")
    if(user_input == "5"):
        print("No more orders taking")
        break
    
    i=1
