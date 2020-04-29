import csv

count = 0
with open('/Users/malcolm/Downloads/TescoOut.csv', 'w', newline='') as csvOutfile:
    csvwriter = csv.writer(csvOutfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    with open('/Users/malcolm/Downloads/Tesco.csv',encoding='latin1' ) as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        for row in data:
                if count == 0:
                    count += 1
                    csvwriter.writerow(['Date(DD/MM/YYYY)']+['Description']+['Amount'])
                else:
                    count = count + 1
                    if 'DIRECT DEBIT PAYMENT' not in row[3]:
                        if '-' in row[2]:
                            csvwriter.writerow([row[0],row[3]+' '+row[4]+' '+row[5]+' '+row[6],row[2].strip('£-')])
                            print(row[0],row[3]+' '+row[4]+' '+row[5]+' '+row[6],row[2].strip('£-'))
                        else:
                            csvwriter.writerow([row[0],row[3]+' '+row[4]+' '+row[5]+' '+row[6],'-'+row[2].strip('£')])
                            print(row[0],row[3]+' '+row[4]+' '+row[5]+' '+row[6],'-'+row[2].strip('£'))

with open('/Users/malcolm/Downloads/NatwestOut.csv', 'w', newline='') as csvOutfile:
    csvwriter = csv.writer(csvOutfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    with open('/Users/malcolm/Downloads/Natwest.csv') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        csvwriter.writerow(['Date(DD/MM/YYYY)']+['Description']+['Amount'])
        for row in data:
            if len(row)>0:
                if row[0] != 'Date':
                    csvwriter.writerow([row[0],row[2],row[3]])

f = open("/Users/malcolm/Downloads/AmexCombined.csv", "w")
tempf1 = open('/Users/malcolm/Downloads/Amex1.csv')
tempf2 = open('/Users/malcolm/Downloads/Amex2.csv')
f.write(tempf1.read())
f.write(tempf2.read())
f.close()
with open('/Users/malcolm/Downloads/AmexOut.csv', 'w', newline='') as csvOutfile:
    csvwriter = csv.writer(csvOutfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    with open('/Users/malcolm/Downloads/AmexCombined.csv') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        csvwriter.writerow(['Date(DD/MM/YYYY)']+['Description']+['Amount'])
        for row in data:
                if 'PAYMENT RECEIVED - THANK YOU' not in row[3]:
                        if '-' in row[2]:
                                csvwriter.writerow([row[0],row[3],(row[2].strip(' -'))])
                                print(row[0],row[3],(row[2].strip(' -')))
                        else:
                            csvwriter.writerow([row[0],row[3],'-'+(row[2].strip())])
                            print(row[0],row[3],'-'+row[2].strip())
                            
count = 0
with open('/Users/malcolm/Downloads/HalifaxOut.csv', 'w', newline='') as csvOutfile:
    csvwriter = csv.writer(csvOutfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    with open('/Users/malcolm/Downloads/Halifax.csv') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        #csvwriter.writerow(['Date(DD/MM/YYYY)']+['Description']+['Amount'])
        for row in data:
                if count == 0:
                    count += 1
                    csvwriter.writerow(['Date(DD/MM/YYYY)']+['Description']+['Amount'])
                else:
                        count = count + 1
                        if 'DIRECT DEBIT PAYMENT' not in row[3]:
                                if '-' in row[4]:
                                        csvwriter.writerow([row[0],row[3],(row[4].strip(' -'))])
                                        print(row[0],row[3],(row[4].strip(' -')))
                                else:
                                    csvwriter.writerow([row[0],row[3],'-'+(row[4].strip())])
                                    print(row[0],row[3],'-'+row[4].strip())

with open('/Users/malcolm/Downloads/Santander.txt',encoding='latin1') as csvfile:
	data = csv.reader(csvfile)
	for row in data:
		x=row[0].split('\xa0')
		if len (x) > 1:
			print(x[0],x[1])
