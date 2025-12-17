+++
title = "The Birthday Problem for Last Names"
date = "2025-03-01"
tags = [
    "statistics",
    "probability"
]
math = true
featured = true
weight = 2
hiddenInHomeList = true
+++
How large of a group do you need so that the chances of two random people sharing a last name is 50%?  <!--more-->

The [birthday problem](https://en.wikipedia.org/wiki/Birthday_problem) “asks for the probability that, in a set of n randomly chosen people, at least two will share the same birthday.” In order to achieve a probability of 50%, only 23 people are needed, which is a surprisingly low number.

Recently I was looking through a class roster and noticed there were 4 Chens out of 90 people in the section. Remembering the birthday problem, I wondered what the probability was in a set of n random people that two would have the same surname. TLDR: with a group of 50 there is about a 50% chance of a shared last name. Before I get into how we come to that result, the data I’ll be using comes from the 2010 US census. The data can be found [here](https://www.census.gov/topics/population/genealogy/data/2010_surnames.html). 

The big difference between the birthday problem and the surname problem is that birthdays are ([more or less](https://www.panix.com/~murphy/bday.html)) distributed evenly, so the probability of any given birthday being 1/365 is a fine assumption. Surnames, on the other hand, are definitely not evenly distributed. The top 100 names constitute ~17% of the population, the top 1000 constitute ~41%, and the 100,000 most popular names constitute ~87% of all Americans (in 2010). Meanwhile, there were 6.3 million(!) total surnames reported in the 2010 census. In fact, 3.6 million surnames were only reported once. The distribution of names is extremely weighted towards the popular ones.

Here is a visualization of that:
<div style="text-align: center;">
  <img src="/images/surnames/top_250.png" style="width:100%;">
</div>

Even the 250th most popular last name (Morrison) has only 1/20th the number of instances as the most popular name (Smith).

Another implication of this is that as you go to the other far end of the distribution, you get lots of names that appear the same number of times. For example, there are 96 surnames that appear exactly 300 times, and there are 1,279 surnames that appear exactly 100 times. Remember, there are also 3.6 million surnames that appear exactly once. 
Here is a plot of that relationship for names that appear fewer than 600 times:
<div style="text-align: center;">
  <img src="/images/surnames/bottom_600.png" style="width:100%;">
</div>

A few things to realize about this. First of all, the y-axis is a log scale. There are way, way more names that appear once (3.6 million) than appear even 100 times (1,279). Second of all, where is the data between 2 and 99 appearances? Presumably because that would result in a spreadsheet with millions of rows, the US Census Bureau decided they don’t want to include that in the .csv file. Understandable, but a little bit of a hassle moving forward.

My big idea was to simulate this problem. I’ll get into how exactly later, but to do so I need to fill in the 2-99 gap. Here’s what we know from the census data:
 - There were 294,979,229 people sampled in total
 - The names that appear more than 99 times constitute 265,667,228 people
 - The names that appear once constitute (about) 3,906,000 people
 - That leaves us with 25,406,001 total people with 2-99 appearance surnames.

Further, we know that:
 - 162,253 names appear more than 99 times
 - 6.3 million surnames were recorded in total
 - 3.906 million surnames were recorded once
 - That leaves us with 6,137,746 surnames in the 2-99 appearance category.

So the gap represents 25,406,001 people with 6,137,746 different names. Going forward I will write $a_n$ to represent how many names there are with n appearances. For example, $a_{100}$ = 1,279 because there are 1,279 surnames that appear 100 times. We can write the requirements above as follows:


$$ \sum_{n=2}^{99} n \cdot a_n = 25,406,000 $$  from the total people requirement, and 

$$ \sum_{n=2}^{99} a_n = 6,137,746 $$ from the total number of names requirement.

From the second graph the relationship looks pretty exponential, and there are nice closed-form equations we can write for the sums above, so let’s give that a shot.

In general, when
$$a_n=a_1 \cdot r^{n-1}$$
as in a geometric series, it’s true that
$$
\sum_{n=1}^{m} n \cdot a_n = a_1 \frac{1 - (m+1) r^m + m r^{m+1}}{(1 - r)^2}
$$
and, more commonly,
$$
\sum_{n=1}^{m} a_n = a_1 \frac{r^m - 1}{1 - r}
$$
With some algebra, these equations yield that $r = .75841$ and $a_2 = 1.48282$ million given the first two requirements. Let’s see what it looks like in the plot.
<div style="text-align: center;">
  <img src="/images/surnames/first_function.png" style="width:100%;">
</div>

So that’s definitely not it. Kind of forgot we would also like $a_{99}$ to be fairly close to 1300. Time to try harder. How about keeping the exponential part and introducing a power law function so that we have
$$a_n= b \cdot n^p \cdot e^{cn}$$
In order to find the parameters b, p, and c we will use scipy for optimization. We would like to minimize the following: 
$$ (\frac{\sum_{n=2}^{99} n \cdot a_n - 25,406,000}{25,406,000})^2 + $$
$$ (\frac{\sum_{n=2}^{99} a_n - 6,137,746}{6,137,746})^2 + $$
$$ (\frac{a_{99}-1,300}{1,300})^2 $$
which are just the requirements we listed normalized and squared. Using that, we get $b = 3.546987e6$, $p = -1.9727$, and $c = 0.01141$. Let’s see how that looks:
<div style="text-align: center;">
  <img src="/images/surnames/second_function.png" style="width:100%;">
</div>

That’s more like it. The objective function also comes out to nearly 0, meaning our requirements are met almost exactly.

Alright, let’s get back on track. How many people do we need before surnames overlap? To simulate this, a value in “number of appearances” is generated according to what percentage of the population falls in that category. For example, there are 1,279 names that have 100 people each, so that accounts for 127,900 people, or 127,900/294,979,229 = 0.04% of the population. So 0.04% of the time that category is chosen.

Once the category of 100 appearances is chosen, there are 1,279 possible names within that category, so we choose a random number between 1 and 1,279. We store this “person” as person_100_1279. If we choose another person_100_1279 over the course of picking out that sample, that means we have a duplicate. This process is done for samples of many sizes, from 5 to 125. Each sample size is tested 10,000 times, so the number of times a duplicate is found divided by 10,000 represents the probability a group of that many people will contain a duplicate surname.

Here are the results:
<div style="text-align: center;">
  <img src="/images/surnames/duplicate_rate.png" style="width:100%;">
</div>

Running more tests around where the curve appears to cross the red line, it looks to be almost exactly 50 people needed for a 50% chance that there will be a shared last name. Kind of a neat coincidence.

On a practical note, that number is for a completely random group of people selected. The groups that people tend to find themselves in, on the other hand, probably are not a random slice of the American population. You’re probably around people that are more like you than a random sampling of Americans. If that increases the similarity of last names, which I think it would, my guess is that the 50 number should be lower in practice.

The results seem much more intuitive to me than the birthday problem/paradox. In a group of 20 random people, a last name being shared about 10% of the time feels about right. Or, in a group of 100 people, just over a 90% chance of a shared last name also feels natural.

The census data also has what percentage of each name is from different racial groups. An interesting expansion of this could be to mimic smaller communities, like states or towns, by weighting the frequency names are chosen to match the demographics of the community. 