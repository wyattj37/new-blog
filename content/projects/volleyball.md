+++
title = "Volleyball Data Analytics App"
date = "2024-08-20"
tags = [
    "sports",
    "data analytics"
]
featured = true
weight = 5
hiddenInHomeList = true
+++

### Check Out the App
You can find the link to the app [here](https://wyattjohn.shinyapps.io/fake_vb/). It serves track data for a college volleyball team.

The keen eye might notice there are only four players, two of which have been dead for centuries and none of which play college volleyball. I scrambled some real games played and created the two of us as players to demonstrate how the app works. Just imagine that the pages include lots of real players from lots of real college teams. I stripped the actual data used on the app because the team I worked with will be using it hopefully to their competitive advantage.

### On Volleyball Analytics in General
First and foremost, if you are interested in programming and volleyball analytics, check out [datavolley](https://github.com/openvolley/datavolley) on Github. The match data I used was processed as a datavolley file (.dvw), which can be loaded in using the library as list of each moment in the game and about 80 of its describing characteristics. For example, the line that describes the serve which starts the game would include things like the home team, the visiting team, the location of the serve, the quality of the serve, the name of ther server, the score "0-0", and so on.

Given all the categories there are lots of ways to group things when creating a visualization. Commonly statistics are used to describe the location and quality of a hit and then grouped either by player, team, date, or some combination of those. You can imagine the relevance of these sorts of visualizations: How often does a team attack from this spot? Where does a player serve to most? How is a player performing over time? Those are the sorts of things you see on the app.

### On Making the App
Because datavolley is available as a package for R on Github, the app was made using Shiny. I wasn't all that familiar with R or the Shiny package (or any other R package for that matter) prior to starting work on this project, so those both took some time to get comfortable with. The biggest challenge, even more so than figuring out R and the libraries, wound up being trying to handle all the data. Every shot of every point of every game played by every team in the conference was loaded in and used. Which is quite a lot of data.

For all those points being loaded in and used, the "loaded in" part was the culprit of most issues. Loading the .dvw files took time, and, more importantly, more memory than my free Shiny account would allow. I wound up making a second R script that would load in the files locally, try and shave them down as much as possible (getting rid of useless fields or matches), and then save them into the app's directory. When the app loaded it would then just store what was saved in the directory as a variable to be used in all the other features. When it's just four players though the jumping through hoops is limited, which was another reason for making the fake app.