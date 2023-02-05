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
const buttonBookCart = document.querySelector('.book-cart-icon')
const bookCart = document.querySelector('.aside-book-cart')

buttonBookCart.addEventListener('click', toggleBookCart);

function openBookCart(){
    bookCart.classList.remove('inactive');
}

console.log("que onda ")

/*
const booksContainer = document.querySelector('.books-container')

const bookList = []
bookList.push({
    name:'Ingenieria del software: Un enfoque practico',
    author: 'Rogger S. Pressman',
    available: 2,
    editorial: 'Mc Graw hill, Septima Edicion(2 abril 2019)',
    languague: 'Español',
    pages: 300,
    image: 'https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940'
})

bookList.push({
    name:'Ingenieria del software: Un enfoque practico',
    author: 'Rogger S. Pressman',
    available: '2',
    image: 'https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940'
})

bookList.push({
    name:'Ingenieria del software: Un enfoque practico',
    author: 'Rogger S. Pressman',
    available: '2',
    image: 'https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940'
})

bookList.push({
    name:'Ingenieria del software: Un enfoque practico',
    author: 'Rogger S. Pressman',
    available: '2',
    image: 'https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940'
})

bookList.push({
    name:'Ingenieria del software: Un enfoque practico',
    author: 'Rogger S. Pressman',
    available: '2',
    image: 'https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940'
})

bookList.push({
    name:'Ingenieria del software: Un enfoque practico',
    author: 'Rogger S. Pressman',
    available: '2',
    image: 'https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940'
})

/* <div class="book">
                <div class="contenido">
                    <button type="button" id="libro2">
                        <img src="{%static 'images/libro2.jpg'%}" width="150" height="250" >
                        <h5>Inteligencia Artificial con aplicaciones a la ingeniería</h5>
                        <div class="info">
                            <h6>Pedro Ponce Cruz</h6>
                            <h6>Disponibles: 0</h6>
                        </div>
                    </button>                    
                </div>
            </div>
*/
/*
function renderBooks(arr){
    for(book of arr){
        const bookCard = document.createElement('div')
        bookCard.classList.add('book-card')

        const bookContent = document.createElement('div')
        bookContent.classList.add('book-content')

        const bookButton = document.createElement('button')
        const bookImg = document.createElement('img')
        bookImg.setAttribute('src', book.image)
        const bookName = document.createElement('p')
        bookName.classList.add('book-title')
        bookName.innerText = book.name
        const bookInfo = document.createElement('div')
        bookInfo.classList.add('book-info')
        const bookAuthor = document.createElement('p')
        bookAuthor.innerText = book.author
        const bookAvailable = document.createElement('p')
        bookAvailable.innerText = 'Disponibles: ' + book.available

        bookInfo.append(bookAuthor, bookAvailable)

        bookButton.append(bookImg, bookName, bookInfo)

        bookContent.appendChild(bookButton)

        bookCard.appendChild(bookContent)

        booksContainer.appendChild(bookCard)

        /* <div class="tarjeta" align="center"> 
                        <div class="contenido">
                            <h3>Ingeniería del software: Un enfoque práctico</h3>
                            <h5>por Rogger S. Pressman</h5>
                            <h5>Disponibles: 2</h5>
                            <br>
                            <h3>Detalle del libro</h3>
                            <h5>Editorial: Mc Graw hill, Septima Edicion(2 abril 2019)</h5>
                            <h5>Idioma: Español</h5>
                            <h5>Pasta blanda: 300 páginas</h5>
                            <a href="#" id="Solicitar">Solicitar</a>
                            <a href="#"id="Añadir">Añadir al carrito</a>
                        </div>
                </div> */
/*
        const hiddenCard = document.createElement('div')
        hiddenCard.classList.add('hidden-card')

        const hiddenCardContent = document.createElement('div')
        hiddenCardContent.classList.add('hidden-card-content')

        const bookDetail = document.createElement('p')
        bookDetail.innerText = 'Detalle del libro'
        const bookEditorial = document.createElement('p')
        bookEditorial.innerText = 'Editorial: ' + book.editorial
        const bookLanguague = document.createElement('p')
        bookLanguague.innerText = 'Idioma: ' + book.languague
        const bookPages = document.createElement('p')
        bookPages.innerText = 'Páginas: ' + book.pages
        const buttonSolicitar = document.createElement('a')
        buttonSolicitar.classList.add('boton-solicitar')
        buttonSolicitar.innerText = 'Solicitar'
        const buttonAnadir = document.createElement('a')
        buttonAnadir.classList.add('boton-anadir')
        buttonAnadir.innerText = 'Añadir al carrito'

        hiddenCardContent.append(bookDetail, bookEditorial, bookLanguague,
            bookPages, buttonSolicitar, buttonAnadir)

        hiddenCard.appendChild(hiddenCardContent)

        booksContainer.appendChild(hiddenCardContent)
    }
}

//renderBooks(bookList)*/
