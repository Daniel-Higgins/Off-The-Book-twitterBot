from urllib.request import urlopen
from functionsPage import addPlusTo, sortSOddsH, sortSOddsA, printResults, sortMLa, sortMLh, checkTeam, sortBook, getCMP, publishCMP, convert
import functionsPage
import json

# store the URL in url as

# parameter for urlopen

keyP = .....

url = "https://api.the-odds-api.com/..../../..//....

response = urlopen(url)

# storing the JSON response

# from url in data

data_json = json.loads(response.read())


draftkings = []
betmgm = []
pb = []
fanduel = []
caesars = []
wynn = []
barstool = []

for i in data_json:
    gameID = i['id']
    ht = checkTeam(i['home_team'])
    at = checkTeam(i['away_team'])
    time = i["commence_time"]
    
    #if check == ht or check == at: 
    
    hml = ""
    aml = ""
    for j in i['bookmakers']:
        
            bookKey = j['key']
            bookTitle = j['title']
        
            if True:
                
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
                
                if bookKey == 'draftkings':
                    draftkings.append(obj)
                elif bookKey == 'fanduel':
                    fanduel.append(obj)
                elif bookKey == 'barstool':
                    barstool.append(obj)
                elif bookKey == 'wynnbet':
                    wynn.append(obj)
                elif bookKey == 'williamhill_us':
                    caesars.append(obj)
                elif bookKey == 'betmgm':
                    betmgm.append(obj)
                elif bookKey == 'pointsbetus':
                    pb.append(obj)
                else:
                    pppppppp=1

wmax = 0
fmax = 0
cmax = 0
dmax = 0
bmax = 0
gmax = 0
pmax = 0
sortBook(wynn)
wworks = sortBook(wynn).copy()
if len(sortBook(wynn)) >= 8:
    
    wmax = convert(sortBook(wynn)[2], sortBook(wynn)[5], sortBook(wynn)[8])
sortBook(wynn).clear()

sortBook(fanduel)
fworks = sortBook(fanduel).copy()
if len(sortBook(fanduel)) >= 9:
    fmax = sortBook(fanduel)[2] + sortBook(fanduel)[5] + sortBook(fanduel)[8]
sortBook(fanduel).clear()


sortBook(caesars)
cworks = sortBook(caesars).copy()
if len(sortBook(caesars)) >= 8:
    cmax = sortBook(caesars)[2] + sortBook(caesars)[5] + sortBook(caesars)[8]
sortBook(caesars).clear()

sortBook(betmgm)
gworks = sortBook(betmgm).copy()
if len(sortBook(betmgm)) >= 8:
    gmax = convert(sortBook(betmgm)[2], sortBook(betmgm)[5], sortBook(betmgm)[8])
sortBook(betmgm).clear()

sortBook(draftkings)
dworks = sortBook(draftkings).copy()
if len(sortBook(draftkings)) >= 8:
    dmax = convert(sortBook(draftkings)[2], sortBook(draftkings)[5], sortBook(draftkings)[8])
sortBook(draftkings).clear()

sortBook(barstool)
bworks = sortBook(barstool).copy()
if len(sortBook(barstool)) >= 9:
    bmax = convert(sortBook(barstool)[2], sortBook(barstool)[5], sortBook(barstool)[8])
sortBook(barstool).clear()

sortBook(pb)
pworks = sortBook(pb).copy()
if len(sortBook(pb)) >= 8:
    pmax = convert(sortBook(pb)[2], sortBook(pb)[5], sortBook(pb)[8])
sortBook(pb).clear()                                             
    
     
sortedOddsList = [wmax, fmax, bmax, gmax, pmax, dmax, cmax]
print(sortedOddsList)
sortedOddsList.sort(reverse = True)


fanswer = ""
if sortedOddsList[0] == wmax:
    fanswer = getCMP(wworks, "WynnBet")
elif sortedOddsList[0] == bmax:
    fanswer = getCMP(bworks, "Barstool")
elif sortedOddsList[0] == pmax:
    fanswer = getCMP(pworks, "PointsBet")
elif sortedOddsList[0] == cmax:
    fanswer = getCMP(cworks, "Caesars")
elif sortedOddsList[0] == dmax:
    fanswer = getCMP(dworks, "DraftKings")
elif sortedOddsList[0] == gmax:
    fanswer = getCMP(gworks, "BetMGM")
elif sortedOddsList[0] == fmax:
    fanswer = getCMP(fworks, "Fanduel")
else:
    print("yo")



publishCMP(fanswer)
