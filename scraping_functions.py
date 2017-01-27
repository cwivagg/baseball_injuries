from urllib2 import urlopen
from lxml import etree
from unidecode import unidecode

def fetchPlayerName(s):
    s = 'http://www.baseball-reference.com/players/' + s[0] + '/' + s + '.shtml'
    parser = etree.HTMLParser(encoding='utf-8')
    try:
        page = urlopen(s)
    except:
        page = urlopen(s)
    tree = etree.parse(page, parser)
    root = tree.getroot()
    test = root.xpath('//div/span[@id="player_name"]/text()')
    if test:
        return unidecode(test[0])
    else:
        return 'no_name'

def fetchPlayerBirths(name):
	player_url = 'http://www.baseball-reference.com/players/' + name + '.shtml'
	parser = etree.HTMLParser()
	page = urlopen(player_url)
	tree = etree.parse(page, parser)
	root = tree.getroot()
	try:
		birthString = root.xpath('//p/span/@data-birth')[0]
	except:
		birthString = '0'
                print "Failure on " + player_url	
	time.sleep(3)
	return birthString