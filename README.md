ism = input("Ismingiz nima? ")
tugilgan_yil = int(input("Tug'ilgan yilingizni kiriting: "))

joriy_yil = 2026
yosh = joriy_yil - tugilgan_yil

print(f"\nSalom, {ism}!")
print(f"Siz hozirda {yosh} yoshdasiz.")

if yosh >= 18:
    print("Siz voyaga yetgan foydalanuvchisiz. 😎")
else:
    print("Siz hali juda yosh ekansiz! 🌱")
