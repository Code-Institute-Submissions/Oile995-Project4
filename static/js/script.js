
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
    console.log(event.target.id)
    exercise_slug = event.target.id
    showExercise(exercise_slug);
}

function showExercise(exercise_slug){
    let collection = document.getElementsByClassName(exercise_slug);
    let allexercises = document.querySelectorAll('.exercise');
    allexercises.forEach((exercise) => {
        exercise.classList.add('hidden');
        });
    if(collection[0].classList.contains("hidden")){
        collection[0].classList.remove("hidden")

    }
    else{
        collection[0].classList.add("hidden")
    }
}

