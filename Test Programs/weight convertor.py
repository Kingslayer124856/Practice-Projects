"""
Project weight converter
Made by: Cassandra King
Edit date:
"""
#could add more weight options and conversions
# selection of type of weight into another selection, will need formulas for each weight type

weight = float(input("Weight: "))
type = input("(K)g or (L)bs: ").lower()
if type == "k":
    converted = weight / 0.45
    print("Weight in Lbs: ", converted)
elif type == "l":
    converted= weight * 0.45
    print("Weight in Kg: ", converted)
