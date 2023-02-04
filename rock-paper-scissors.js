console.log(getComputerChoice());

function getComputerChoice () {
    //create an array with 'rock + paper + scissors'
    let choice = ['rock', 'paper', 'scissors'];
    //create a variable that will pick a random string out of the array
    let random = Math.floor(Math.random() * choice.length);
    //return the variable
    return choice[random];
}

//create variable for getPlayerChoice input prompt
let getPlayerChoice = prompt('Rock, Paper, or Scissor?');

console.log(rpsGame(getPlayerChoice,getComputerChoice()));

//declare function for game (two parameters)
function rpsGame (playerSelection, computerSelection) {
    //call getPlayerChoice var.
    getPlayerChoice;
    //IF getPlayerChoice equality check w/ getComputerChoice is true
    if (playerSelection == 'rock' && computerSelection == 'rock'
    ,   playerSelection == 'paper' && computerSelection == 'paper'
    ,   playerSelection == 'scissors' && computerSelection == 'scissors'
    ) {
        return 'Draw';
    //ELSE IF getPlayerChoice wins (rock > scissors) + (scissors > paper) + (paper > rock)
    } else if (
        playerSelection == 'rock' && computerSelection == 'scissors',
        playerSelection == 'scissors' && computerSelection == 'paper',
        playerSelection == 'paper' && computerSelection == 'rock'
    ) {
        return 'WINNER!!!';
    //ELSE IF getPlayerChoice loses (rock < paper) + (paper < scissors) + (scissors < rock)     
    } else if (
        getPlayerChoice == 'rock' && getComputerChoice == 'paper',
        getPlayerChoice == 'paper' && getComputerChoice == 'scissors',
        getPlayerChoice == 'scissors' && getComputerChoice == 'rock'            
    ) {
        return 'Loser';     
    } else {
        return 'Try again';
    }  
}

