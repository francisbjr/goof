//get 'grid' div element by ID
const grid = document.getElementById('grid')
//create function called createGrid 
const createGrid = () => {
    //loop will run 16 times
    for (let i = 0; i < 4; i++) {
        //create a var that makes a child div for 'grid' 
        let divRow = document.createElement('div')
        divRow.setAttribute('id', 'divRow')
        grid.appendChild(divRow)
        
        for (let i = 0; i < 4; i++) {
            let divColumn = document.createElement('div')
            divColumn.setAttribute('id', 'divColumn')
            divColumn.addEventListener("mouseover", () => divColumn.style.cssText = 'background: red;')
            divRow.appendChild(divColumn)
        }
    }

    return
}
//call createGrid function
createGrid()