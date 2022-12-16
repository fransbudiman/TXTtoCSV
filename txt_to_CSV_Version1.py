import glob
import pandas as pd
import csv


for file in glob.glob("\\UNIFRANS\\Others\\testing\\*.xlsx"):
    print(file)
    read_file = pd.read_excel(file)
    backName = file.split("\\")[-1]
    backName = backName.split(".")[0]
    print(backName)
    read_file.to_csv("\\UNIFRANS\\Others\\testing\\"+backName + "_split.csv", index = None)
    outputHandle = open("\\UNIFRANS\\Others\\testing\\"+backName + "_final.csv", 'w', newline = None)
    writer = csv.writer(outputHandle)
    
    with open("\\UNIFRANS\\Others\\testing\\"+backName + "_split.csv", 'r') as f:
        for row in f:
            row = row.replace("\n","")
            listRow = row.split(" ")
            print(listRow)
            writer.writerow(listRow)
    outputHandle.close()
    

            
    
print("DONE!")