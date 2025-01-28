function sumOfDigits() {
    let input = document.getElementById("numberInput").value;
    let sum = 0;
    for (let char of input) {
        sum += parseInt(char);
    }
    document.getElementById("result").innerText = "Sum of digits: " + sum;
}
