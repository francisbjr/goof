//create 'getComputerChoice' function
function getComputerChoice () {
    //create an array with 'rock + paper + scissors'
    let choice = ['rock', 'paper', 'scissors'];
    //create a variable that will pick a random string out of the array
    let random = Math.floor(Math.random() * choice.length);
    //return the variable
    return choice[random];
}

console.log(getComputerChoice());