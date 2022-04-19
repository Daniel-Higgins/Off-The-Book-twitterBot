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
        
            # cycles through the sportsbooks and gets info in every matchup
                    
                            
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
                    #nothing here

wmax = 0
fmax = 0
cmax = 0
dmax = 0
bmax = 0
gmax = 0
pmax = 0

#now sorts every matchup per book
sortBook(x)
sortBook(x)
sortBook(x)
sortBook(x)
sortBook(x)
sortBook(x)
sortBook(x)


#gets the highest paying odds per book and lists them
     
sortedOddsList = [wmax, fmax, bmax, gmax, pmax, dmax, cmax]
print(sortedOddsList)
sortedOddsList.sort(reverse = True)


fanswer = ""
if sortedOddsList[0] == wmax:
    fanswer = getCMP(wworks, "WynnBet")
elif sortedOddsList[0] == bmax:
    fanswer = getCMP(bworks, "Barstool")
elif sortedOddsList[0] == pmax:
    fanswer = getCMP(pb, "PointsBet")
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
