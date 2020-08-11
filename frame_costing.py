import time

print("Welcome to Furniture Frame Pricing Module v 0.1")
time.sleep(1)
print("First Enter Nesting Information")
time.sleep(1)
one_whole = int(input("1 qty Whole "))
one_fraction = int(input("1 qty Fraction "))
one_of = int(input("of? "))
five_whole = int(input("5 qty Whole "))
five_fraction = int(input("5 qty Fraction "))
five_of = int(input("? "))
ten_whole = int(input("10 qty Whole "))
ten_fraction = int(input("10 qty Fraction "))
ten_of = int(input("of? "))

def frame_yield(whole,fraction,direction,qty):
    if direction == 96:
        sheets = whole + (fraction / direction)
        ply_yield = qty / sheets
        return ply_yield
    elif direction == 45:
        sheets = whole + ((48 - fraction) / direction)
        ply_yield = qty / sheets
        return ply_yield


def hardwood(qty, length, width):
    footage = (length * width) / 144
    with_waste = footage * 1.6
    total_footage = with_waste * qty
    return total_footage

one_yield = frame_yield(one_whole, one_fraction, one_of, 1)
five_yield = frame_yield(five_whole, five_fraction, five_of, 5)
ten_yield = frame_yield(ten_whole, ten_fraction, ten_of, 10)

average_yield = (one_yield + five_yield + ten_yield) / 3

footage = (1 / average_yield) * 32

ply_cost = float(input("how much per sq ft? "))

ply_price = ply_cost * footage

hdwd = []

while True:
    print("enter Qty")
    qty = input()
    if qty == '':
        break
    print("enter Length")
    length = input()
    if length == '':
        break
    print("Enter Width (1 3/4, 2 7/8, or 1 5/8)")
    width = input()
    if width == '':
        break
    footage = ((float(length) * float(width))/ 144)
    waste_factor = 1.6
    footage_withwaste = footage * waste_factor
    total_footage = footage_withwaste * float(qty)
    hdwd = hdwd + [total_footage]

total_hdwd_footage = sum(hdwd)

print("Price per sq ft? ")
hdwd_price = input()



hdwd_total_price = float(hdwd_price) * total_hdwd_footage



print("KD or Assembled? ")

assembly = input()
kup_pay = 0
sup_pay = 0

if assembly == "KD":
    pass
elif assembly == "Assembled":
    print("How much for Knock up?")
    kup_pay = input()
    print("How much for Sprint Up? ")
    sup_pay = input()

machine_room_labor = (total_hdwd_footage * .27) + (footage * .09)

matlab = hdwd_total_price + ply_price + float(kup_pay) + float(sup_pay) + float(machine_room_labor)



print("Overhad Factor? Profit Margin? ")

oh_factor = input()
margin = input()

cost_of_goods_sold = (matlab * (1 + float(oh_factor)))



quote = round((cost_of_goods_sold * (1 + float(margin))), 2)


time.sleep(1)
print("Total hardwood footage: " + str(total_hdwd_footage))
time.sleep(1)
print("Average plywood footage: " + str(average_yield))
time.sleep(1)
print("The cost for Plywood for this frame will be: $" 
    + str(round(ply_price, 2)) + "with a total hdwd price of " + str(round(hdwd_total_price, 2)))
time.sleep(1)
print("Total Materials and Labor for this frame: $" + str(matlab))
time.sleep(1)
print("Cost of Goods Sold: " + str(cost_of_goods_sold))
print("Your quote is: $" + str(quote))

print("Save as? ")

filename = input()

frame_file = open(filename+".txt","w+")

frame_file.write( "Total Hardwood Footage: " + str(total_hdwd_footage) + "\n"
                    + "Average Plywood Footage: " + str(average_yield) + "\n"
                    + "The cost of plywood for this frame will be: $" + str(round(ply_price, 2)) + "\n"
                    + "With a total hardwood price of " + str(round(hdwd_total_price, 2)) + "\n"
                    + "Total Materials and Labor for this frame: $" + str(matlab) + "\n"
                    + "Costs of Goods Sold: $" + str(cost_of_goods_sold) + "\n"
                    + "Your Quote is: $" + str(quote))

frame_file.close()

print("Done!")