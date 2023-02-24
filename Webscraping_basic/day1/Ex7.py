import csv
with open("data.csv",'w',newline = '') as f:
    wd = csv.writer(f)
    
    wd.writerow(["data1", 
                 "data2", 
                 "data3"])
    
    wd.writerows([[10, 20, 30], 
                  [10, 20, 30],
                  [10, 20, 30],
                  [10, 20, 30]])