cp = float(input("Enter CP: "))
sp = float(input("Enter SP: "))

if sp > cp:
    print(f"Profit of {sp - cp}")
elif cp > sp:
    print(f"Loss of {cp - sp}")
else:
    print("No Profit No Loss")
