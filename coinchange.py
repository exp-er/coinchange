#Coin Change

def dpMakeChange(coinValueList,change,mincoins,coinsUsed):
    for counts in range(change+1):
        coinCount = counts
        newcoin = 1
        for j in [c for c in coinValueList if c <= counts]:
            if mincoins[counts-j] + 1 < coinCount:
                coinCount = mincoins[counts-j]+1
                newcoin = j
            mincoins[counts] = coinCount
            coinsUsed[counts] = newcoin
    return mincoins[change]

def printcoins(coinsUsed,change,coin_list):
    coin = change
    while coin > 0:
        thiscoin = coinsUsed[coin]
        coin_list.append(thiscoin)
        coin = coin - thiscoin

def main():
    Total=int(input("Enter amount paid:"))
    cost=int(input("Enter cost of item:"))
    amnt = Total-cost
    clist = [1,2,5,10,20,50,100,200,500,2000]
    
    coinsUsed = [0]*(amnt+1)
    coinCount= [0]*(amnt+1)
    coin_list=[]
    print("Making change for",amnt,"requires")
    print(dpMakeChange(clist,amnt,coinCount,coinsUsed),"Coins")
    print("They are:")
    printcoins(coinsUsed,amnt,coin_list)
    coin_change = {item:coin_list.count(item) for item in coin_list}
    for coin,value in coin_change.items():
        print("Rs." + str(coin) + " x" + str(value))    
    
main()

