var snd = new Audio("static/data/awesome.mp3");

$(document).ready(function() {
    console.log("Page Loaded");
    snd.play();
    loaddropdown();
    $("#filter").click(function() {
        makePredictions();
    });
});

function loaddropdown() {
    d3.csv("static/data/full_avg_2021.csv").then(function(data) {
        console.log(data);

        var teams = data.map(x => x.TeamName_Clean);
        teams.sort();
        teams.forEach(function(x) {
            $("#team1").append(`<option value="${x}">${x.toUpperCase()}</option>`);
            $("#team2").append(`<option value="${x}">${x.toUpperCase()}</option>`);

        })
    })
}

function makePredictions() {
    var year1 = $("#year1").val();
    var year2 = $("#year2").val();
    var e = document.getElementById("team1");
    var e2 = document.getElementById("team2");
    var team1 = e.options[e.selectedIndex].value;
    var team2 = e2.options[e2.selectedIndex].value;
    // create the payload
    var payload = {
            "year1": year1,
            "year2": year2,
            "team1": team1,
            "team2": team2
        }
        // Perform a POST request to the query URL

    $.ajax({
        type: "POST",
        url: "/makePredictions",
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({ "data": payload }),
        success: function(returnedData) {
            // print it
            console.log(returnedData);
            $("#output").text(returnedData["prediction"][0]["points"]);
            $("#output1").text(returnedData["prediction"][1]["points"]);
            $("#output2").text(returnedData["prediction"][0]["team"]);
            $("#output3").text(returnedData["prediction"][1]["team"]);

        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("Status: " + textStatus);
            alert("Error: " + errorThrown);
        }
    });
}