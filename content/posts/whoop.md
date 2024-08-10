+++
title = "How Much HRV Matters in Calcuating WHOOP Recovery Scores"
date = "2024-07-11"
tags = [
    "Machine Learning",
    "Health"
]
+++
Heart rate variability (HRV) is the primary metric that the WHOOP fitness band uses to calculate your recovery. In this article I look at just how much HRV contributes to recovery, plus how a high HRV variance can make things tricky.
<!--more-->
# What is a WHOOP Recovery Score
The WHOOP fitness band is a product that tracks your activity throughout the day by measuring primarily your heart rate. In addition, and more importantly, it tracks your recovery during sleep. The WHOOP website (and my personal experience) will tell you HRV is the primary contributer to calculating recovery. What exactly HRV is and why it's so important is something I surely will explain worse than WHOOP themselves, so find out more about that [here](https://www.whoop.com/us/en/thelocker/heart-rate-variability-hrv/).

Luckily WHOOP allows you to export your data, which includes a daily value for quite a few metrics. These include resting heart rate, blood oxygen %, energy burned in calories, time in bed, light sleep, REM sleep, and more. All of these features, including HRV, are inputs to the model that calculates recovery score. By using this data, something of a crude recreation of the recovery score model can be made. Of course it won't be perfect, but by using data from both myself and a friend, it suffices to provide some useful insight as to how HRV specifically plays its part.

# Investigating the Features
I'll use a few different methods to find out the relative importance of each of the features. The first is a linear regression with L1 regularization. Using this shows which features have coefficients that don't trend to 0, and that can gives a decent idea of which handful of features are of the most importance. The next is using a GBM model and extracting the feature importance, measured on the contribution to reducing error. The last is permutation importance. This is newer to me, but, as I understand, the function shuffles the feature values of a model randomly and the more important features are the ones which cause the model to perform worst when shuffled.

The code for each of these can be found on GitHub. I don't link my own data because that feels sort of weird to put online, but if you are a WHOOP user you can put the filepath to your own "phisiological_cycles.csv" from the WHOOP data export. The results I found are similar amongst each of the different approaches. The LR with L1 regularization shows HRV is about 9 times as impactful as the next most important feature (light sleep duration) out of 5 contribution features. The GBM feature importance has HRV as accounting for 90% of the importance with light sleep duration at 4.3%. The permutation importance calcualtes HRV at about 97% for both the GBM and linear model.

# The (Potential) Problem With a High HRV Variance
What's unique, and potentially misleading, about my particular data is that my HRV has a very high variance. This is due to, let's say, lifestyle choices. Because an n=1 sample size is bad practice, I also use another WHOOP user's data to assemble a doubly robust n=2 sample size. For reference, this WHOOP user's HRV variance is calculated to be 303.3, whereas mine is 1981.2. Using the same methods as before on the lower variance HRV dataset, it was seen that HRV played a smaller, albeit still majority, role in recovery score. The LR coefficient of HRV was about 5.5 times higher than the next, and the GBM significance was only 75%. Seemingly because the models trained with this data could not rely so heavily on HRV, the test performance was also lower.

This discrepancy is what originally led me to conduct this study: I noticed my HRV can hit high extremes, and my recovery would correspondingly be high despite poor or little sleep. But is that an accurate representation of my body's recovery? Or is it just inflated because the variance of my HRV is greate? In addition, my average HRV (125.4) is quite a bit higher than the other dataset (70.6). It's possible that there is a bias in the model towards a HRV that is simply larger.

I am sure more considerations are taken into calculating the recovery score than I could possibly be aware of. I would assume that data beyond just one value per day is involved in the model as well. Perhaps the HRV is taken at different points throughout the night which aren't available in the data export. Regardless, the bottom line is that a high HRV is overwhelmingly the preeminent factor in a good recovery score.