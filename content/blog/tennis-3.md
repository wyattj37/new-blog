+++
title = "Revisiting the Tennis Model: The 4 Factors Approach"
date = "2025-04-15"
math = true
tags = [
    "sports",
    "betting",
    "statistics"
]
draft = true
hiddenInHomeList = true
+++
Foregoing newfangled learning methods and going back to the basics.
<!--more-->

# Mild Success
In the past, I've made a couple of posts about models I made for predicting tennis outcomes. The idea was to congregate information from matches, turn it into a giant set of features and throw the data into a machine learning library to train. The outcome, I hoped, would be a neural network encoded with all the answers. Which sort of happened but not really. The accuracy was sort of impressive, but the model was unstable. And it was clear that there were cases of the outputted probabilities just *feeling off*. With this sort of model, though, there's of course no way to see what's going on under the hood and tweak it.

# A New Approach: Two Inspirations
That brings me to my new approach. It seemed to me that a [Four Factors](https://www.basketball-reference.com/about/factors.html) type metric might make sense for tennis. Some way of segmenting the game into a few key stats. There are 4 outcomes of a tennis point: the server wins on the first serve, loses on the first serve, wins on the second serve, or loses on the second serve (I am counting aces as being included in the first category and double faults as being included in the last). If we had a good calculation of those 4 probabilities, we would be able to simulate tennis games quite effectively.

Another inpsiration I've been thinking about is the handicapping system proposed by Billy Walters in his memoir "Gambler". The system he describes is for football, and begins with giving each team a power rating from -10 to 10. To find the point spread, you subtract the power ratings, then account for different factors that hold different point spread values. Home field advantage would be a positive point spread addition, while having to travel coast-to-coast would have a negative point spread effect. On top of that, he keeps a database with the value of each player in point-spread terms. In tennis terms, I am imagining using an ELO system - perfect for two players and I already have one implemented. Then, the ELO results can be adjusted based on factors like surface, handedness, etc. if it seems necessary.

# Making the New Model
As we start the first approach (the simulation approach), we need to broach an interesting problem. It's easy enough to calculate a player's win percentage on their 1st serve. Let's say it's 75% for Player 1. It's also easy enough to calcualte a player's win percentage returning their opponent's first serve. Let's say that's 30% for Player 2. When Player 1 serves to Player 2, though, which percentage do we use? They can't both be true.

I am going to try and remedy this by calcualting a weighted average, where the weight assigned to each is a parameter learned through previous data. P(P1 wins 1st serve) = .75 $\cdot$ alpha + (1 - .30) $\cdot$ (1-alpha). I will do this for the alpha parameter 