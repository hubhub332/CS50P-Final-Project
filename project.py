'''
dictreader, rec spendings as dictionary
delete object (add serial code or number to dlt, or with dictionary["name"] if possible)
add file

Menu
1. Add Rec >> choice of file >> add (item, price, time rec)
2. Dlt Rec >> choice of file >> choose which to dlt
3. Add File >> choose csv or txt >> type file name
4. Exit Program


sort (choice) ex: sort item sort price
can count total

item price time
'''
# rec = []
# while True:
#     item = input("Item: ")

#     if item == "":
#         break

#     else:
#         price = input("Price: RM")
#         a = {"Item":item, "Price":price}
#         rec.append(a)




# with open("Rec.txt", "a") as f:
#     for i in rec:
#         f.write(f"Item: {i['Item']}, Price: RM{i['Price']}\n")


import sys
import csv
import re
import os

try:
    os.mkdir("C:\\Desktop\\Personal Code\\Spendings")
except FileExistsError:
    ...


fieldname = ["Item", "Price"]

def main():
    while True:
        try:
            print("1. Add Records")
            print("2. Delete Records")
            print("3. Add File")
            print("4. Exit Program")

            choice = int(input())

            match choice:
                case 1:
                    file = choosefile()
                    rec(file)

                case 2:
                    file = choosefile()
                    dltrec(file)

                case 3:
                    outcome = openfile()
                    print(outcome)

                case 4:
                    sys.exit("See you next time")

                case _:
                    print("Thats not a valid choice! Please choose 1-4!")

        except ValueError:
            print("Please select the choices given!\n")
        
        except IndexError:
            print("Please only select the choice given!")

        except TypeError:
            print("Please only input numbers (0-9)!")


def openfile(): #make a new file(csv) with custom name
    global fieldname
    filename = input("Please name your csv file: ")

    #catch input
    try:
        #re.match to ensure only give alphabets, no special character
        with open(f"{filename}.csv", "x", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldname)
            writer.writeheader()

    #return for testing
    except FileExistsError:
        return("File already exist.\n")
    
    #return for testing
    else:
        return(f"File {filename}.csv is created.\n")

def choosefile():
    count = 0
    files = os.listdir("C:\\Desktop\\Personal Code\\Spendings")
    for file in files:
        count += 1
        print(f"{count}. {file}")

    choice = int(input())
    return files[choice-1]

def dltrec(file):
    global fieldname
    read = []

    #read file (have to make it to read what files do i have.)
    with open(f"{file}") as file:
        count = 0
        reader = csv.DictReader(file)
        for row in reader:
            count += 1
            read.append({"No": count, "Item": row["Item"], "Price": row["Price"]})

    #show what to delete
    for r in read:
        print(r)

    #catch input error
    try:
        dlt = int(input("Choose what No. to delete: "))
        read.pop((dlt-1))
    except IndexError:
        print("Please only delete what you have!")
    except TypeError:
        print("Please only input numbers (0-9)!")

    #rewrite deleted version into the file
    with open(f"{file}", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldname)
        writer.writeheader()
        for i in read:
            writer.writerow({"Item":i["Item"], "Price":i["Price"]})


def rec(file): #record 
    global fieldname

    #read file (have to make it to read what files do i have.)
    with open(f"{file}", "a", newline="") as file:
        while True:
            item = input("Item: ")

            if item == "":
                break
            else:
                price = input("Price: ")
                writer = csv.DictWriter(file, fieldnames=fieldname)
                writer.writerow({"Item": item, "Price": price})

#run
if __name__ == "__main__":
    main()