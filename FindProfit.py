'''You work for a manufacturer, and have been asked to calculate the total profit made on the sales of a product. You can prepare a dictionary containing the cost price per unit (in INR), sell price per unit (in INR), and the starting inventory. Return the total profit made, rounded to the nearest INR Examlpe dictionary ] total_profit({ "cost_price": 32.67, "sell_price": 45.00, "inventory": 1200 }'''
def findProf(dict):
    profit =(dict["sell_price"]*dict["inventory"])-(dict["cost_price"]*dict["inventory"])
    return profit

total_profit = { "cost_price": 32.67, "sell_price": 45.00, "inventory": 1200 }

print(findProf(total_profit))
