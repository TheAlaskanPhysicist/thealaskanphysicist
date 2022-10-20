const data = {
    "name": "Stanley F. Goodwin",
    "highest-degree": "B.S."
}



document.addEventListener("DOMContentLoaded", function() {
    load_header(data);
});

function load_header(data) {
    var text = data["name"] + ", " + data["highest-degree"]
    document.getElementById("h1-section-name").innerHTML = String(text);
    console.log("H1 Section Name: Initialized!")
}