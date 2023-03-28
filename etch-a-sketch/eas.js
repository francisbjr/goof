//get 'grid' div element by ID
const grid = document.getElementById('grid')
//create function called createGrid 
const createGrid = () => {
    //loop will run 16 times
    for (let i = 0; i < 16; i++) {
        //create a var that makes a child div for 'grid' 
        let div = document.createElement('div')
        grid.appendChild(div)
    }

    return
}
//call createGrid function
createGrid()