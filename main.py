import csv

data = []

with open("star.csv","r") as m:
    csvreader = csv.reader(m)
    for row in csvreader:
        data.append(row)

#headers is in 0 index
headers = data[0]
#1: to get all data
stars_data = data[1:]

for data_point in stars_data:
    data_point[0] = data_point[0].lower()

#creating anonymous funtion to sort alphabetically
stars_data.sort(key = lambda stars_data: stars_data[0])

#a+ = appending and writing
with open("stars_sorted.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(stars_data)

