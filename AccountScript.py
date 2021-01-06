import csv
import datetime

#CCT
count = 0
with open('/Users/malcolm/Documents/HomeBudget/CCTout.csv', 'w', newline='') as csvOutfile:
    csvwriter = csv.writer(csvOutfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    with open('/Users/malcolm/Documents/HomeBudget/CCT.csv',encoding='latin1' ) as csvfile:
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
#CA1
with open('/Users/malcolm/Documents/HomeBudget/CA1Out.csv', 'w', newline='') as csvOutfile:
    csvwriter = csv.writer(csvOutfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    with open('/Users/malcolm/Documents/HomeBudget/CA1.csv') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        csvwriter.writerow(['Date(DD/MM/YYYY)']+['Description']+['Amount'])
        for row in data:
            if len(row)>0:
                if row[0] != 'Date':
                    csvwriter.writerow([row[0],row[2],row[3]])
#CCA
f = open("/Users/malcolm/Documents/HomeBudget/CCACombined.csv", "w")
tempf1 = open('/Users/malcolm/Documents/HomeBudget/CCA1.csv')
tempf2 = open('/Users/malcolm/Documents/HomeBudget/CCA2.csv')
f.write(tempf1.read())
f.write("\n")
f.write(tempf2.read())
f.close()
with open('/Users/malcolm/Documents/HomeBudget/CCAOut.csv', 'w', newline='') as csvOutfile:
    csvwriter = csv.writer(csvOutfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    with open('/Users/malcolm/Documents/HomeBudget/CCACombined.csv') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        csvwriter.writerow(['Date(DD/MM/YYYY)']+['Description']+['Amount'])
        for row in data:
            if row[0] != 'Date':
                if ('PAYMENT RECEIVED - THANK YOU' not in row[1]):
                        if '-' in row[4]:
                                csvwriter.writerow([row[0],row[1],(row[4].strip(' -'))])
                                print(row[0],row[1],(row[4].strip(' -')))
                        else:
                            csvwriter.writerow([row[0],row[1],'-'+(row[4].strip())])
                            print(row[0],row[1],'-'+row[4].strip())

#CCH
count = 0
with open('/Users/malcolm/Documents/HomeBudget/CCHOut.csv', 'w', newline='') as csvOutfile:
    csvwriter = csv.writer(csvOutfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    with open('/Users/malcolm/Documents/HomeBudget/CCH.csv') as csvfile:
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

#CA2
'''
with open('/Users/malcolm/Documents/HomeBudget/CA2.txt',encoding='latin1') as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        print('YY',row)
        x=row[0].split('\xa0')
        if len (x) > 1:
            print(x[0],x[1])
'''
#Pp
now = datetime.datetime.now()
lastmonth = now.month - 1
if (lastmonth < 10):
    MonthStr = '0'+str(lastmonth)
else:
    MonthStr = str(lastmonth)
if (MonthStr == '00'):
    MonthStr = '12'

with open('/Users/malcolm/Documents/HomeBudget/PpOut.csv', 'w', newline='') as csvOutfile:
    csvwriter = csv.writer(csvOutfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    with open('/Users/malcolm/Documents/HomeBudget/Pp.csv') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        csvwriter.writerow(['Date(DD/MM/YYYY)']+['Description']+['Amount'])
        for row in data:
            if (row[0][3:5] == MonthStr):
                if len(row)>0:
                    if row[0] != 'Date':
                        if row[15] == '':
                                if row[5] == 'Completed':
                                    csvwriter.writerow([row[0],row[3],row[7]])
                                    print (row[0],row[3],row[7], row[5])
                        else:
                                if row[5] == 'Completed':
                                    csvwriter.writerow([row[0],row[15],row[7]])
                                    print (row[0],row[15],row[7],row[5])
