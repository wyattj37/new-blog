+++
title = "How Badly Can You Win a Tennis Match?"
date = "2025-05-28"
math = true
toc = false
tags = [
    "sports"
]
+++
Winning ugly.
<!--more-->

## Linearity of Scoring in Sports
People who enjoy tennis are likely to know that you don't have to win more points than your opponent to win a given match. Tennis is scored non-linearly, meaning the points you win don't have a direct, linear relationship with the outcome of the match. In basketball, a linearly-scored game, if you have more points than your oponnent at the end of regulation, then you win. In tennis, on the other hand, individual points will only win you games, which win you sets, which *actually* win you matches.

Other sports, like volleyball, also have this sort of nesting effect which creates non-linear scoring. If you are a golfer, in match play there is a similar effect when holes are counted towards a win, not individual strokes. Tennis is a particularly interesting case because there are two levels of separation from the individual point and the outcome: games and sets. This is different from volleyball which only has one level (sets) and golf match play which only has one, as well (holes). What this means for tennis is that a player has the oppotunity to lose lots of points and still win.

## How to Maximize Losing and Win
The fraction we are looking to minimize is $\frac{\text{points won}}{\text{points played}} = \frac{\text{points won}}{\text{points won + points lost}}$. No surprise, we want many points lost and hardly any points won. Let's assume we are looking at a best-of-5-sets match. To win, you need to win at least 3 sets. That also means you can lose up to 2 sets.

### Losing Two Sets
The worst way you could lose those two sets is 0-6, 0-6, and within those 6 games losing every single point (4 points). That brings our total points lost over two sets to: 

$$(\text{2 sets}) \cdot (\text{6 games/set}) \cdot (\text{4 points/game}) = \text{48 points}$$

Our win rate is at a solid $\frac{0}{48}$ after those two sets.

### Winning Three Sets
Now that the lost sets are out of the way, we need to figure out how to win the other three sets. We want to win these sets while allowing our opponent to get lots of points. The two closest ways you can win a set is at 7-5 or at a 6-6 tiebreak. For now we'll focus on the 7-5 option and come back to the tiebreak later. So what's optimal way to get to 7-5? The 5 games lost are easy - just like before we will lose them to love (without winning a point), which gives us 4 points lost each game, or 20 points lost per set.

The 7 games won are a little tricker because of the deuce rules. If a player wins at 40-30, they will have won 4 points and their opponent will have won 2. If instead it goes to deuce (40-40), and the next two points are won for the game, the (points for) to (points against) is 5 to 3. In the event of another deuce, the game could then be won at 6 to 4. The next possibility is 7 to 5, then 8 to 6, and so on. Essentially, all the ways you can win a tennis game as (points for) to (points against) are 4 to 0, 4 to 1, and N to (N-2) for any N $\geq$ 4.

As N can take on any value greater than or equal to 4, it's not immediately clear what this means for our $\frac{\text{points won}}{\text{points won + points lost}}$. We can increase points lost as much as we want, but it requires increasing points won just as much. Clearly winning 4 to 2 is better than 4 to 1 or 4 to 0, but is it better than 5 to 3? 6 to 4? To figure this out, we want to express our win rate as a function of N and minimize it.

Let's start by tallying up the points won. In each of the 3 sets we will win 7 games, so 21 games total. In each of those 21 games we will win N points. That brings us to 

$$ \text{points won} = \text{21N}$$

For points lost, during those same 21 games we will lose (N-2) points per game. 

$$ \text{points lost} =  21\text{(N-2)} $$

But keep in mind, we are winning the 3 sets 7-5. As mentioned before, during those 5 games we are losing 4 points and winning none. That brings us to a total of 60 points lost over the 3 sets.

$$ \text{points lost} =  21\text{(N-2)} + \text{60}$$

Finally there are the 48 points we started off with in the sets lost 0-6, 0-6. All in all, we have

$$ \text{points lost} =  21\text{(N-2)} + \text{60} + \text{48} = \text{21N + 66}$$

The win rate function, let's call it *f*, is therefore represented as 

$$ f(N) = \frac{\text{21N}}{\text{21N + 21N + 66}} = \frac{\text{21N}}{\text{42N + 66}} $$

Remember that the whole idea of writing this in terms of N is we want to know what the best way to win the deuce games is. N is a representation of essentially how many times the deuce point will be played.

## Cut to the Chase
As it turns out, the best value of N is 4. You want to win the games at 40 to 30, or 4 points to 2 points. There is no advantage to playing extended deuce games, because the points you are winning have more of an effect on the win rate than the points you are losing alongside them. I'm go into this at length in the next section. For now, the final result is:

$$ \text{Minimum Win Rate} = \frac{84}{234} = \frac{14}{39} = .359 $$

So by winning only 84 of 234 total points, or a win rate just shy of 36%, you can still win a tennis match. While we're at it, if we are talking about best-of-3 sets, we arrive at

$$ \text{Minimum Win Rate} = \frac{56}{148} = \frac{14}{37} = .378 $$

As a final note, in the 6-6 tiebreaker scenario, the same logic applies that you want to win as few points as possible. The lowest 5-set win percentage you can achieve with tiebreakers is 38.3%, and the lowest in 3-set with tiebreakers is 40.3%. Those are both assuming 7-5 tiebreaker scores (which are played first-to-7) and would increase as the tiebreak scores got higher.

## Ad Nauseam
There's a few last interesting things to say about the function we're looking at. The first I'll mention is the intuition for why a low N is the minimum. Also, while the exact function we looked at was  $$ f(N) = \frac{\text{21N}}{\text{42N + 66}} $$

I'll be referencing the form of

$$ f(x) = \frac{ax + b}{2ax + c} $$

for analysis, where *a*, *b*, and *c* are all positive. It'll be helpful to realize some more general results.

The first thing we can see is that the limit of $f(x)$ will tend towards $\frac{1}{2}$ as x gets large, no matter what the constants are. Taking a derivative and doing some algebra, we find that

$$ f'(x) = \frac{a(c-2b)}{(2ax+c)^2} $$

What we see from this is that $f'(x)$ is always positive or negative across all x greater than 0. The relationship is

$$ \text{if  } c > 2b \rightarrow f'(x) > 0$$ $$ \text{if } c < 2b \rightarrow f'(x) < 0$$

The intuition for this is that, as we said, $f(x)$ will tend towards $\frac{1}{2}$ no matter what. If *c* > 2*b*, what that means is that values of $f(x)$ are starting *below* $\frac{1}{2}$, so the function will always have to be increasing to try and reach the asymptote of $\frac{1}{2}$. On the other hand, if the $f(x)$ starts above $\frac{1}{2}$ (c < 2b), then the function will have to be decreasing for all x > 0. 

What this means for our problem is that since we are in the case of $f'(x) > 0$, the minimum will always be at the lowest value of x we can choose. Or, in our case, x = 4.

### Comparing to Tiebreaks
As for why the tiebreaks did not work out, the same sort of intuition follows. Although it's not the exact same as the reasoning above, if we want to increase *b* by any amount, *c* should be increased by an amount double that, or else all we've done is make the fraction larger. But tiebreaks and deuce games follow the same increases of N points won to N-2 points lost, which is not near a ratio of 2:1 and gets worse as N increases. In a tiebreak, the minimum N is 7, so all you're doing is increasing the win rate at that point.