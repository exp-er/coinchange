#Coin Change\
import sys
import pyarrow as pa
import streamlit as st 

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
    st.title("Coin Change Program")
    Total=int(st.number_input('Enter Amount Paid:',1))
    cost=int(st.slider('Enter Cost', 0, Total))
    amnt = Total-cost
    curr=st.selectbox('Pick one', ['Indian Rupee', 'British Pound','American Dollar',"European Euro","Chinese Yuan","Japanese Yen"])
    if(curr=="Indian Rupee"): clist = [1,2,5,10,20,50,100,200,500,2000]; st.image('./rupee.png')
    if(curr=="British Pound"): clist = [1,2,5,10,20,50]; st.image('./pound.png')
    if(curr=="American Dollar"): clist = [1,2,5,10,20,50,100]; st.image('./dollar.png')
    if(curr=="European Euro"): clist=[1,2,5,10,20,50,100,200,500]; st.image('./euro.png')
    if(curr=="Chinese Yuan"): clist=[1,2,5,10,20,50,100]; st.image('./yuan.png')
    if(curr=="Japanese Yen"): clist=[1,5,10,50,100,500,1000,2000,5000,10000]; st.image('./yen.png')
    
    coinsUsed = [0]*(amnt+1)
    coinCount= [0]*(amnt+1)
    coin_list=[]
    st.write("Making change for",amnt,curr,"requires")
    st.write(dpMakeChange(clist,amnt,coinCount,coinsUsed),"Coins")
    st.write("They are:")
    printcoins(coinsUsed,amnt,coin_list)
    coin_change = {item:coin_list.count(item) for item in coin_list}
    for coin,value in coin_change.items():
        st.write(str(coin) + " x " + str(value) + " " +curr)    
    
main()

