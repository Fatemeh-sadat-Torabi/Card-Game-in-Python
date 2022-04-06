# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 02:34:06 2022

@author: FARZANE.T
"""
import random
Suits=['Clubs','Diamonds','Hearts','Spades']
Ranks=['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
##### How to generate a card randomly - first way with randrange():
suit=random.randrange(0,len(Suits))
rank=random.randrange(0,len(Ranks))
print(Ranks[rank]+' of '+Suits[suit])
##### How to generate a card randomly - second way with choice():
rank=random.choice(Ranks)
suit=random.choice(Suits)
print(rank+' of '+suit)

##### Create 52 card (13*4=52) and store them in deck[].
deck=[]
for rank in Ranks:
    for suit in Suits :
        card = rank + ' of '+suit
        deck += [card]
print(len(deck))
##### Now it is time to shuffle these cards using shuffle algorithm by Donald Knuth :
print('\n Cards before shuffeling: \n')
print(deck) 
print('\n Cards after shuffeling: \n')
for i in range(len(deck)):
    r = random.randrange(0,i+1)
    temp=deck[i]
    deck[i]=deck[r]
    deck[r]=temp
print(deck)
##### How to give some cards randomly to gamers without repeat- using donald knuth shuffling-:
import sys
m =6 # int(sys.argv[1])
n =16# int(sys.argv[2])

perm = [i for i in range(n)]
for i in range(m):
    r = random.randrange(i,n)
    perm[i],perm[r] = perm[r],perm[i]
    
for i in range(m):
    print(str(perm[i]),end=' ')
print()
##### Coupen Collector Problem - using monte carlo :
##### How many random selection is needed to be sure at least one of each suits or one of each ranks are choosen?!!!
print('\n')
total_mc_count = 0
mc_repeat = 100
for i in range(mc_repeat):
    n=13# sys.argv[3]           13 for Ranks! 4 for suits ! or other arbitrary numbers of objects for general
    count = 0
    collected_count = 0
    is_collected = [ False ] * n # It is a boolean array
    while (collected_count < n):
        count +=1
        r= random.randrange(0,n)
        if not is_collected[r]  :
            is_collected[r] = True
            collected_count += 1
    print (count)
    total_mc_count += count
average_count=total_mc_count/mc_repeat 
print('\n')
print(average_count)
##### coupen collector has a formoula as a theory answer : n(1/1 + 1/2 + 1/3 + 1/4 + ... +1/n)~ n*ln(n). So for large mc_repeat
##### the average_count will be near to n*ln(n)


   
    

    
        
