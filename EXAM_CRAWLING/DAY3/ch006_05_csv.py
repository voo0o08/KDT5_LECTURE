import csv
csvFile = open("test.csv", "w", encoding="utf-8")
try:
    writer = csv.writer(csvFile)
    writer.writerow(("num", "num+2", "(num+2)^2"))

    for i in range(10):
        writer.writerow((i, i+2, (i+2)**2))

except Exception as e:
    print(e)
finally:
    csvFile.close()