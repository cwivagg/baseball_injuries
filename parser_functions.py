import re

from lxml import etree
from sys import exit
from datetime import date
from time import strptime
from unidecode import unidecode

def processTable(tbl):
    datesList = []
    transList = []
    inDate = date(1,1,1)
    i = 0
    for row in tbl.xpath('./tr'):
        if row.xpath('./@valign="top"'):
            if row.xpath('./td/b[contains(text(),"/")]'):
                inDate = strptime(row.xpath('./td/b/text()')[0].strip(),'%m/%d/%y')
            shortList = '.'.join(row.xpath('./td[2]/text()'))
            slItems = re.split('[.;:]', shortList)
            for slItem in slItems:
                datesList.append(inDate)
                transList.append(unidecode(slItem.strip()))
    return (datesList, transList)

def parseForDl(s):
    myFile = open(s,'r')
    parser = etree.HTMLParser(encoding='utf-8')
    tree = etree.parse(myFile,parser)
    root = tree.getroot()
    locatedTransaction = root.xpath('//td[text()="Transaction"]')[0]
    locatedTable = locatedTransaction.xpath('./../..')[0]
    return processTable(locatedTable)

def isDl(s):
    if '15' in s:
        if 'laced' in s:
            return True
    return False

def containsPitcher(s,dict):
    for pitcher in dict:
        if pitcher[1] in s:
            return pitcher[0]
    return False

def pitcherFullParse(xmlTable):
    xmlRow = xmlTable.xpath('./tbody/tr')[0]
    pName = xmlRow.xpath('./td/a/@href')[0][11:-6]
    inningsPitched = xmlRow.xpath('./td[2]/span/text()')[0]
    hits = xmlRow.xpath('./td[3]/text()')[0]
    runs = xmlRow.xpath('./td[4]/text()')[0]
    earnedRuns = xmlRow.xpath('./td[5]/text()')[0]
    walks = xmlRow.xpath('./td[6]/text()')[0]
    SO = xmlRow.xpath('./td[7]/text()')[0]
    HR = xmlRow.xpath('./td[8]/text()')[0]
    ERA = xmlRow.xpath('./td[9]/text()')[0]
    BF = xmlRow.xpath('./td[10]/text()')[0]
# These quantities are occasionally missing.
    pitches = xmlRow.xpath('./td[11]/text()')
    pitches = '-1' if not pitches else pitches[0]
    Str = xmlRow.xpath('./td[12]/text()')
    Str = '-1' if not Str else Str[0]
    Ctct = xmlRow.xpath('./td[13]/text()')
    Ctct = '-1' if not Ctct else Ctct[0]
    StS = xmlRow.xpath('./td[14]/text()')
    StS = '-1' if not StS else StS[0]
    StL = xmlRow.xpath('./td[15]/text()')
    StL = '-1' if not StL else StL[0]
    GB = xmlRow.xpath('./td[16]/text()')[0]
    FB = xmlRow.xpath('./td[17]/text()')[0]
    LD = xmlRow.xpath('./td[18]/text()')[0]
    Unk = xmlRow.xpath('./td[19]/text()')[0]
    GSc = xmlRow.xpath('./td[20]/text()')[0]
    WPA = xmlRow.xpath('./td[23]/text()')[0]
    aLI = xmlRow.xpath('./td[24]/text()')[0]
    RE24 = xmlRow.xpath('./td[25]/text()')[0]
    return \
        pName + ',' + inningsPitched + ',' + hits + ',' + \
        hits + ',' + runs + ',' + earnedRuns + ',' + \
        walks + ',' + SO + ',' + HR + ',' + \
        ERA + ',' + BF + ',' + pitches + ',' + \
        Str + ',' + Ctct + ',' + StS + ',' + \
        StL + ',' + GB + ',' + FB + ',' + \
        LD + ',' + Unk + ',' + GSc + ',' + \
        WPA + ',' + aLI + ',' + RE24 + '\n'