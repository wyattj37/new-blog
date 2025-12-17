+++
title = "'Judicial Mandate' (15x15, Themed)"
weight = 3
+++

You can download the grid below as a PDF <a href="/crosswords/judicial_mandate.pdf" target="_blank">here</a>. This is the first full crossword I ever created, so it may be a bit weak but it has a sentimental place for me.

<!-- Show the blank crossword PNG -->
<img src="/crosswords/judicial_mandate.png" alt="Crossword Puzzle" style="width: 100%; max-width: 600px; display: block; margin: auto;">

<!-- Hidden solution section -->
<div style="text-align: center; margin-top: 1rem;">
  <button id="show-solution-btn" style="padding: 0.5rem 1rem; cursor: pointer;">Show Solution</button>
</div>

<div id="solution-container" style="display: none; text-align: center; margin-top: 1rem;">
  <img src="/crosswords/judicial_mandate_solution.png" alt="Crossword Solution" style="display: block; margin: auto; width: 100%; max-width: 400px;">
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