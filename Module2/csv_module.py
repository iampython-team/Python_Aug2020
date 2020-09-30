import csv

#csv.field_size_limit - current max field size 
#csv.reader - it reads the date from csv file 
#csv.writer - it writes the date into csv file


with open('Module2/covid19_tweets 2.csv','r') as csv_file:
    content=csv.reader(csv_file)
    print(content)
    for row in content:
        print(row)