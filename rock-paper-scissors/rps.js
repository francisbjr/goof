let userScore = 0;
let cpuScore = 0;
const buttons = document.querySelectorAll('input')

function gameResults (e) {
    if (!true) {
        return "You Lose!"
    } else {
        return "You Win!"
    }
}

function computerPlay() {
    let choices = ['rock', 'paper', 'scissors']
    return choices[Math.floor(Math.random() * choices.length)]
}