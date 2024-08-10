+++
title = "Game Theory and Probabilistic Strategies in '(Screw) the Dealer'"
date = "2024-07-03"
tags = [
    "drinking games"
]
math = true
+++
Turning a light-hearted, fun drinking game into a math problem.

<!--more-->
# Overview of the Game
The rules to the game can be found [here](https://www.drinkinggames.co.uk/fuck-the-dealer-drinking-game.php). In this version of the game, the first guess is worth 5 drinks to the dealer if correct, and the second is worth 2. If the second guess is wrong, the guesser drinks the difference. For simplificaiton, I'll first look at a version where every guess is just worth one drink, and then return to the original.

# Making Guesses in The Simple Version
In the simple version, everything worth one drink, all the guesser wants to do is be correct on either the first or second guess. In order to do that optimally, the process is as follows: identify the three most available cards left in the deck. Make your first guess the middle card of those three. Your second guess will be one of the other two cards based on whether you are told higher or lower.

As an example, suppose there were four 2s, three Jacks, and two Queens unaccounted for. And suppose there is only one of every other card unaccounted for. Your first guess would be Jack, because that is the middle of the three most likely cards. Based on whether you are told higher or lower, you would then guess Queen or 2, respectively.

The probability of guessing the card on any complete turn boils down to:
$$
\frac{\scriptstyle{\text{(number available of first guess)} + \text{(number available of "higher" guess)} + \text{(number available of "lower" guess)}}}{\scriptstyle{\text{total cards in the deck}}}
$$
So in the above example, because there are three Jacks (first guess), two Queens (higher guess), and four 2s (lower guess) available, the probability comes out to be
$$
\frac{3 + 2 + 4} { 20 } = \frac{9}{20}
$$
Notice that, counterintuitively, if we were to have chosen the most likely card initially, the 2, we would have decreased the probability of guessing correctly to 
$$
\frac{4 + 2 + 1} { 20 } = \frac{7}{20}
$$
because there is only one of our “lower” guess (the Ace). So the most likely card is not always the best guess.

# Making Guesses in the More Common Version
Back to the version where the first guess is worth 5 drinks to the dealer, the second is worth 2, and the guesser drinks the difference if wrong twice. Now the problem is not as simple as being right on either the first or second guess. In an effort to get the dealer more screwed, you are incentivized to guess a more likely card first despite it not necessarily maximizing your chances of being right overall. In an effort to drink less if your second guess is wrong, you are incentized to make a guess where the difference is potentially smaller.

How to balance the goal of maximizing drinks to the dealer and minimizing drinks to yourself? We can assign a positive value to drinks taken by the dealer and a negative value to drinks taken by the guesser, then find the expected value of each potential combination of guesses. The only final problem to remedy is that a drink taken may not be equal in value to a drink given. In the code I’ve included a “selflessness” weight that assigns how much you value giving drinks to the dealer compared to taking 1 drink. For example, if you don’t care about giving drinks to the dealer that much, and taking 1 drink is equal in value to you as giving 5 drinks, the weight would be 1/5 = 0.2. If you really value giving out drinks and each 1 given drink is worth 5 taken drinks, the weight would be 5/1 = 5.

# Probably Just Skip This Section
We want to find
$$
EV_{\text{total}} = \text{(selflessness weight)} \cdot EV_{\text{dealer}} - EV_{\text{guesser}}
$$
For conciseness the following symbols mean:
| Variable   | Description                                    |
|------------|------------------------------------------------|
| g1         | first guess is correct                         |
| g2,h       | second, higher guess is correct                |
| g2,l       | second, lower guess is correct                 |
| higher     | true card is higher than first guess           |
| lower      | true card is lower than first guess            |
| Hval       | higher guess value (e.g., “King” = 12 or 9 = 9)|
| Lval       | lower guess value                              |
| Fval       | first guess value                              |

The expected value of the amount of drinks you give to the dealer is:
$$
EV_{\text{dealer}} = 5 \cdot P(g1) + 2 \cdot P(\neg g1) \cdot [ P(higher) \cdot P(g2,h) + P(lower) \cdot P(g2,l) ]
$$

The expected value of the number of drinks you take is:
$$
EV_{\text{guesser}}  = P(\neg g1) \cdot [(Hval - Fval) \cdot P(higher) \cdot P(\neg g2,h) + (Fval - Lval) \cdot P(lower) \cdot P(\neg g2,l) ]
$$

We can plug these two values back into the total EV equation and get the value we want.

# Using the Guess Calculator
In the code found on GitHub, the cards are represented as a list of how many are left in the deck. So if there are 4 Aces and 1 King left in the deck, the cards list should be updated to [4,0,0,…1]. That is the only input necessary to run the function which returns the optimal guesses in the form [first_guess, lower_guess, higher_guess]. The selflessness coefficient can be tweaked as well to the preference of the user.

The code cycles through each combination of two guesses, calculates the EV, and stores the set of guesses that produces the highest value. There are relatively few combinations, so brute-forcing all of them runs perfectly quick and nothing fancier is required.

As a note, unless the selflessness weight is very high, the code will usually suggest playing it safe with 3 cards near each other as the guesses. In some cases it will even accept defeat and suggest sets of guesses with cards no longer in the deck. This makes intuitive sense in that guaranteeing 1 drink is sometimes better than risking a small chance of 4 or 5 or up to 12 drinks. Depending on the order of the guesses, the code might also suggest a 100% chance of 1 drink as opposed to a 50% chance of 2 drinks, so I included a step that prefers at least some probability of 0 drinks if possible.