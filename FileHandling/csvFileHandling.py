import csv

#csv file writing
with open("students.csv", "w", newline = "") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "age"])
    writer.writerow(["Aparna", "26"])
    writer.writerow(["Suraj", "32"])
    writer.writerow(["Pruthvi", "7"])

#csv file reading
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
