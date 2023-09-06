import './style.css'

const moveBy = 10
const character = document.getElementById("character")
let charPos = [0, 0]
const constrained: boolean = true

window.addEventListener('load', () => {
  character!.style.position = 'absolute'
  character!.style.left = "0px"
  character!.style.top = "0px"
})

document.addEventListener("keypress", (e) => {
  switch(e.key){
    case (('w') || ('UpArrow')):
      character!.style.top = parseInt(character!.style.top) - moveBy + 'px'
      charPos[1] = Number(character!.style.top.replace('px', ''))
      break

    case 's':
      character!.style.top = parseInt(character!.style.top) + moveBy + 'px'
      charPos[1] = Number(character!.style.top.replace('px', ''))
      break
    
    case 'a':
      character!.style.left = parseInt(character!.style.left) - moveBy + 'px'
      charPos[0] = Number(character!.style.left.replace("px", ""))
      break

    case 'd':
      character!.style.left = parseInt(character!.style.left) + moveBy + 'px'
      charPos[0] = Number(character!.style.left.replace("px", ""))
      break
    }
  if(constrained === true) {

  if(charPos[0] < 0){
    character!.style.left = 0 + "px"
  }
  if(charPos[0] > window.innerWidth - 102){
    character!.style.left = (window.innerWidth - 102) + 'px'
  }
  if(charPos[1] > window.innerHeight - 102){
    character!.style.top = (window.innerHeight - 102) + 'px'
  }
  if(charPos[1] < 0){
    character!.style.top = 0 + 'px'
  }
  }
  }
)