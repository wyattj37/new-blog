+++
title = "Ballot Stuffing and Mansplaining"
date = "2025-07-16"
tags = [
    "web scraping",
    "browser automation"
]
+++
Learning a few things about the web via voter fraud and the Lex Fridman podcast. <!--more-->

# Overview
There's a pair of things I worked on recently that had to do with browser interaction / web stuff / HTML / JavaScript, which was all fairly new to me. Neither of the projects were exceedingly interesting or involved on their own, so I'll throw them together here. The first is to do with automated voting for a recent sports all star game. The second is scraping podcasts transcripts to see Lex Fridman's mansplain rate.

# Ballot Stuffing
Some websites, like Google, will immediately flag you if they detect you are using a library like selenium to automate control of the browser. Other websites, like some popular all star voting platforms, will not do that. Which means that, if you wanted to, you could write a script that opens an incognito Chromium window and navigates to the URL of the voting site. Then, inspecting the web page, you could see what identifies the buttons you need to click in order to select and submit a vote. Using that information, you could complete the script by ordering those elements to be clicked, close out the page, and start anew.

In order to do this repeatedly, it would help to have a lightweight computer laying around, like a Raspberry Pi. Depending on your internet speed, you could probably let the script run thousands of times during the duration of the voting period. Now it wouldn't be enough to completely overwhelm the tally with millions of extra votes - that would require a more sophisticated approach, I assume - but it's not nothing. In theory, you could find a moderately censored version of such a script on my GitHub.

# Mansplaining
Following the theme of parsing through HTML, the Lex Fridman podcast has uploaded the transcript of recent interviews to its website. Using the BeautifulSoup library, it's not so hard to take the entirety of the interview and get a word count for both Lex and the guest. With the word count you can see what percent of the conversation came from guest. This was on my mind because I was recently listening to an episode where the guest was a woman, and it seemed like Lex was doing more of the talking than I was used to hearing in other episodes. So, I took the transcript of the 9 most recent solo-woman guests and compared them to the 70 most recent solo-man guests. Here are the results in a box plot:

<div style="text-align: center;">
  <img src="/images/webstuff/box_plot.png" style="width:80%;">
</div>

And in a histogram:

<div style="text-align: center;">
  <img src="/images/webstuff/histogram.png" style="width:80%;">
</div>

As seen above, yes, the percentage of words spoken by the guest is in fact lower for woman guests. Using the same data to run a t-test on the sample means yields a p-value of .0154. That's quite significant, but of course the sample of guests that are women is small. Lex mostly hosts guests in STEM fields, in which women are underrepresented, so if there is a problem with the conversations worth discussing, there is a also systemic component worth discussing.

While on the subject, the conversation most equally shared between Lex and the guest is Roman Yampolskiy. The most guest dominant conversations, both over 90% guest-leaning, came from Omar Suleiman 2 and Matthew Cox. And since we're already in the weeds, the longest conversations come just shy of 40,000 words with ThePrimeagen and Pieter Levels. Pieter apparently talks pretty fast because his interview is a whole 2 hours shorter.

For what it's worth, here is the convsersation length data via box plot:

<div style="text-align: center;">
  <img src="/images/webstuff/box_plot_length.png" style="width:80%;">
</div>

The medians are within a hundred of each other, but the 20,000 - 40,000 word count range is almost entirely male.