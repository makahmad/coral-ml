import os
import csv

reader = csv.reader(open('HistoryOfCoralBarcodes_20160906.csv'))

result = {}
for row in reader:
    key = row[0]
    result[key] = row[1]
    if key[:3] == '100':
        result[key[3:]] = row[1]
    elif key[:2] == '10':
        result[key[2:]] = row[1]


# Open a file
path = "photos"
dirs = os.listdir(path)

# This would print all the files and directories
for file in dirs:
    if os.path.isfile(os.path.join(path, file)) and file[:1] != ".":
        # print file
        x = str.split(file.lower())
        lastString = x[len(x) - 1]
        if lastString=="(2).jpg":
            lastString=x[len(x) - 2]
        barcode = lastString.replace(".1.jpg","") #x[len(x)-1][:9]
        barcode = barcode.replace(".2.jpg", "")  # x[len(x)-1][:9]
        barcode = barcode.replace(".3.jpg", "")
        barcode = barcode.replace(".4.jpg", "")
        barcode = barcode.replace("c.jpg", "")
        barcode = barcode.replace("b.jpg", "")
        barcode = barcode.replace("a.jpg", "")
        barcode = barcode.replace(".jpg", "")  # x[len(x)-1][:9]
        print barcode
        try:
            if not os.path.exists(path+"/"+result[barcode]):
                os.makedirs(path+"/"+result[barcode])

            os.rename(path+"/"+file, path+"/"+result[barcode]+"/"+file)
        except KeyError, e:
            if not os.path.exists(path+"/UnknownBarcodes"):
                os.makedirs(path+"/UnknownBarcodes")

            os.rename(path+"/"+file, path+"/UnknownBarcodes/"+file)





