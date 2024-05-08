#it's a GPA finer

cgpa = float(input("What is your CGPA? "))

if(cgpa>=2.00 and cgpa<=5.00):
    print('You passed. And your CGPA is ',cgpa)
elif(cgpa >5.00 or cgpa < 0.005):
    print('Please inter valid CGPA')
else:
    print('Failed')