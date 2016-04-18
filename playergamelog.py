import time
import requests
import json
import os

#Send an request to stats.nba.com which returns a JSON file containing all the player's info
url = 'http://stats.nba.com/stats/commonallplayers?IsOnlyCurrentSeason=0&LeagueID=00&Season=2014-15'
useragent = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'}
response = requests.get(url,headers=useragent)
response.raise_for_status()
playerinfo = response.json()['resultSets'][0]['rowSet']

#Parse the JSON data, retrieve players' full name and ID. Write it into a dictionary
allid = {}
for player in playerinfo:
    allid[player[2]] = player[0]
print 'Retrieve all player ID done'

#Backup the dictionary. Export it into a JSON file and save it to local
output = open('allid.json','w')
json.dump(allid,output,indent=4)
output.close()

#input = open('allid.json','r')
#playerid = json.load(input)
#input.close()

#Makd a 'gamelog' folder to store all the gamelogs
if not os.path.exists('gamelog'):os.mkdir('gamelog')

#Sent requests to stats.nba.com to get gamelog JSON files for all players in the list
#and save it to local
playerlist = open('playerlist.txt','r')
for player in playerlist:   
    player = player.strip()
    print player, allid[player]
    gamelogurl = 'http://stats.nba.com/stats/playergamelog?LeagueID=00&PlayerID='+str(allid[player])+'&Season=2014-15&SeasonType=Regular+Season'
    print gamelogurl
    response2 = requests.get(gamelogurl,headers=useragent)
    response2.raise_for_status()
    #gamelogheaders = response2.json()['resultSets'][0]['headers']
    #print gamelogheaders
    gamelog = response2.json()
    fileconn = open('gamelog/'+player+'.json','w')
    json.dump(gamelog,fileconn,indent=4)
    fileconn.close()
    print 'Retrieve',player,'\'s gamelog done'    
    time.sleep(3)
playerlist.close()

print 'All Done'