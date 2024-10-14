nama= input("Masukkan nama anda: ")
sex= input("Masukkan jenis kelamin anda (L atau P): ")
while sex != "P" or sex!= "L":
    sex= input("Masukkan jenis kelamin anda (L atau P): ")
    if sex=='P' or sex=='L':
        break

BB= float(input("Masukkan berat bada anda dalam Kg: "))
TB= float(input("Masukkan tinggi anda dalam Cm: "))

BMI= BB / (TB/100)**2

if BMI < 18.5 and sex == 'L':
    print("Underweight")
elif (BMI>18.5 or BMI < 24.9) and sex == 'L':
    print("Healthy weight")
elif (BMI>25 or BMI < 29.9) and sex == 'L':
    print("Overweight")
elif BMI>=30  and sex == 'L':
    print("Obesity")
elif BMI<17.5:
    print("Underweight")
elif (BMI>17.5 or BMI <23.9) and sex == 'P':
    print("Healthy weight")
elif (BMI>24 or BMI < 27.9) and sex == 'P':
    print("Overweight")
elif (BMI>=28) and sex == 'P':
    print("Obesity")