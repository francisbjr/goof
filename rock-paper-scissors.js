//randomized computer choice
function getComputerChoice () {
    //create an array with 'rock + paper + scissors'
    let choice = ['rock', 'paper', 'scissors'];
    //create a variable that will pick a random string out of the array
    let random = Math.floor(Math.random() * choice.length);
    //return the random result
    return choice[random];
}
//strings
let question = 'Rock, Paper, or Scissor?';
let winner = 'You Win!';
let loser = 'You Lose!';
let paperWins = 'Paper beats Rock!';
let rockWins = 'Rock beats Scissors!';
let scissorsWins = 'Scissors beats Paper!';
//both players start at zero
let userScore = 0;
let computerScore = 0;
//start game
game();

//declare playRound function (two parameters)
function playRound (playerSelection,computerSelection) {
    let result;
    //conditions for playerSelection
    switch (playerSelection) {
        case 'rock':
            if (computerSelection === 'rock')
            {
                result = 'Draw. Try Again.';
                result += '\n';
                result += `Player: ${userScore} | ${computerScore} CPU`;
            } else if (computerSelection === 'paper')
            {
                computerScore++;
                result = `${loser} ${paperWins}`;
                result += '\n';
                result += `Player: ${userScore} | ${computerScore} CPU`;
            } else if (computerSelection === 'scissors')
            {
                userScore++;
                result = `${winner} ${rockWins}`;
                result += '\n';
                result += `Player: ${userScore} | ${computerScore} CPU`;
            } else {
                result = 'not an option... Choose rock, paper or scissors.';
                result += '\n';
                result += `Player: ${userScore} | ${computerScore} CPU`;
            }
            break;
        case 'paper':
            if (computerSelection === 'paper')
            {
                result = 'Draw. Try Again.';
                result += '\n';
                result += `Player: ${userScore} | ${computerScore} CPU`;
            } else if (computerSelection === 'scissors')
            {
                computerScore++;
                result = `${loser} ${scissorsWins}`;
                result += '\n';
                result += `Player: ${userScore} | ${computerScore} CPU`;
            } else if (computerSelection === 'rock')
            {
                userScore++;
                result = `${winner} ${paperWins}`;
                result += '\n';
                result += `Player: ${userScore} | ${computerScore} CPU`;
            } else {
                result = 'not an option... Choose rock, paper or scissors.';
                result += '\n';
                result += `Player: ${userScore} | ${computerScore} CPU`;
            }
            break;
        case 'scissors':
            if (computerSelection === 'scissors')
            {
                result = 'Draw. Try Again.';
                result += '\n';
                result += `Player: ${userScore} | ${computerScore} CPU`;
            } else if (computerSelection === 'rock')
            {
                computerScore++;
                result = `${loser} ${rockWins}`;
                result += '\n';
                result += `Player: ${userScore} | ${computerScore} CPU`;
            } else if (computerSelection === 'paper')
            {
                userScore++;
                result = `${winner} ${scissorsWins}`;
                result += '\n';
                result += `Player: ${userScore} | ${computerScore} CPU`;
            } else {
                result = 'not an option... Choose rock, paper or scissors.';
                result += '\n';
                result += `Player: ${userScore} | ${computerScore} CPU`;
            }
            break;
    }
    return result;
}
//'GAME OVER' function
function endGame () {
    if (userScore > computerScore) {
        console.log("Game Over! You Win! :)");
    } else if (computerScore > userScore) {
        console.log("Game Over! You Lost! :(");
    }
}
//declare game function
function game () {
    //prompt for playerChoice
    let playerChoice = prompt(question).toLowerCase();
    let computerChoice = getComputerChoice();
    //call playRound func.
    console.log(playRound(playerChoice,computerChoice));
    //players will continue to play if their scores are lower than 5
    if (userScore < 5 && computerScore < 5) {
        game();
    } else {
        //'GAME OVER' screen
        endGame();
    }
} 