import re
import time

from parser_functions import parseForDl
from parser_functions import isDl
from parser_functions import containsPitcher
from os import listdir

pitcherDictFile = open('pitcher_dict.csv','r')
pitcherDict = []
for line in pitcherDictFile:
    line = line.split(',')
    pitcherDict.append((line[0],line[1].rstrip()))

transactionDates = []
transactionTable = []

for file in listdir('transaction_history'):
    if file[0] != '.':
        (l1, l2) = parseForDl('transaction_history/' + file)
        transactionDates += l1
        transactionTable += l2

dlDates = []
dlTable = []

isDlCounter = 0
for i in range(len(transactionDates)):
    if isDl(transactionTable[i]):
        isDlCounter += 1
        shortenedExpression = transactionTable[i].split('15')[0]
        if containsPitcher(shortenedExpression,pitcherDict):
            dlDates.append(transactionDates[i])
            dlTable.append(containsPitcher(shortenedExpression,pitcherDict))
print "# Transaction Dates is %d" % len(transactionDates)
print "# Not Dl is %d\t" % (len(transactionDates)-isDlCounter)
f = open('db_dl_history.csv','w')
for i in range(len(dlDates)):
    f.write(dlTable[i] + ',' + time.strftime('%Y%m%d',dlDates[i]) + '\n')