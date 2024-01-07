let totalDraws = 0;
let totalDiamonds = 0;
let results = [];

function draw() {
    let rand = Math.random() * 100;
    if (rand < 7.0) {
        return "星4";
    } else if (rand < 42.0) {
        return "星3";
    } else {
        return "星2";
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
    results.push("---");  // 仕切りを追加
    totalDraws += 10;
    totalDiamonds += 50;
    displayResults();
}

function displayResults() {
    let resultsHTML = "";
    for (let i = 0; i < results.length; i++) {
        if (results[i] === "---") {
            resultsHTML += "<div style='width: 100%;'></div>";  // 仕切りを検出したら全幅の空のdivを追加
        } else {
            resultsHTML += "<div style='margin: 5px;'>" + results[i] + "</div>";  // 結果をdivで囲み、マージンを追加
        }
    }
    document.getElementById("results").innerHTML = resultsHTML;
    document.getElementById("totalDraws").innerHTML = "合計回数: " + totalDraws;
    document.getElementById("totalDiamonds").innerHTML = "合計ダイヤ: " + totalDiamonds;
}

function reset() {
    totalDraws = 0;
    totalDiamonds = 0;
    results = [];
    displayResults();
}