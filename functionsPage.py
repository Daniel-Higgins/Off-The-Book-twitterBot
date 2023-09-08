import json
from twitterBot import publictweet
from datetime import datetime
from bookDictionary import websites
import dateutil.parser
import pytz


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
sbook = []
def sortSOddsH(x):
    arrayj = x
    #debugging matchup variable calls
    if arrayj:
        omax = arrayj[0].homePrice
        mbj = arrayj[0]
        for i in arrayj:
            if i.homePrice > omax:
                omax = i.homePrice
                mbj = i
        SprnewList.append(mbj)
        arrayj.remove(mbj)
        
        sortSOddsH(arrayj)
        
        
def sortSOddsA(x):
    arrayj = x
    #debugging matchup variable calls
    if arrayj:
        omax = arrayj[0].awayPrice
        mbj = arrayj[0]
        for i in arrayj:
            
            if i.awayPrice > omax:
                omax = i.awayPrice
                mbj = i
        SprnewList.append(mbj)
        arrayj.remove(mbj)
        
        sortSOddsA(arrayj)
        
def sortMLa(x):
    arrayj = x
    #debugging matchup variable calls
    if arrayj:
        omax = arrayj[0].aML
        mbj = arrayj[0]
        for i in arrayj:
            
            if i.aML > omax:
                omax = i.aML
                mbj = i
        MLnewList.append(mbj)
        arrayj.remove(mbj)
        sortMLa(arrayj)  
def sortMLh(x):
    arrayj = x
    #debugging matchup variable calls
    if arrayj:
        omax = arrayj[0].hML
        mbj = arrayj[0]
        for i in arrayj:
            
            if i.hML > omax:
                omax = i.hML
                mbj = i
        MLnewList.append(mbj)
        arrayj.remove(mbj)
        sortMLh(arrayj)
        
        

def sortBook(x):
    arrayj = x
    #debugging matchup variable calls
    omax = 0
    team=""
    oper = ""
    if arrayj:
        mbj = arrayj[0]
        if arrayj[0].awayPrice > arrayj[0].homePrice:
            omax = arrayj[0].awayPrice
            team = arrayj[0].awayTeam
            oper = arrayj[0].awaySpread

        else:
            omax = arrayj[0].homePrice
            team = arrayj[0].homeTeam
            oper = arrayj[0].homeSpread
     
        if omax < arrayj[0].aML:
            omax = arrayj[0].aML
            team = arrayj[0].awayTeam
            oper = "ML"
        if omax < arrayj[0].hML:
            omax = arrayj[0].hML
            team = arrayj[0].homeTeam
            oper = "ML"
  
        for i in arrayj:
            comp = 0
            cteam =""
            coper = ""
            if i.homePrice > i.aML:
                comp = i.homePrice
                cteam = i.homeTeam
                coper = i.homeSpread
                
            elif i.aML > i.homePrice: 
                comp = i.aML
                cteam = i.awayTeam
                coper = "ML"
                
            if i.hML > comp:
                comp = i.hML
                cteam = i.homeTeam
                coper = "ML"
            if i.awayPrice > comp:
                comp = i.awayPrice
                cteam = i.awayTeam
                coper = i.awaySpread
            if omax < comp:
                omax = comp
                team = cteam
                oper = coper
                mbj = i
        
        sbook.append(team)
        sbook.append(oper)
        sbook.append(omax)
        arrayj.remove(mbj)
        sortBook(arrayj)
    else:
        return sbook

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
        answer += "Final odds: " + str(addPlusTo(int(finalOdds))) + "\n\n" + "Risk $100 to win $" + str(int(finalOdds)) +"\n\n" + "#nfl" + "\n"
        
        answer += "Bet it now here: " + websites[t]
        #print(answer)
        return answer
    
    
    
    
    
def timefix(x):
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
    string = string +"\n#nfl"
    print(string)
    print("Length: " + str(len(string)))
    #publictweet(string)
    SprnewList.clear()
    
def printMLResults():
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
    string = string +"\n#nfl"
    print(string)
    print("Length: " + str(len(string)))
    #publictweet(string)
    MLnewList.clear()

def publishCMP(z):
    #publictweet(z)
    print(z)
    print("Length: " + str(len(z)))
