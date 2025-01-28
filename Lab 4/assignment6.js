function reverseNumber() {
    var num = document.getElementById("numberInput").value;
    var reversedNum = num.split('').reverse().join('');
    document.getElementById("result").innerText = "Reversed Number: " + reversedNum;
}