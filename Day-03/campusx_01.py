ctc = float(input("Enter annual CTC: "))
hra = 0.10 * ctc
da = 0.05 * ctc
pf = 0.03 * ctc
taxable = ctc - (hra + da + pf)

if ctc < 5:
    tax = 0
elif ctc >= 5 and ctc < 10:
    tax = 0.10 * taxable
elif ctc >= 10 and ctc < 20:
    tax = 0.20 * taxable
else:
    tax = 0.30 * taxable

in_hand = (taxable - tax) / 12
print(f"Monthly In-Hand Salary: {in_hand}")
