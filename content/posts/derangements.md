+++
title = "Deranged Probability Puzzle"
date = "2024-10-03"
tags = [
    "combinatorics",
    "math"
]
math = true
+++

Attempting a "deadly" probability problem with combinatorics. <!--more-->

# The Problem
I stumbled across the website Brain Stellar, a collection of sorts of strategy and probability puzzles. I saw that one problem, [here](https://brainstellar.com/puzzles/1008), was one of four marked as "deadly" and no solution was given, only an attempt by the author. Naturally I had to give it a go myself.

# My Approach
The aim of the problem is to find the probability that starting with N shooters, we end up with 1 survivor. We will call this probability P(N). This probability is the sum of P over all possible states we can move to from N, multiplied by the probability that we will move to that state. We will call that probability, of moving from state N to state N - k, p(N - k). For example, in the case N = 4, there will be at most 4 people shot, k = 4, and at least 2 people shot (no self-shots allowed), k = 2. So:

$$
P(4) = P(3)p(4 - 1) + P(2)p(4 - 2) + P(1)p(4 - 3) + P(0)p(4 - 4)
$$

Note that the base cases are:

One survivor:
$$
P(1) = 1
$$

No survivors:
$$
P(0) = 0
$$ 

And in the case of 2 shooters, they must both shoot each other.
$$
P(2) = 0
$$ 

Therefore, in order to calculate P(N), we must first calculate P(3), P(4), ..., P(N-1).

Because P(N) will be found iteratively, the trouble comes in calculating p(N - k). In order to find p(N - k), we need to find all possible ways that the N people can shoot k, and then divide by the total arrangement of shootings. The total arrangement is simple enough; there are N shooters and N - 1 possible targets for each, or $$N^{(N-1)}$$ But how many ways can N people shoot k of themselves? There's the rub.

# Derangements and Stirling Numbers
We can think about the problem as having N distinct objects and sorting them into k distinct non-empty sets. Luckily, there are [Stirling numbers of the second kind](https://en.wikipedia.org/wiki/Stirling_numbers_of_the_second_kind), which describe how many ways to sort N distinct objects into k non-empty sets. All that we need to do to adjust this to make the k sets distinct is to assign each of them a label. That's easy enough: we are choosing k assignments for k sets, and we can multiply our S(N,k) (denoting the Stirling numbers of the second kind) by k!. However, there is still one more pesky condition: no self-shots are allowed. 

In this way, the problem resembles finding [derangements](https://en.wikipedia.org/wiki/Derangement), or "permutations of the elements of a set in which no element appears in its original position." But this only gives us the number of ways to sort n elements into n sets with one element each, and we have more elements than sets which of course can contain multiple elements. So the answer to counting our possible arrangements lies somewhere in the middle of these two methods.

# Attempting a Solution
In order to find all the arrangements that work, it would make sense to find all possible arrangements, which I mentioned was $$ k! S(N, k) $$ and then subtract the arrangements that do not work. The arrangements that do not work are the ones in which a set contains the same labeled element (self-shot). Let's walk through an example and see how we might approach this. Here is what it looks like for N = 5, k = 3.

|  Choice 1 |  Choice 2 |  Choice 3 |  Options  |
|-----------|-----------|-----------|-----------|
|           |           |           |     1     |
|           |           |           |     2     |
|           |           |           |     3     |
|           |           |           |     4     |
|           |           |           |     5     |

Let's consider the case of 1 self-shot: we will place 1 into Choice 1 to represent this.

|  Choice 1 |  Choice 2 |  Choice 3 |  Options  |
|-----------|-----------|-----------|-----------|
|    1      |           |           |           |
|           |           |           |     2     |
|           |           |           |     3     |
|           |           |           |     4     |
|           |           |           |     5     |

How many ways can we now fill up the rest of the choice columns so that they each have at least one entry? It seems like we are back to Stirling numbers of the second kind: we need to fill the other k = 2 bins with the remaining N = 4 options. That would, however, only leave us with the cases where exactly option 1 is in the choice 1 column. Additionally, we are faced with the same problem once again in that S(4,2) will give us options in which 2 is in the choice 2 column, or 3 is in the choice 3 column, and we are only considering the case of 1 violation. 

Things get messy from there. Let's try again.

# Re-attempting a Solution
This time, let's turn to derangements and try to count all ways that we can create a valid arrangement. After some analysis, the arrangements can be broken up into how many choices are only filled with "free" options, that is, options that do not have a corresponding choice column. The case where there are no choices filled with only free options might look something like this:

|  Choice 1 |  Choice 2 |  Choice 3 |  Options  |
|-----------|-----------|-----------|-----------|
|           |           |      1    |           |
|     2     |           |           |           |
|           |      3    |           |           |
|           |           |           |     4     |
|           |           |           |     5     |

And then we can place options 4 and 5 however we please. How can we make the arrangement of 1, 2, and 3? The derangements of 3 items, or \(D(3)\). So the number of valid solutions from here comes to 

$$
D(3) \cdot 3^2
$$

Written more generally:

$$
D(k) \cdot k^{N-k}
$$

Alright, how about whenever 1 choice is filled with only "free" options? Consider if we give choice 3 this condition. First, we must choose at least one free option to fill its column, of which there are (N-k) options. Let's choose option 5. Options 1 and 2 are now constrained to only the remaining choices, which in this case are also 1 and 2. We are actually just making another derangement out of the remaining non-free options, of which there are \(D(k - 1)\) possibilities. In this case, there is only one of these. Now our table looks like this:

|  Choice 1 |  Choice 2 |  Choice 3 |  Options  |
|-----------|-----------|-----------|-----------|
|           |      1    |           |           |
|     2     |           |           |           |
|           |           |           |     3     |
|           |           |           |     4     |
|           |           |     5     |           |

We are left with option 3, which can go to any of the (k - 1) = 2, remaining choices, and 4, which can go to any of the k = 3 remaining choices. All in all, the total options are:

$$
(N-k) \cdot D(k-1) \cdot (k-1) \cdot k
$$

For the case where we are limiting i choices to be only filled with free options, this expression comes to:

$$
(k - i)^i \cdot \text{Perm}(N-k, i) \cdot k^{(N - k - i)} \cdot \left( D(k - i) + D(k - 2i) \cdot (k-2)^i + D(k - 3i) \cdot (k-3)^i + \ldots \right)
$$

We also need to consider that originally we chose a group of k out of N to be the ones shot, which brings us to: 

$$
\binom{N}{k} \cdot (k - i)^i \cdot \text{Perm}(N-k, i) \cdot k^{(N - k - i)} \cdot \left( D(k - i) + D(k - 2i) \cdot (k-2)^i + D(k - 3i) \cdot (k-3)^i + \ldots \right)
$$

# The Problem with the Problem
This formula seems to work for calculating the P(N) for k = 2,3,4,5,6. However, after that, it begins to break down. I've come to realize that it's because there are duplicate cases when it comes to choosing spots for the free options and non-free options excluded from derangements. To be continued...