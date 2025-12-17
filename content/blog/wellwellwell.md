+++
title = "Well, We'll, We(?)ll"
date = "2024-09-10"
tags = [
    "nlp",
    "machine learning"
]
draft = true
hiddenInHomeList = true
+++
Using NLP and ML techniques to determine whether sentences containing 'well' should be autocorrected to 'we'll'. <!--more-->

# Background
When I'm typing on my phone, I pretty much never use apostrophes - I leave the insertion of those entirely up to autocorrect. While autocorrect does this accurately for the most part, I noticed it struggles on correcting "well" to "we'll", especially at the beginning of a sentence. Of course at the beginning of the sentence there is no context, but one would think several words down the line the correction could be more accurate. I wanted to investigate how much better a language model could perform than standard autocorrect, and how each added word of context improves that performance.

# Collecting the Data
I'm not sure if you've heard, but language processing is something of a hot topic these days. Lucky for me, that means there's lots of data out there to use. I opted for a collection of [blogs](https://www.kaggle.com/datasets/rtatman/blog-authorship-corpus) for two reasons. First, blogs are more likely to be written in the first person, which might include some first person plural like "we'll". Second, they are more likely to be grammatically correct then something like a dataset of text messages.

I used the spacy library which provides lots of useful tools for separating sentences and finding which ones contain or start with certain words. As is typical for dealing with lots of data, the process is time-intensive. Patience is a virtue. When it's all said and done I'm working with 19113 sentences starting with "well" and 896 sentences starting with "we'll".

# The Prediction Task
Once all of the sentences are collected, I indicate which ones contain "we'll" and then remove the apostrophe. I then decide how many words after the "well" to include (starting with 1) and then remove the rest. As it's much more common for a sentence to start with "well" than "we'll", with 0 added context guessing no apostrophe would be the best move.

I haven't 