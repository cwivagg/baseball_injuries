import os

from lxml import etree
from scraping_functions import player_record
from scraping_functions import age_db_creator
from scraping_functions import age_db_no_match
from scraping_functions import get_player_hands

parser = etree.HTMLParser()

prevWork = open('db_age2.csv', 'r')
db = age_db_creator(prevWork)
prevWork.close()
fetchPlayersIndex = [9, 11]
pA = open('db_age2', 'a')

for file in os.listdir('parsed_box_scores'):
	if file[0] != '.':
		fullFile = 'parsed_box_scores/' + file
		tree = etree.parse(fullFile, parser)
		root = tree.getroot()
		for ind in fetchPlayersIndex:
			for player in root.xpath('/html/body/div/div[3]/div[%i]/div[2]/table/tbody/tr/td[1]/a/@href' % ind):
				name = player[11:-6]
				if age_db_no_match(db,name):
					ages = fetchPlayerBirths(name[0] + '/' + name)
					db.append(player_record(name, ages))
					pA.write('\n' + name + ',' + ages)