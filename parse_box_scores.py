from lxml import etree
from os import listdir

parser = etree.HTMLParser()

from parser_functions import pitcherFullParse
from parser_functions import getTemperature



### Part 0: Setting up Files and XML

parsing = open("./parse_012717afternoon.csv",'w')

ii = 0
tempList = []
tempList.append('CAL199004090.txt')
#for file in tempList:
for file in listdir('./parsed_box_scores'):
#    if file[0] != '.asdf':
    if file[0] != '.':
        fullFile = './parsed_box_scores/' + file
        tree = etree.parse(fullFile, parser)
        root = tree.getroot()

### Part 1: Extracting and Writing Data

        tablesOnPage = root.xpath('//table[@class="sortable  stats_table"]')
        gameDate = file[3:11]
        temperature = getTemperature(root)

        for i in range(2,4):
            try:
                extractedData = pitcherFullParse(tablesOnPage[i])
                ## pitcherFullParse returns a trailing newline.
                extractedData = extractedData[0:-1] + ',' + gameDate + ',' \
                    + str(temperature) + '\n'
                parsing.write(extractedData) 
            except:
                print file

### Part 2: Handholding and Cleanup

    ii += 1
    if ii % 1000 == 0:
        print str(ii), "games parsed"

parsing.close()