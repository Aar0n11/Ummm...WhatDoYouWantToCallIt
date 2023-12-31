import './style.css'
import * as THREE from "three"

const scene = new THREE.Scene()

const camera = new THREE.PerspectiveCamera( 75, window.innerWidth! / window.innerHeight!, 0.1, 1000 )

const renderer = new THREE.WebGL1Renderer({
  canvas: document.querySelector("#bg")!
});

const geometry = new THREE.TorusGeometry( 10, 3, 16, 100)
const material = new THREE.MeshStandardMaterial({color: 0xFF6347})
const torus = new THREE.Mesh( geometry, material )

const light = new THREE.AmbientLight(0xffffff)

scene.add(torus, light)

renderer.setPixelRatio( window.devicePixelRatio )
renderer.setSize( window.innerWidth, window.innerHeight )

camera.position.setZ(30)

function animate(){
  requestAnimationFrame(animate)
  renderer.render(scene, camera)

  torus.rotation.x += 0.008
  torus.rotation.y += 0.015
  torus.rotation.z += 0.007
}

animate()