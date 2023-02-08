
function getComputerChoice () {
    //create an array with 'rock + paper + scissors'
    let choice = ['rock', 'paper', 'scissors'];
    //create a variable that will pick a random string out of the array
    let random = Math.floor(Math.random() * choice.length);
    //return the variable
    return choice[random];
}

let gCC = getComputerChoice();
console.log(gCC);

//create variable for getPlayerChoice input prompt
let getPlayerChoice = prompt('Rock, Paper, or Scissor?');

console.log(rpsGame(getPlayerChoice,gCC));

//declare function for game (two parameters)
function rpsGame (playerSelection,computerSelection) {
    console.log('rpsGame',computerSelection);
    let result;

    switch (playerSelection) {
        case 'rock':
            if (computerSelection === 'rock')
            {
                result = 'Draw';
            } else if (computerSelection === 'paper')
            {
                result = 'wins';
            } else if (computerSelection === 'scissors')
            {
                result = 'win';
            } else {
                result = 'try again';
            }
            break;

        case 'paper':
            if (computerSelection === 'paper')
            {
                result = 'Draw';
            } else if (computerSelection === 'scissors')
            {
                result = 'lose';
            } else if (computerSelection === 'rock')
            {
                result = ' win';
            } else {
                result = 'try again';
            }
            break;

        case 'scissors':
            if (computerSelection === 'scissors')
            {
                result = 'Draw';
            } else if (computerSelection === 'rock')
            {
                result = 'lose';
            } else if (computerSelection === 'paper')
            {
                result = ' win';
            } else {
                result = 'try again';
            }
            break;
    } 
    return result;
}

