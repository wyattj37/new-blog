+++
title = "Making a Machine Learning Model for Tennis Betting Part 1: The Model"
date = "2024-08-14"
tags = [
    "sports",
    "betting",
    "machine learning"
]
draft = true
hiddenInHomeList = true
+++
Creating a machine learning model that predicts tennis matches efficiently enough to bet on them profitably.  <!--more-->

# Setting the Baseline
I’ve found a fair number of attempts online to predict tennis matches with ML models. There were two that I liked quite a bit: a masters dissertation from the University of Ghent found [here](https://libstore.ugent.be/fulltxt/RUG01/002/945/727/RUG01-002945727_2021_0001_AC.pdf) and [Github repository](https://github.com/BrandoPolistirolo/Tennis-Betting-ML) with 27 stars. I was unable to find the code for the dissertation posted anywhere, but the paper is awfully explicit in its 54 pages, which will be helpful. Some serious publications I found actually trained their models on in-match data, which I thought was pretty funny. They achieved 90% accuracy or more because the model was using information like how many points each player won that match, which is unsurprisingly helpful in determining the winner.

As seen in the dissertation, using just ATP rating to predict the winner of a match gets you 64.5% accuracy. Objective #1 is to beat that, or else what was really the point. The 27 star Github repository “achieves a 66% accuracy rate.” Objective #2 is to beat that, because otherwise I could’ve just used the code publicly available. Finally, the dissertation’s best performing neural network achieves 68.2% accuracy. The lofty Objective #3 is to beat that. Admittedly that could be difficult, but I have a few ideas on where to start.

# Feature Selection
Each match will be stored as a collection of features on player 1, player 2, the environment, and then the result. The first feature is a [Glicko-2 rating](https://en.wikipedia.org/wiki/Glicko_rating_system), which is like ELO but with three variables: rating, rating deviation, and rating volatility. The next features all revolve around the number of wins and losses: total, each surface (hard, clay, grass, carpet), each match length (best of 3 or 5 sets), head-to-head, and each opponent handedness (left, right). The physical descriptions of the players, age and height, are also added. There is another feature for how many days ago their last match was, hopefully to indicate if they have spent time off for an injury or are otherwise out of practice. Of course the features describing the match, either best of 3 or 5 and the surface, are included as well. 

Finally, my most original contributions, I wanted to incorporate some features on serving, returning, and break points. I think the stats that make the most sense are % won on first serve, % won on second serve, % won on first return, % won on second return, % breaks points saved (serving), and % break points won (returning). I hope this can capture some of the parts of an individual player’s game that changes how they stack up against another opponent. For example, if there are two players that are completely equal except one has a serve slightly better than the other, you’d expect the better serving player to win. But if the player who has a slightly worse serve also has a slightly better return, the balance could change.

To me, including ace and double fault averages is redundant because those things directly impact first and second serve win percentages, but that could be an oversimplification. Speaking of things I did not include: I opted not to include home advantage and the number of matches in the past few weeks. The former is because only the tournament name is included in the original data and I haven’t felt like dealing with another data set to convert that to countries, although I’m sure there is some impact it would have. The latter is because, on the tour, you are going to have lots of players with similar schedules, and I don't think the fatigue it causes will either be significant or vary greatly between players.

# Data Processing + Feature Extraction
Note: I am using Jeff Sackmann’s [excellent ATP match database](https://github.com/JeffSackmann/tennis_atp) on Github.

Now all that’s left to do is clean up the data and create the features we want. The data set available provides matches from the ATP Tour as well as the lower level tournaments, Challengers and Futures. I opted to leave out the lower level tournaments, challengers and futures, from feature extraction and training. I left them out of training because creating the training data turned out to be rather computationally expensive, which I’ll get into shortly. As for feature extraction, I’m sure there are cases where players spent years at the Challenger level, and that data could potentially be helpful. However I also think that, for almost all cases, the player is also going to have quite a few ATP Tour matches, the data from which is more relevant.

The tricky part is you only want each match’s features to be from prior to the match taking place. You can’t just define a player’s wins as the total number of wins in the data and then use that for each match they play - you would be using data from the future. To combat this I loaded in 15 years of players’ statistics from 1995 to 2009 all at once with the intention not to use it for any training. Then, for each match from 2010 on, I created the features for that match given the available data, then updated each player’s statistics to be used in the future. There are almost 40,000 matches from 2010 to now. Updating the features one match at a time already took long enough without any of the Challenger or Future matches, of which there are even more than ATP Tour matches, hence why I left them out of training.

# Creating the Models
The first model will be a simple logistic regression imported from sci-kit learn. The logistic regression model achieves objectives #1 and #2 with a 67.8% test accuracy (which I might note is higher than the referenced dissertation). Scaling the features made a significant difference in the logistic regression accuracy, and I do so for the neural network too.

The neural network built using Keras is a simple one. In a few tests with multiple layers the model performed very poorly, so I stuck with using one “Dense” layer. The layer has 256 units and ReLu activation. Then there’s a dropout layer at 50%, then a sigmoid activation layer. I used the Adam optimizer with 0.0005 learning rate, a batch size of 128, and 25 epochs. Because there are two classes, it uses binary cross-entropy loss. I used a broad grid search to get a ballpark of the number of units, learning rate, batch size, and epochs, and then tweaked it from there.

After all the setup, we finally achieved 69.2% accuracy! Objective #3 complete. To be clear, I am training and testing on all matches 2010-2024. Depending on the random split of training/test data, the test accuracy can fluctuate by plus or minus 1.0%(ish), and the same goes for the logistic regression model. The task itself is very random so I’m not taking that to be an issue with the model. Here's an overall summary:

| Model | Accuracy   |
|------|------------|
| Logistic regression | 67.8%  |
| Neural Network | 69.2%    |

In all fairness to the research paper I’ve referenced, it uses only years 2016-2019 for testing, and 2017 seems to be a bad year for prediction. Whenever I quickly trained and tested for those years only, my results were:

| Year | Accuracy   |
|------|------------|
| 2016 | 70.2%      |
| 2017 | 66.0%      |
| 2018 | 68.5%      |
| 2019 | 68.3%      |

Once again these could fluctuate, but, on average, the model performed better in the years before and after this timeframe.

# Onto the Next
I’m hoping that 69.2% is enough of an edge to squeak out some profit over time. My estimation is that it will be close, but with a sound betting system it could work. In the next part I will spend some time investigating different betting systems and see how the model does.