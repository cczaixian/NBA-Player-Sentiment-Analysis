import urllib2
from bs4 import BeautifulSoup as bs
import re
import time
import json

#Make a browser
browser=urllib2.build_opener()
browser.addheaders=[('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A')]

#Make a dictionary to store all the players' info, including Twitter Account and salaries
playerinfo = {}
playerlist = open('playerlist.txt','r')
for player in playerlist:   
    player = player.strip()
    #Get to first character of player's last name
    lastname = player.split(' ')[1][0].lower()
    
    #Open the webpage of all players, retrieve the url for this player 
    url='http://www.basketball-reference.com/players/'+lastname
    html = browser.open(url).read()
    soup = bs(html,'lxml')
    #Find all the strong tags which contain only active players in this season but not retired players 
    tag = soup.find('strong',string = re.compile(player)).find('a')
    url2 = 'http://www.basketball-reference.com' + tag.get('href',None)
    time.sleep(2)
    
    #Open a player's URL and parse his info
    print 'Parsing',player,'\'s info.'
    soup2 = bs(browser.open(url2).read(),'lxml')
    
    #twitter = soup2.find('a',class_=False,href=re.compile('https://twitter.com'))
    #print 'Get',player, '\'s Twitter Account.'
    
    #Parse the html code and retrieve player's 2014-15 season salary. Write it to a dictionary
    salaries = soup2.find('table',class_="sortable  stats_table", id="salaries")\
    .find('tbody').find_all('tr')
    salarydict = {}
    for each in salaries:
        if each.contents[1].text != '2014-15':
            continue
        salarydict[str(each.contents[1].text)] = each.contents[7].get('csk',None)
        print 'Get',player, '\'s 2014-15 Season Salaries.'
    
    #Summarize the player info into a dictionary
    playerinfo[player] = {'salary':salarydict}
    #playerinfo[player]['screen_name'] = str(twitter.text)
    print 'Get',player,'\'s Info Done.'    
    time.sleep(2)
playerlist.close()
#print playerinfo

#Export the playerinfo dictionary to a JSON file and save to local
fileconn = open('playerinfo.json','w')
json.dump(playerinfo,fileconn,indent=4)
fileconn.close()
print 'All Done'
