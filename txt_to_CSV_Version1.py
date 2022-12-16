import csv


print("START")

openHandle = open("C:\\UNIFRANS\\Others\\testing\\AAATesting.txt", 'r')
outputHandle  =  open("\\UNIFRANS\\Others\\testing2\\" + "OutputSample" + ".csv" ,'w', newline = "")

writer = csv.writer(outputHandle)

content = openHandle.read()

rowSplitList = content.split('\n') #splits big String into list of rows

for rowItem in rowSplitList:
    cellSplitList = rowItem.split() #splits rows separated by spaces into list of individual cell content
    writer.writerow(cellSplitList)

openHandle.close()
outputHandle.close()


print("DONE")