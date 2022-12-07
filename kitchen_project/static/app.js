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
