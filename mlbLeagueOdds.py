from urllib.request import urlopen
from functionsPage import addPlusTo, sortSOddsH, sortSOddsA, printResults, sortMLa, sortMLh, checkTeam
import functionsPage
import json

#this file displays the results of everymatchup for the whole MLB


# store the URL in url as

# parameter for urlopen
keyP = ...
-
-
url = "https://api.the-odds-api.com/.../.../.../.../...&...&.../..."

response = urlopen(url)

# storing the JSON response

# from url in data

data_json = json.loads(response.read())

#parse json
#

for i in data_json:
    gameID = i['id']
    ht = checkTeam(i['home_team'])
    at = checkTeam(i['away_team'])
    time = i["commence_time"]
    
    #pull starting info from json results

        
        for j in "Sportsbooks":
            #pull bookie information next
            bookKey = j['key']
            bookTitle = j['title']
        
            
            #if popular bookie exists advance
            -
                hspread = ""
                hsprOdds = ""
                aspread = ""
                asprOdds = ""
                for k in #markets :
                    #loop over the bookie matchup details and pull odds
                    -
                    -
                    -
                    -
                    -
                    
                    #grab odds and place in a list   
                    -
                    -
                    -
                    -
                #add matchup object with all detailsinto a list ready to parse through   
                
                -
                -
                -
                -
                -
                -
         
                
          if True:
            sortMLh(array)
            sortSOddsH(array2)
            printResults("spreads")
            printResults("ml")
            -
            -
