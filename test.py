hdwd = [
    {'name':'Front Spring Rail','qty': 1 , 'length': 50 , 'width': 1.75}
    ,{'name':'Back Spring Rail','qty': 1 , 'length': 60 , 'width': 1.75}]

print(hdwd[-1]['name'] + str(hdwd[-1]['qty']))

name_update = input()
qty_update = input()
length_update = input()
width_update = input()

hdwd = hdwd + [{'name': name_update , 'qty':qty_update, 'length': length_update , 'width': width_update}]

hdwd_file = open("filenamegohere.csv", "w+")

for i in range(3):
    hdwd_file.write(hdwd[i]['name'] + "," + str(hdwd[i]['qty']) + "," + str(hdwd[i]['length']) + "," + str(hdwd[i]['width']) + "\n")

print("Done!")