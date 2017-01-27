from scraping_functions import fetchPlayerName
from time import sleep
from unidecode import unidecode

f1 = open('unique_pitchers.txt','r')
f2 = open('pitcher_dict.csv','w')

for line in f1:
    shortName = line[:-1]
    fullName = fetchPlayerName(line[:-1])
    sleep(3)
    f2.write(shortName + ',' + fullName + '\n')