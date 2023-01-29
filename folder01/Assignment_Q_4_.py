import csv, sys
filename = 'CSVfile.csv'
newfile = 'new_file.csv'
Data = []
# reading data from a file
with open(filename, newline='') as f:
    reader = csv.reader(f)
    try:
        for row in reader:
            print(row)
            Data.append(row)
    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))
# writing data to another file
with open(newfile, 'w') as F:
    writer = csv.writer(F)
    try:
        for r in Data:
            for a in r :
                if a=='check' :
                    continue
            writer.writerow(r)
        print("\nData successfully written in new file !!")
    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))
        