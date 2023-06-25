
const selected = document.getElementsByClassName("selected");
const exercise = document.getElementsByClassName("exercise")
const checkboxes = document.getElementsByClassName("checkbox");
const elements = document.querySelectorAll('*');




// add eventlistener for each button and call selectAnswer function with the event and the current question object.
for (let checkbox of checkboxes) {
    checkbox.addEventListener("click", (event) => {
        selectedExercise(event);
    });
}


function selectedExercise(event){
    elements.forEach((element) => {
    element.classList.remove('selected');
    });
    event.target.classList.add("selected")
}
