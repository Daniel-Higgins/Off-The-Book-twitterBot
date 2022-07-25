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
#can do this part bc im great
check = "Blue Jays"

for i in data_json:
    gameID = i['id']
    ht = checkTeam(i['home_team'])
    at = checkTeam(i['away_team'])
    time = i["commence_time"]
    
    #if check == ht or check == at: 

    array = []
    array2 = []
    hml = ""
    aml = ""
    for j in i['bookmakers']:
        
            bookKey = j['key']
            bookTitle = j['title']
        
            if(bookKey == 'draftkings' or bookKey == 'fanduel' or bookKey == 'betmgm' or bookKey == 'barstool' or bookKey == 'pointsbetus' or bookKey == 'wynnbet' or bookKey == 'williamhill_us'):
                
                hspread = ""
                hsprOdds = ""
                aspread = ""
                asprOdds = ""
                for k in j['markets']:
                    #fix a few B keys
                    
                    if bookKey == 'williamhill_us':
                        bookTitle = "Caesars"
                    if bookKey == 'pointsbetus':
                        bookTitle = "PointsBet"
                    if bookKey == 'barstool':
                        bookTitle = 'Barstool'
                        
                    if k['key'] == "spreads":
                        if checkTeam(k['outcomes'][0]['name']) == ht:
                            hspread = k['outcomes'][0]['point'] 
                            hsprOdds = k['outcomes'][0]['price']
                            aspread = k['outcomes'][1]['point']
                            asprOdds = k['outcomes'][1]['price']
                        elif checkTeam(k['outcomes'][1]['name']) == ht:
                            hspread = k['outcomes'][1]['point'] 
                            hsprOdds = k['outcomes'][1]['price']
                            aspread = k['outcomes'][0]['point']
                            asprOdds = k['outcomes'][0]['price']
                        else:
                            print("spr what")
                    if k['key'] == "h2h":
                        if checkTeam(k['outcomes'][0]['name']) == ht:
                            hml = k['outcomes'][0]['price']
                            aml = k['outcomes'][1]['price']
                        elif checkTeam(k['outcomes'][1]['name']) == ht:
                            hml = k['outcomes'][1]['price']
                            aml = k['outcomes'][0]['price']
                        else:
                            print("ML what")                    
                obj = functionsPage.Matchup(gameID, time, ht,at, bookTitle, hml, aml, hspread, hsprOdds, aspread, asprOdds)
                
                array.append(obj)
                array2.append(obj)   
                
    if True:
            sortMLh(array)
            sortSOddsH(array2)
            printResults("spreads")
            printResults("ml")
            array.clear()
        #if check == at:
         #   sortMLa(array)
          #  sortSOddsA(array2)
           # printResults("spreads")
            #printResults("ml")
            #array.clear()
    
