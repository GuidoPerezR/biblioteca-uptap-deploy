/*Programacion Slider*/ 
const prev = document.querySelector('.prev')
const next = document.querySelector('.next')
const slider = document.querySelector('.slider')

prev.addEventListener('click', () => (
    slider.scrollLeft -= 600
))

next.addEventListener('click', () => (
    slider.scrollLeft += 600
))

/*Programacion menu de vistas de la pagina de libros*/
const buttonBookCart = document.querySelector('.book-cart-icon')
const buttonUserMenu = document.querySelector('.user-icon')
const bookCart = document.querySelector('.aside-book-cart')
const userMenu = document.querySelector('.aside-user-menu')

buttonUserMenu.addEventListener('click', toggleUserMenu)
buttonBookCart.addEventListener('click', toggleBookCart)

function toggleUserMenu(){
    const isBookCartClosed = bookCart.classList.contains('inactive')

    if(!isBookCartClosed){
        bookCart.classList.add('inactive')
    }

    userMenu.classList.toggle('inactive')
}

function toggleBookCart(){
    const isUserMenuClosed = userMenu.classList.contains('inactive')

    if(!isUserMenuClosed){
        userMenu.classList.add('inactive')
    }

    bookCart.classList.toggle('inactive')
}

console.log(" sssonda ")