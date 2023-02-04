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


//declare function for game (two parameters)
    //call getPlayerChoice var.
    //IF getPlayerChoice equality check w/ getComputerChoice is true
        //message 'Draw'
        //refresh browser or exit game
    END //ELSE IF getPlayerChoice wins (rock > scissors) + (scissors > paper) + (paper > rock)
        //message 'Winner'
    END //ELSE getPlayerChoice loses (rock < paper) + (paper < scissors) + (scissors < rock)     
        //message 'Loser'
    END       
END    