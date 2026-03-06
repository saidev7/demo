# Foydalanuvchidan ma'lumot olish
ism = input("Ismingiz nima? ")
tugilgan_yil = int(input("Tug'ilgan yilingizni kiriting: "))

# Joriy yilni belgilash va yoshni hisoblash
joriy_yil = 2026
yosh = joriy_yil - tugilgan_yil

# Natijani chiqarish
print(f"\nSalom, {ism}!")
print(f"Siz hozirda {yosh} yoshdasiz.")

# Shartli tekshirish
if yosh >= 18:
    print("Siz voyaga yetgan foydalanuvchisiz. 😎")
else:
    print("Siz hali juda yosh ekansiz! 🌱")
