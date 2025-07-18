+++
title = "The Worst Feasible Sequence AI"
date = "2025-03-24"
tags = [
    "cards",
    "card games",
    "board games"
]
featured = true
weight = 2
+++
Making the worst possible AI that can win at the game Sequence.
<!--more-->

# Introduction
When I first started to make this post, my plan was something much more involved. I was going to replicate the strategies used by the labs that made bots like Pluribus (for poker) and AlphaGo (for go) for the board game Sequence (see [here](https://en.wikipedia.org/wiki/Sequence_(game))).

In order to do that, I would need to make a fully functioning Sequence game with all the logic, make the computer play itself over and over for millions of games, record the moves and board states to create training data, use some neural network to evaluate potential moves along with a Monte Carlo Tree Search, and probably many other complicated steps and headaches along the way.

That stuff is interesting and all, but I realized it would entail months of work for a game that just isn't *that* hard. In fact, if I had 5 minutes to explain the game to a complete beginner, then showed them a hand and a random board state, they would probably make a move that is at least fine. Also, the outcome of the game has a large luck component based on the number of Jacks (wild cards) that a player is dealt.

Given the simplicity and luck factor, what I guessed is that you could probably make an "AI" that wins at least some games against humans without being robust at all - maybe just a handful of rules. And that is what I have set out to do: make the worst feasible Sequence AI.

# The Rules
The first of two rules will be dedicated to using Jacks (wild cards).

1. The program will use a two-eyed Jack (offensive wild card) if and only if it completes a sequence.

The second rule concerns the placement of all other cards:

2. The card will be used which has the largest score in its surrounding 4x4 box of squares.

I will go into further detail what I mean by "score" in the next section, but I assure you it is not complicated.

# The Implementation (All Offense)
I will be using a 2D array the same size as the board to represent the Sequence board. The values of the squares (places in the 2D array) can have the following values:

- 1 = own chip already placed there / free space

- -1 = opponent chip already placed there

- 0 = empty

- .33 = potential to be filled based on card in possession

The aforementioned "score" will be calculated as the sum of the squares in the surrounding 4x4 box WITHOUT taking into account the opponent's chips. For now, I am foregoing any sort of defensive measure, including One-Eyed jacks that can remove opposing chips.

There was some work involved in finding one-away sequences and full sequences, and some slight headaches converting cards to board positions, especially since every card appears twice. Besides those items and calculating the score for each card, there isn't much else.

One last note: once the bot plays a sequence, it turns all of those spaces into a -1 value. Otherwise I'm guessing it would just keep playing around the chips that are no longer relevant.

# First Run Through
I was intentionally foregoing the ability of the bot to play a One-Eyed (removing) Jack, but I forgot the opponent is free to do so. Had to include some logic for allowing the opponent to remove a chip.

# Second Run Through
Couple more bugs. Mostly to do with duplicate cards. First, whenever a card is played which there are multiple of in the hand, both cards are deleted. For instance if there are two 3 of Clubs and one is played, both are deleted. That should be an easy enough to fix. Another is that when a card is picked up that it already played, it will try and play in the same spot again. Once again, simple oversight.

A bigger issue came to my attention when the bot wouldn't play the game-winning Two-Eyed Jack because it overlapped with a previous sequence. Now the fact it got a sequence at all is a massive win. But this situation happens fairly often and it will take some work to address. Each new sequence can contain exactly one chip from a previous sequence. So I will change the "old sequence" chips to be a value of -2 and then adjust the logic to account for that.

# Third Run Through
Forgot to consider that the start of the game could begin with either player. Also playing without One-Eyed Jacks is a pretty severe advantage but I think a game could be won as-is. Just gotta keep trying.

# Fourth Run Through - Winner
That's a W folks. It wasn't a clean win, but as I suspected with the Two-Eyed Jack advantage it got the job done. Even with a bug I forgot to fix that kept the winning move from being played for 3 or 4 turns. Once I fix that I'll upload to my GitHub with instructions how to use it - it's a little janky but the computer really does do all the decision making.

# Example Outputs
Below is a picture of a typical turn of the game.
<div style="text-align: center;">
  <img src="/images/sequence/sequence_output.png" style="width:80%;">
</div>

"Play Ks1" indicates the user plays the King of Spades on the top half of the board. 10d1 is entered to indicate the 10 of Diamonds was drawn afterwards. "2h2" is entered to indicate the opponent played the 2 of Hearts in the bottom half of the board in response.

In the board, you'll notice all the 1's indicate chips that are previously played, -1's are opponent chips, 0's are empty, and .33's are empty but the user has a card that could be played there.

Here is another example of a turn, except this time the opponent played a one-eyed jack:
<div style="text-align: center;">
  <img src="/images/sequence/sequence_output_jack.png" style="width:80%;">
</div>

Whenever the "Where?" input is entered, the square that used to contain a user chip will return back to a 0 or .33, depending if that card is held by the user.