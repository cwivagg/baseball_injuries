from urllib2 import urlopen
from time import sleep

primStr1 = 'http://mlb.mlb.com/mlb/transactions/?c_id=mlb&year='
primStr2 = '&month='
for i in range(2001,2009):
    for j in range(1,13):
        myUrl = primStr1 + str(i) + primStr2 + str(j)
        page = urlopen(myUrl)
        pageText = page.read()
        myFileName = 'trans' + str(i) + '_' + str(j) + '.txt'
        myFile = open(myFileName,'w')
        myFile.write(pageText)
        myFile.close()
        sleep(3)