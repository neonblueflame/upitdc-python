"""
Programming in Business. Mark, a businessman, would like to 
purchase commodities necessary for his own sari-sari store. 
He would like to determine what commodity is the cheapest one 
for each type of products. You will help Mark by creating a 
program that processes a list of 5 strings. The format will 
be the name of the commodity plus its price (<name>-<price>).

Author: Sheena Dale Mariano
Date created: 20190830
"""

commodities = [
    "Sensodyne-100, Close Up-150, Colgate-135",
    "Safeguard-80, Protex-50, Kojic-135",
    "Surf-280, Ariel-350, Tide-635",
    "Clover-60, Piatos-20, Chippy-35",
    "Jelly bean-60, Hany-20, Starr-35"
]

def get_price(commodity):
    return int(commodity.split("-")[1])

def get_cheapest(commodities):
    cheapest = commodities[1]
    cheapest_price = get_price(commodities[1])
    
    for item in commodities:
        price = get_price(item)
        
        if price <= cheapest_price:
            cheapest_price = price
            cheapest = item
        
    return cheapest, cheapest_price

def get_cheapest_commodities(commodities):
    
    commodity_arr = []
    for commodity in commodities:
        commodity_arr.append(commodity)
    
    items_arr = []
    for commodity in commodity_arr:
        items_arr.append(commodity.split(", "))
    
    total_price = 0
    cheapest_commodities = []
    
    for items in items_arr:
        cheapest_item, cheapest_price = get_cheapest(items)
        total_price += int(cheapest_price)
        cheapest_commodities.append(cheapest_item)
    
    return total_price, cheapest_commodities

############################################################

for commodity in commodities:
    print(commodity)

print()
    
total, cheapest = get_cheapest_commodities(commodities)
print(f"Cheapest: { ', '.join(cheapest) }")
print(f"Total: { total }")
