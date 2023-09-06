import './style.css'

const moveBy = 10
const character = document.getElementById("character")
let charPos = [0, 0]
let charSize = [Number(character!.style.width.replace("px", "")), Number(character!.style.height.replace("px", ""))]

window.addEventListener('load', () => {
  character!.style.position = 'absolute'
  character!.style.left = "0px"
  character!.style.top = "0px"
})

document.addEventListener("keypress", (e) => {
  switch(e.key){
    case 'w':
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

  if(charPos[0] < 0){
    character!.style.left = 0 + "px"
  }
  if(charPos[0] > window.innerWidth){
    character!.style.left = window.innerWidth - charSize[0] + 'px'
  }
  if(charPos[1] > window.innerHeight){
    character!.style.top = window.innerHeight - charSize[1] + 'px'
  }
  if(charPos[1] < 0){
    character!.style.top = 0 + 'px'
  }
  }
)