let totalDraws = 0;
let totalDiamonds = 0;
let results = [];

function draw() {
    let rand = Math.random() * 100;
    if (rand < 7.0) {
        return "Star 4";
    } else if (rand < 42.0) {
        return "Star 3";
    } else {
        return "Star 2";
    }
}

function drawOne() {
    let result = draw();
    results.push(result);
    totalDraws++;
    totalDiamonds += 5;
    displayResults();
}

function drawTen() {
    for (let i = 0; i < 10; i++) {
        let result = draw();
        results.push(result);
    }
    totalDraws += 10;
    totalDiamonds += 50;
    displayResults();
}

function displayResults() {
    document.getElementById("results").innerHTML = "Results: " + results.join(", ");
    document.getElementById("totalDraws").innerHTML = "Total Draws: " + totalDraws;
    document.getElementById("totalDiamonds").innerHTML = "Total Diamonds: " + totalDiamonds;
}

function reset() {
    totalDraws = 0;
    totalDiamonds = 0;
    results = [];
    displayResults();
}