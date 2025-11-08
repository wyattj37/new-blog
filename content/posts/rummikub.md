+++
title = "Perfecting Rummikub"
date = "2025-08-02"
tags = [
    "cards",
    "card games",
    "board games"
]
math = true
featured = true
weight = 1
+++
Making the best possible Rummikub player with integer programming.
<!--more-->

# Addressing the Problem
[Rummikub](https://en.wikipedia.org/wiki/Rummikub) is an awfully fun game, and, coincidentally, awfully well-suited to be posed as an integer programming problem. Specifically, it is a set partioning problem[^1] with a few adjustments. All the available tiles form one large set, and the rules for forming partitions are the rules which define runs and groups. The objective to be maximized in forming these partitions is the number of tiles used from the player's rack. The next section will go into describing this much more explicitly.

# Definitions
First, let's denote $S$ as the set of all valid groups in Rummikub. So if $$ S = (s_1, s_2, s_3, \ldots )$$ the contents would look something like $$s_1 = (\text{Red 1, Red 2, Red 3})$$ $$s_2 = (\text{Yellow 5, Black 5, Red 5})$$ $$s_3 = (\text{Yellow 10, wild, Yellow 11, Yellow 12})$$ and so on for all possible valid sets.

As a note, we only need to account for runs up to length 5, because any run of length 6 or more can just be split into smaller runs that are already included in $S$. As a second note, without wild tiles the number of distinct valid groups is 65, and the number of distinct valid runs is 120. When wilds are included, however, it brings the size of $S$ to 1646 members. This sounds about right, considering you are increasing the size by $_n P _2$ for each subset of size $n$.

Now that we've defined $S$ (and gotten slightly distracted), let's define $x_s$, the decision variable. $x_s$ can take on values 0, 1, or 2, and tells us how many times the corresponding set, $s$ is used in the partitioning. (Because there are two of each tile, it is possible to have 2 of a set, but no more.)

Next, we will define $T$ as the set of all tiles. It has the 104 color/number tiles and the 2 wild tiles.

Lastly, we need some look-up values. Namely, we need to know how many times a tile $t$ (belonging to $T$) is in our rack, on the board, or used in a set. The first will be denoted as $r_t$, the second as $b_t$, and the last as $u_{s,t}$. Once again, each of these can take on a value of 0, 1, or 2. Of course the only case a value in $u$ can be 2 is when there are 2 wilds in a set, as no other tile could be used twice in a set.

As an example, if there are two Yellow 11s on the board: $$b_{\text{Yellow 11}} = 2$$ We would call the $u$ (uses) table like so: $$u_{\text{(Red 11, Red 12, Red 13), Red 13}} = 1$$

# Formulating the IP Problem
Now that everything is defined, let's describe the constraints and objective and then write them mathily. The first constraint is that a every tile must be included in the partitioning at least as many times as it is on the board. I.e. you cannot take tiles off the board. We can write this using the definitions above as:

$$ \forall t \in T:\quad \sum_{s \in S} x_s \cdot u_{t,s} \geq b_t $$

The second constraint is that every tile can only be included in the partitioning as many times as it is on the board plus in your rack. We can write this, very similarly, as:

$$ \forall t \in T:\quad \sum_{s \in S} x_s \cdot u_{t,s} \leq b_t + r_t$$

And those are the only two constraints we actually need. As for the objective, we are trying to maximize the total number of tiles on the board. The only way we can increase that is by using tiles from our rack, so this is the same as maximizing tiles played from the rack. We can write this as:

$$ \max Z = \sum_{s \in S} \sum_{t \in T} x_s \cdot u_{t,s} $$

# Implementation and Solving
Now that the problem is defined, we only need use the PuLP library and encode the variables, constraints, and objective above. The rest of the hassle is just taking care of things like tracking where tiles are once they've been drawn and played, what tiles the other players are using, and the initial case of the meld.

The intial meld phase is really a sub-problem of the one detailed above. The tiles currently on the board are ignored and the only constraint is the tiles must be in your rack. If the move you can make sums to 30 points or more, then you play your meld and the game logic moves on. 

All this can be seen and used on my GitHub linked below.

# Other Things to Consider
At no point in this have we discussed points, which are the way that you win the game, not just an individual round. The only case I can think of that points would need to be addressed - in this version of the game - is as some tiebreaker between two tiles which can only be played with mutual exclusivity. You can technically configure situations where this happens. Consider a board that has a set of three 7s and three runs of 4-5-6. If you had a 7 and an 8 in your rack, you could break up the 7s on the board and play the 8, or you could leave the 7s on the board intact and play your own 7. But that situation doesn't often happen. In general, adding tiles to the board is going to increase the fluidity of things, and make it *more* likely, if anything, that your other tiles can be played. 

I also hinted at some other considerations by qualifying "in this version of the game". On the Wikipedia page you can see some rule variations that spice things up a bit. The Draw Two / River variation is particularly attractive to me because you start to incorporate some elements of imperfect information. In the original rules, you don't have any choices besides what tiles you play from your rack, and that is a choice which there is an objectively correct answer to. And the solver will find it every time. With drawing two and the river, however, you now have to make some decisions that impact future turns, where you don't necessarily know what the board will look like. Not to mention, you are making a guess as to how good the tiles you draw will be compared to the impact of drawing from the river, which is something you can calculate.

I might dive more into that river variation in the future. The first approach that comes to mind is simulating over all possible two-draws, choosing the best tile and averaging the outcome, then comparing that to each of the outcomes from drawing from the river. The latter choice would also need to be discounted in order to account for the fact you might not be able to play all non-key tiles on your next turn, if the board shifts. 

[^1]: "A set partitioning problem determines how the items in one set (S) can be partitioned into smaller subsets. All items in S must be contained in one and only one partition."
