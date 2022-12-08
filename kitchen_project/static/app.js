// RECIPE CARD FLIP ---------------------------------

let front_btn = document.querySelector('#front-btn')
let back_btn = document.querySelector('#back-btn')

let front = document.querySelector('#front')
let back = document.querySelector('#back')

front_btn.onclick = function() {
  front.style.display = 'none'
  back.style.display = 'flex'
}

back_btn.onclick = function() {
  front.style.display = 'flex'
  back.style.display = 'none'
}

// MANUALLY ADD TO WHITEBOARD ---------------------------

// let needs = document.querySelector('#needs')
// let todo = document.querySelector('#todo')

// let needs_p = document.querySelector('#needs-p')
// let todo_p = document.querySelector('#todo-p')

// let needs_a = document.querySelector('#needs-a')
// let todo_a = document.querySelector('#todo-a')

// let whiteboard_input_needs = document.querySelector('#whiteboard-input-needs')

// let whiteboard_input_todo = document.querySelector('#whiteboard-input-todo')

// whiteboard_input_needs.addEventListener('keypress', function(event) {
//   if (event.key === 'return'){
//     needs_a = whiteboard_input_needs.value
//     needs_p.style.display = 'flex'
//     whiteboard_input_needs.value = ''
//   }
// })


// MANUALLY REMOVE FROM WHITEBOARD ----------------------


// MANUALLY CHECK OFF WHITEBOARD ----------------------


// CHANGE ARROW ON PREP SORT BUTTON --------------------

// let prep_btn_1 = document.querySelector('#prep-btn-1')
// // let prep_btn_2 = document.querySelector('#prep-btn-2')

// prep_btn_1.onclick = function(){
//   prep_btn_1.innerHTML = '&#8595;'

// }

// prep_btn_1.onclick = function() {
//   if (prep_btn_1.innerHTML === '&#8593;'){
//     prep_btn_1.innerHTML = '&#8595;'
//   }
//   else if (prep_btn_1.innerHTML === '&#8595;') {
//     prep_btn_1.innerHTML = '&#8593;'
//   }
// }

// prep_btn_2.onclick = function() {
//   prep_btn_2.style.display = 'none'
//   prep_btn_1.style.display = 'block'
// }

// const app = Vue.createApp({
//   delimiters: ['[[', ']]'],
//   data(){
//       return{
//           name: 'dude'
//       }
//   },
//   methods:{

//   },
//   mounted(){
//     console.log('suppppp')
//   }
// })
