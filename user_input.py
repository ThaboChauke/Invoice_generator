
import questionary as qs


company_details = """
King Hardware\n
123 Anywhere Street\n
City/State/Zip,Post code\n
"""
contact_details = """0123456789
king@co.business.co.za"""

list_of_products = ["steel beams", "planks", "tiles","pipes","cables"]



def price_calculation(item,quantity):
    prices = {"steel beams" : 200, "planks": 100,
           "tiles" : 50,"pipes" : 40
           ,"cables" : 150}
    price = prices[item]
    total_price = price * quantity
    return price,total_price


def vat_calculation(item):
    vat_percentage = 0.15
    return item * vat_percentage


def collect_info():
    client_data = {}
    client = qs.text("Name of client: ").ask()
    client_data["Name"] = client
    print()
    
    number = int(qs.text("how many items: ").ask())
    for i in range(number):
        items = qs.select("Select product: ", choices=list_of_products).ask()
        quantity = int(qs.text(f"How many {items}: ").ask())
        unit_price,gross_total_price = price_calculation(items,quantity)
        print()
        
        discount = qs.confirm("Discount? ").ask()
        if discount:
            discount_amount = int(qs.text("How much:").ask())
            print()
            price_after_discount = gross_total_price - discount_amount
            vat = qs.confirm("Is VAT charged: ").ask()
            if vat:
                vat_price = vat_calculation(price_after_discount)
                net_total = price_after_discount + vat_price
            else:
                vat_price = 0
            client_data[f"item_{i}"] = {"item":items,"quantity":quantity,
                                        "unit price":unit_price,"sub total":gross_total_price,
                                        "discount":discount_amount,"vat":vat_price,"total":net_total}
        else:
            discount_amount = 0
            vat = qs.confirm("Is VAT charged: ").ask()
            if vat:
                vat_price = vat_calculation(gross_total_price)
                net_total = gross_total_price + vat_price
            else:
                vat_price = 0
                net_total = gross_total_price - vat_price
            client_data[f"item_{i}"] = {"item":items,"quantity":quantity,
                                        "unit price":unit_price,"subtotal":gross_total_price,
                                        "discount":discount_amount,"vat":vat_price,"total":net_total}

    return client_data


print(collect_info())
# print(company_details)