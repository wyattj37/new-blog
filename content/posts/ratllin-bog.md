+++
title = "Ratllin' Bog and Thunderstruck: Where You Should Be in the Rotation"
date = "2024-01-03"
description = "Limiting the damage at the pregame."
tags = [
    "drinking games"
]
+++
Use these charts to find the optimal spot in the Rattlin' Bog or Thunderstruck rotation to minimize the damage.  <!--more-->
# Overview
These are two similar games - in Rattlin' Bog a player's turn lasts the duration of the song's verse which gets increasingly long. In Thunderstruck, a player's turn lasts from one use of "thunder" in the song to the next. You can select the number of participants in the dropdown menu. The player that begins is Player 1, the next Player 2, and so on. The player(s) with the longest rounds are highlighted in red. I recorded the times of each round, stored them in a list and looped through to create the charts.

# Rattlin' Bog
<div>
  <select id="imageSelectorRB" onchange="showImageRB()">
    <option value="" disabled>Select an image</option>
    <option value="2Players.png">2 Players</option>
    <option value="3Players.png">3 Players</option>
    <option value="4Players.png">4 Players</option>
    <option value="5Players.png">5 Players</option>
    <option value="6Players.png">6 Players</option>
    <option value="7Players.png">7 Players</option>
    <option value="8Players.png">8 Players</option>
    <option value="9Players.png">9 Players</option>
    <option value="10Players.png">10 Players</option>
    <option value="11Players.png">11 Players</option>
    <option value="12Players.png">12 Players</option>
    <option value="13Players.png">13 Players</option>
    <option value="14Players.png">14 Players</option>
  </select>
</div>

<div>
  <img id="selectedImageRB" src="" alt="Selected Image" style="display:none; width:100%; max-width:600px;" />
</div>

<script>
function showImageRB() {
  var selectorRB = document.getElementById('imageSelectorRB');
  var selectedImageRB = document.getElementById('selectedImageRB');
  var imagePathRB = '/images/rattlin-bog/' + selectorRB.value;

  if (selectorRB.value) {
    selectedImageRB.src = imagePathRB;
    selectedImageRB.style.display = 'block';
  } else {
    selectedImageRB.style.display = 'none';
  }
}

window.addEventListener('load', function() {
  var selectorRB = document.getElementById('imageSelectorRB');
  selectorRB.value = '5Players.png'; // Set this to your default image value
  showImageRB();
});
</script>

# Thunderstruck
<div>
  <select id="imageSelectorTS" onchange="showImageTS()">
    <option value="" disabled>Select an image</option>
    <option value="2Players.png">2 Players</option>
    <option value="3Players.png">3 Players</option>
    <option value="4Players.png">4 Players</option>
    <option value="5Players.png">5 Players</option>
    <option value="6Players.png">6 Players</option>
    <option value="7Players.png">7 Players</option>
    <option value="8Players.png">8 Players</option>
    <option value="9Players.png">9 Players</option>
    <option value="10Players.png">10 Players</option>
    <option value="11Players.png">11 Players</option>
    <option value="12Players.png">12 Players</option>
    <option value="13Players.png">13 Players</option>
    <option value="14Players.png">14 Players</option>
  </select>
</div>

<div>
  <img id="selectedImageTS" src="" alt="Selected Image" style="display:none; width:100%; max-width:600px;" />
</div>

<script>
function showImageTS() {
  var selectorTS = document.getElementById('imageSelectorTS');
  var selectedImageTS = document.getElementById('selectedImageTS');
  var imagePathTS = '/images/thunderstruck/' + selectorTS.value;

  if (selectorTS.value) {
    selectedImageTS.src = imagePathTS;
    selectedImageTS.style.display = 'block';
  } else {
    selectedImageTS.style.display = 'none';
  }
}

window.addEventListener('load', function() {
  var selectorTS = document.getElementById('imageSelectorTS');
  selectorTS.value = '5Players.png'; // Set this to your default image value
  showImageTS();
});
</script>

As a note, Thunderstruck is not a very equal game. Two players usually take the brunt of the drinking time. And in the case of 4 players, avoid being the 4th. Also, there is one subtle "thunder" around the middle of the song that is easily missed, at which point the charts would be inaccurate.