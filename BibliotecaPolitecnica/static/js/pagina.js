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

/*Programacion carrito de libros*/
const buttonOpenBookCart = document.querySelector('.book-cart-icon')
const bookCart = document.querySelector('.aside-book-cart')
const buttonCloseBookCart = document.querySelector('.book-card-head-content-image')

buttonOpenBookCart.addEventListener('click', openBookCart);
buttonCloseBookCart.addEventListener('click', closeBookCart);

function openBookCart(){
    bookCart.classList.remove('inactive');
}

function closeBookCart(){
    bookCart.classList.add('inactive');
}

console.log("que onda ")