+++
title = "Making a Machine Learning Model for Tennis Betting Part 2: The Betting (Work in Progress)"
date = "2024-09-01"
tags = [
    "sports",
    "betting",
    "machine learning"
]
+++
Deploying the model built in Part 1 to a betting scheme to see what kind of money can (hypothetically) be made. <!--more-->

# Choosing the Timeframe and Model Usage
I’ll be using the neural network from part 1 and the years 2021-2024 for testing betting strategies. In order to keep the model from seeing any data from the future, I will only train it on matches from the past. Every 1000 bets made I will retrain the model to include the matches that "just happened". I’m interested in re-training the model at the start of every tournament (as opposed to an arbitrary number like every 1000 matches), but I will come back to that another time.

# The Data
The betting odds data comes from [here](http://www.tennis-data.co.uk/alldata.php). The files were sort of a hassle to combine because the tournament names and player names aren't stored the same, so some matches were lost when combining the betting data with the model data. Also the ATP Tour match data was more robust than the betting odds data, so the matches which didn't overlap were also lost. I'll be using the best odds given for either the favorite or underdog, as I imagine any good sports bettor would. It's important to be careful of keeping the odds data separated from the feature data, as a mixture of the two would obviously lead to biased results. 

# The Betting Strategy
The [Kelly criterion](https://en.wikipedia.org/wiki/Kelly_criterion) is a method of bet sizing which has been popular for a long time. In essence, you want to bet more on games where you either stand to win a lot or have a high probability of winning, and bet less otherwise. The formula, in which f* is a fraction of your bankroll, is given by:

<div style="text-align: center;">
  <img src="/images/tennis/kelly.png" style="width:35%;">
</div>

There are two variations of the Kelly criterion that I will be testing. The first is the Half-Kelly, which just divides the formula above by two. Simple enough - smaller bets are more prudent. The other variation comes from a [paper by Baker and Mchale](https://www.researchgate.net/publication/262425087_Optimal_Betting_Under_Parameter_Uncertainty_Improving_the_Kelly_Criterion). I recommend you check it out, it’s a bit dense for getting into here. But the formula for f* (k*) becomes:

<div style="text-align: center;">
  <img src="/images/tennis/kelly2.png" style="width:40%;">
</div>

You'll notice the σ term, wich represents the error variance of the predictions. Different values for this parameter will have to be expiremented with to see which yields the best results.

The last component of the betting strategy is when to make a bet. You don't have to bet on everything - choosing to skip matches below a confidence threshhold can  only matches in which your estimated probability from the model differs significantly enough from the bookmaker's odds to be profitable.

# Oops! Data Leak
Remember when I said it was important to keep the model from training on matches it was going to predict? Well I messed that up. Or I created the greatest tennis betting model ever with 140x returns. But I definitely messed it up. Here's what my simulated bankroll(starting at 10,000) over time looked like:

<div style="text-align: center;">
  <img src="/images/tennis/bad-graph.png" style="width:80%;">
</div>

For the first 2000 matches it does about how you'd expect: some ups and downs but hovering around even. Then comes a seemingly impossible climb including some huge upswings all the way up to 140,000. What I'm assuming happened is whenever that second re-training occurred a handful of matches from the future leaked into the training matches. The model was therefore extremely confident on these matches and made huge, correct bets. I'll have to revisit the way I sorted and merged the betting line data and the match data. Back to the drawing board...