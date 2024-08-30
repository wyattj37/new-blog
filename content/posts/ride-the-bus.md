+++
author = "Hugo Authors"
title = "Riding the Bus: A Ballistics Report via Monte Carlo Simulation"
date = "2024-06-30"
tags = [
    "drinking games"
]
+++

How many drinks will a person take while riding the bus? In short: a lot. <!--more-->

# How it Works
You can find the rules to the game [here](https://drinkinggamezone.com/drinking-games/ride-the-bus/). The linked article explains the initial phases of the game, as well, but I will mostly be looking at the final phase - the riding of the bus.  The only discrepancy is that this article claims the bus ride [stops at the end of the deck](https://www.amazon.com/Charmin-Ultra-Bathroom-Tissue-White/dp/B086D4VR9M). In the version of the game studied hereafter, at that point the deck is reshuffled and the bus starts back up, only stopping after 4 consecutive correct answers.

# The Approach
My approach was to build a simulation of the game, then run the simulation a bunch of times and track the results. Or a Monte Carlo simulation if you're feeling fancy. The code is available on my GitHub for an in-depth look, but essentially a list of integers acts as a deck of cards and the computer makes guesses just like a person would. If the computer gets it wrong, it takes a sip (drink_count++) and the round goes back to "red or black".

How does the computer determine what guess to make? Just like a person, it makes the more likely guess. If there is a low card during the "Higher/Lower" round, it guesses higher. If the cards during "Inside/Outide" are far apart, it guesses inside. In addition to this, I added a feature called the "memory" that keeps track of some number of the previous cards turned over. This influences the computer's guess, i.e. if the memory is set to store the last 3 cards, and all 3 were red cards, it will choose black on the next "Red/Black" round. In theory, this is meant to mimic the way a human can use seeing the previous cards to their advantage. In practice, a participant is unlikely to play the game this accurately. But, as will be discussed later, the memory has a surprisingly small impact on the success of the round anyways.

# Results
In summary, riding the bus results in taking about 13.5 drinks on average if you’re playing accurately. If you count duplicate cards as being wrong during "Higher/Lower" and "Inside/Outside", the average goes up 1 drink. The distribution of 100,000 simulations can be seen below. 

<div style="text-align: center;">
  <img src="/images/bus-ride-dist.png" alt="Probability of number of drinks taken per bus ride." style="width:50%;">
</div>

What we see from the distribution is what makes the game popular: about 50% of the time you'll wind up in the 0 to 10 drink range. About 25% of the time you'll be within 10 to 20 drink range - a little heftier. But for the final damaging 25%, you'll be in the 20s, 30s, or more. Some of the simulations even reached past 100 drinks (at which point my computer got its stomach pumped). 

I mentioned before that the memory plays only a small role in the player's success. In a set of simulations I ran with a perfect memory, that is the computer is using every single card played to make the most accurate guess, the average number of drinks only drops from 13.5 to 10. That’s because, even with a savant's memory, you only get more information as you lose more rounds. Once you’ve seen most of the deck you can make very accurate guesses, but at that point it's already too late.

# The Other Phases
The other phases of the game are interesting, but the rules vary so greatly from person to person they are less useful to analyze. However, one general approach is to assume the drinks are given out randomly. Under that assumption, you can think of these rounds as being a pool of drinks that everyone will share evenly. Say in the first phase each card is worth 1 drink to give or take if you are right or wrong, then the second is worth 2, and so on. If there are 5 people playing, there are 5*(1+2+3+4) = 50 drinks to be taken in total. So everyone can expect about to take an even share of that pool, or 50/5 = 10 drinks. The pyramid phase is a little more tricky but the same logic could give a decent estimate.