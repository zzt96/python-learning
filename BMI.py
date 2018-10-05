weight=input('please input your weight(kg):')
height=input('please input your height(m):')
w=float(weight)
h=float(height)
bmi=w/(h*h)

print(" your weight is",weight,"kg\n",
"your height is",height,"m\n",
"your BMI is %.2f\n" %bmi)

if bmi<18.5:
    print('您太轻了，需要增肌')
elif bmi<25:
    print('您的体重正常！')
elif bmi<28:
    print('您过重啦！')
elif bmi<32:
    print('your are obesity!')
else:
    print('your are dangerously obesity, please start fitness immediately')

    
