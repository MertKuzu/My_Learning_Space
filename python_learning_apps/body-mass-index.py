
name=input("Adınız: ")
weight=float(input("Kilonuz:"))
height=float(input("Boyunuz: "))

formul= weight/(height**2)            #bmi formula
formul=round(formul, 3)     #küsüratlı sayı çok uzamasın 

if (formul<=18.4):
    print(f"{name}, zayıfsın.")
elif (formul>=18.5 and formul<=24.9):
    print(f"{name}, vücut kilte endeksin {formul} normalsin.")
elif (formul>=25.0 and formul<=29.9):
    print(f"{name}, vücut kitle endeksin {formul} fazla kilolusun.")
elif (formul>29.9):
    print(f"{name}, vücut kitle endeksin {formul} aşırı kilolusun obezsin acilen diyetisyene git!!!")
else:
    print("Girdiğiniz bilgiler hatalıdır.")