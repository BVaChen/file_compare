import csv, sys
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askdirectory

print("Select the first file to compare: ")
firstFile = filedialog.askopenfilename()    #Prompts user to select first file
print("Select the second file to compare: ")
secondFile = filedialog.askopenfilename()   #Prompts user to select second file

#Prompts user to choose an output location and writes output into file called, "output_list.csv"
print("Choose a folder you want to write your output to:")
path = askdirectory(title='Select Folder')
full_path = path + "/compare_output_list.csv"

firstInput = int(input("Type which column you would like to compare in the first file: ")) - 1    #Asks user to type in the number for the column they want to compare
secondInput = int(input("Type which column you would like to compare in the second file: ")) - 1

firstList = []
secondList = []

with open(firstFile, encoding='utf-8-sig') as csvFile1, open(secondFile, encoding='utf-8-sig') as csvFile2:       #Opens CSV file
    reader1 = csv.reader(csvFile1)      #Reads the two CSV file 
    reader2 = csv.reader(csvFile2)      
    for row1 in reader1:
        firstList.append(row1[int(firstInput)])         #Iterates each row and appends the field to a list
    for row2 in reader2:
        secondList.append(row2[int(secondInput)])

#Compares the two lists and finds differences
diff = list(set(firstList) - set(secondList))
print(diff)

#Compare the Mac Address section between firstFullList and secondList. Select the email that matches with the Mac Addresses
f = open(full_path, 'w', newline='')
writer = csv.writer(f)

for element in diff:
    writer.writerow([element])

f.close()

