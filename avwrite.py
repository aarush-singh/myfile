import csv

with open("data.csv", "w", newline="")as f:
    rsc = csv.write(f,)
    rsc.writerow(["new", "roll", "class"])
    li = []

    while True:
        name = input("Enter Your Name: ")
        roll_no = int(input("Enter Your Roll Number: "))
        c = int(input("Enter Your Class: "))
        li = (name, roll_no, c)
        rsc.writerow(li)
        more_info = input("Enter More Information I You Want To: ")

        if more_info in "Nn":
            break

                      





