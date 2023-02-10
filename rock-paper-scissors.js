//randomized computer choice
function getComputerChoice () {
    //create an array with 'rock + paper + scissors'
    let choice = ['rock', 'paper', 'scissors'];
    //create a variable that will pick a random string out of the array
    let random = Math.floor(Math.random() * choice.length);
    //return the random result
    return choice[random];
}
//stored value of getComputerChoice func.
let computerChoice = getComputerChoice();
//both players start at zero
let userScore = 0;
let computerScore = 0;
//create variable for getPlayerChoice input prompt
let playerChoice = prompt('Rock, Paper, or Scissor?').toLowerCase();

//declare playRound function (two parameters)
function playRound (playerSelection,computerSelection) {
    //console.log('rpsGame',computerSelection);
    let result;
    let winner = 'You Win!';
    let loser = 'You Lose!';
    let paperWins = 'Paper beats Rock!';
    let rockWins = 'Rock beats Scissors!';
    let scissorsWins = 'Scissors beats Paper!';
    //conditions for playerSelection
    switch (playerSelection) {
        case 'rock':
            if (computerSelection === 'rock')
            {
                result = 'Draw. Try Again.';
            } else if (computerSelection === 'paper')
            {
                result = `${loser} ${paperWins}`;
            } else if (computerSelection === 'scissors')
            {
                result = `${winner} ${rockWins}`;
            } else {
                result = 'not an option... Choose rock, paper or scissors.';
            }
            break;
        case 'paper':
            if (computerSelection === 'paper')
            {
                result = 'Draw. Try Again.';
            } else if (computerSelection === 'scissors')
            {
                result = `${loser} ${scissorsWins}`;
            } else if (computerSelection === 'rock')
            {
                result = `${winner} ${paperWins}`;
            } else {
                result = 'not an option... Choose rock, paper or scissors.';
            }
            break;
        case 'scissors':
            if (computerSelection === 'scissors')
            {
                result = 'Draw. Try Again.';
            } else if (computerSelection === 'rock')
            {
                result = `${loser} ${rockWins}`;
            } else if (computerSelection === 'paper')
            {
                result = `${winner} ${scissorsWins}`;
            } else {
                result = 'not an option... Choose rock, paper or scissors.';
            }
            break;
    } 
    return result;
}
//'GAME OVER' function
function endGame() {
    if (userScore > computerScore) {
        console.log("Game Over! You Win! :)");
    } else if (computerScore > userScore) {
        console.log("Game Over! You Lost! :(");
    }
}
//declare game function
function game () {
    //call playRound func.
    console.log(playRound(playerChoice, computerChoice));
    playRound(playerChoice, computerChoice);

} 