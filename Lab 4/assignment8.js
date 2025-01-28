function checkEligibility() {
    var age = document.getElementById("ageInput").value;
    var result = document.getElementById("result");
    if (age >= 18) {
        result.textContent = "You are eligible for voting.";
    } else {
        result.textContent = "You are not eligible for voting.";
    }
}