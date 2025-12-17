+++
title = "'Grand Number' (15x15, Themed)"
weight = 2
+++

You can download the grid below as a PDF <a href="/crosswords/grand_number.pdf" target="_blank">here</a>.

<!-- Show the blank crossword PNG -->
<img src="/crosswords/grand_number.png" alt="Crossword Puzzle" style="width: 100%; max-width: 600px; display: block; margin: auto;">

<!-- Hidden solution section -->
<div style="text-align: center; margin-top: 1rem;">
  <button id="show-solution-btn" style="padding: 0.5rem 1rem; cursor: pointer;">Show Solution</button>
</div>

<div id="solution-container" style="display: none; text-align: center; margin-top: 1rem;">
  <img src="/crosswords/grand_number_solution.png" alt="Crossword Solution" style="display: block; margin: auto; width: 100%; max-width: 400px;">
</div>

<script>
  const btn = document.getElementById("show-solution-btn");
  const solution = document.getElementById("solution-container");

  btn.addEventListener("click", () => {
    if (solution.style.display === "none") {
      solution.style.display = "block";
      btn.textContent = "Hide Solution";
    } else {
      solution.style.display = "none";
      btn.textContent = "CLICK HERE TO SHOW SOLUTION";
    }
  });
</script>