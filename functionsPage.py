import json
from twitterBot import publictweet
from datetime import datetime
import dateutil.parser
import pytz

#different functions called. Some greyd out


def addPlusTo(x):
    if(x > 0):
        newX = "+" + str(x)
        return newX
    
    else:
        return str(x)
    
def checkTeam(w):
    
    if w == "Toronto Blue Jays":
        ht = "Blue Jays"
        return ht
    elif w == "Boston Red Sox":
        ht = "Red Sox"
        return ht
    elif w == "Chicago White Sox":
        ht = "White Sox"
        return ht
    else:
        temp = w.split()
        ht = temp[-1]
        return ht
    
    
class Matchup:
    def __init__(self, gid, time, ht, at, sb, hmline, amline, hspr, hprice, aspr, aprice):
        if hprice == "":
            hprice = -100000
            hspr = 1.5
        if aprice == "":
            aprice = -100000
            aspr = 1.5
        if hmline == "":
            hmline = -100000
        if amline == "":
            amline = -100000
        self.gameID = gid
        self.dTime = time
        self.homeTeam = ht
        self.awayTeam = at
        self.sportsbook = sb
        self.hML = hmline
        self.aML = amline
        self.homeSpread= hspr
        self.awaySpread = aspr
        self.homePrice = hprice
        self.awayPrice = aprice
        
        
SprnewList = []
MLnewList = []
def sortSOddsH(x):
    arrayj = x
    #debugging matchup variable calls
    if arrayj:
        
        #This function sorts all the sportsbooks Spread odds recursivly and places the
        # results in a list waiting to be called from
        
        sortSOddsH(arrayj)
        
        
def sortSOddsA(x):
    arrayj = x
    #debugging matchup variable calls
    if arrayj:
      
        #This function sorts all the sportsbooks Spread odds recursivly and places the
        # results in a list waiting to be called from
        
        sortSOddsA(arrayj)
        
def sortMLa(x):
    arrayj = x
    
    if arrayj:
        #This function sorts all the sportsbooks MoneyLines odds recursivly and places the
        # results in a list waiting to be called from
        sortMLa(arrayj)  
def sortMLh(x):
    arrayj = x
    #debugging matchup variable calls
    if arrayj:
        
        #This function sorts all the sportsbooks MoneyLines odds recursivly and places the
        # results in a list waiting to be called from
        
        sortMLh(arrayj)

#converts american to decimal format then does the math to find parlay odds
def convertD(a):
    dec = 0.0
    if a > 0:
        dec = (a/100)+1
    else:
        dec = 1-(100/a)
    return dec

def convert(a,b,c):
    decimal = convertD(a) * convertD(b) * convertD(c)
    decimal = decimal * 100
    decimal = decimal - 100
    return int(decimal)
    
    
#displays the cash money parlay 
def getCMP(x, t):
    parlay = x
    if parlay:
        teamA = parlay[0]
        operA = parlay[1]
        oddsA = parlay[2]
        teamB = parlay[3]
        operB = parlay[4]
        oddsB = parlay[5]
        teamC = parlay[6]
        operC = parlay[7]
        oddsC = parlay[8]
        
        x = datetime.now()
        finalOdds = convert(oddsA, oddsB, oddsC)
        answer = "" + str(x.month) + "/" + str(x.day) + "\n"
        answer += "Today's Cash Money Parlay provided by " + t + "\n\n"
        answer += teamA + " " + str(operA) + " " + addPlusTo(oddsA) + "\n"
        answer += teamB + " " + str(operB) + " " + addPlusTo(oddsB) + "\n"
        answer += teamC + " " + str(operC) + " " + addPlusTo(oddsC) + "\n\n"
        answer += "Final odds: " + str(addPlusTo(int(finalOdds))) + "\n\n"
    
        answer += "Bet it now here: " + websites[t]
    
        return answer
    
        
def timefix(x):
  #time comes in as unix format, displaying EST time
    g = x.replace("Z", "+00:00")
    f = dateutil.parser.isoparse(g)
    
    fe = f.astimezone(pytz.timezone('US/Eastern')).strftime('%Y-%m-%d %H:%M:%S %Z%z')
    s = fe.split(" ")
    day = s[0]
    t = s[1]
    spl = t.split(":")
    hour = spl[0]
    mins = spl[1]
    if int(hour) >12 :
        hour = int(hour) - 12
        mins = str(mins) + " PM"
    elif int(hour) >= 12:
        mins = str(mins) + " PM"
    else: 
        mins = str(mins) + " AM"
    time = str(hour) +":" + mins
    return time
         
    
def printResults(answer):
    if answer == "spreads":
        
        printSpreadResults()
    elif answer == "ml":
        
        printMLResults()
    
    else: 
        print("what")


def printSpreadResults():
  
  # gets reults ready to tweet out
    teams = SprnewList[0].awayTeam + " vs " + SprnewList[0].homeTeam.upper() + "\n"
    
    string = teams + timefix(SprnewList[0].dTime) + "\n" + "\nSpreads:\n\n"
    
    k = 1
    for matchup in SprnewList:
        
        aprice = addPlusTo(matchup.awayPrice)
        apoint = addPlusTo(matchup.awaySpread)
        hprice = addPlusTo(matchup.homePrice)
        hpoint = addPlusTo(matchup.homeSpread)
        
        string = string + matchup.sportsbook + "\n" + matchup.awayTeam + ": " + apoint + " " + aprice + "\n" + matchup.homeTeam + ": " + hpoint + " " + hprice + "\n\n"
        
        if k == 4:
            break
        k = k+1
    string = string +"\n#mlb"
    #print(string)
    print("Length: " + str(len(string)))
    publictweet(string)
    SprnewList.clear()
    
def printMLResults():
  
  # gets reults ready to tweet out
    teams = MLnewList[0].awayTeam + " vs " + MLnewList[0].homeTeam.upper() + "\n"
    
    string = teams + timefix(MLnewList[0].dTime) + "\n\n" + "MoneyLines:\n\n"
    
    k = 1
    for matchup in MLnewList:
        
        aml = addPlusTo(matchup.aML)
        hml = addPlusTo(matchup.hML)
        
        string = string + matchup.sportsbook + "\n" + matchup.awayTeam + ": " + aml + "\n" + matchup.homeTeam + ": " + hml + "\n\n"
        
        if k == 4:
            break
        k = k+1
    string = string +"\n#mlb"
    #print(string)
    print("Length: " + str(len(string)))
    publictweet(string)
    MLnewList.clear()
