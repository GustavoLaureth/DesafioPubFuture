buttonMenu = document.getElementById('buttonMenu')
arrow = document.getElementById('arrow')
menu = document.getElementById('menu')

let cont = 1

function InterageMenu() {
    if (cont % 2 == 0) {
        cont = cont + 1
        menu.style.display = 'none'
        arrow.style.transform = 'rotate(0deg)'
        arrow.style.transitionDuration = '.5s'
    }
    else {
        cont = cont + 1
        menu.style.display = 'block'
        arrow.style.transform = 'rotate(-90deg)'
        arrow.style.transitionDuration = '.5s'
    }
}
