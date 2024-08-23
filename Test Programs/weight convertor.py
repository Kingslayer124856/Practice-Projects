weight = float(input("Weight: "))
type = input("(K)g or (L)bs: ").lower()
if type == "k":
    converted = weight / 0.45
    print("Weight in Lbs: ", converted)
elif type == "l":
    converted= weight * 0.45
    print("Weight in Kg: ", converted)
