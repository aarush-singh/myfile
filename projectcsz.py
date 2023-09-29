import csv

# def search():

#     f = open("data.csv", "a", newline='')
#     obj = csv.writer(f)

#     while True:
#         name = input("Enter Your Name: ")
#         roll_no = int(input("Enter Your Roll No: "))
#         marks = int(input("Enter Your Total Marks: "))
#         y_n = input("Enter Y if you want to continue, if you want to stop here press n: ")
        
#         l = [name, roll_no, marks]
#         obj.writerow(l)
        
#         if y_n in "Nn":
#             break
#     f.close()

def search():
    f = open("data.csv", 'r')
    re = csv.reader(f)
    n = input("Enter Your Name For Search: ")
    for i in re:
        if n == i[0]:
            print(i)
    f.close()
#writing()
#read()
search()
