/*let Libro = document.getElementById('libro1');

let hidetext = document.getElementById('hidetext');

Libro.addEventListener('click', toggleText);

function toggleText(){
    hidetext.classList.toggle('show')
}

let Libro2 = document.getElementById('libro2');

let hidetext2 = document.getElementById('hidetext2');

Libro2.addEventListener('click', toggleText2);

function toggleText2(){
    hidetext2.classList.toggle('show')
}

let Libro3 = document.getElementById('libro3');

let hidetext3 = document.getElementById('hidetext3');

Libro3.addEventListener('click', toggleText3);

function toggleText3(){
    hidetext3.classList.toggle('show')
}

let Libro4 = document.getElementById('libro4');

let hidetext4 = document.getElementById('hidetext4');

Libro4.addEventListener('click', toggleText4);

function toggleText4(){
    hidetext4.classList.toggle('show')
}*/

const bookList = []
bookList.push({
    name:'Inteligencia Artificial',
    author: 'Yo mero',
    available: '10',
    image: '{%static "images/libro2.jpg"%}'
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

function renderBooks(arr){
    for(book of arr){
        const book = document.createElement('div')
        book.classList.add('book-card')

        const bookContent = document.createElement('div')
        bookInfo.classList.add('book-content')

        const bookButton = document.createElement('button')
        const bookImg = document.createElement('img')
        bookImg.setAttribute('src', book.image)
        const bookName = document.createElement('p')
        bookName.innerText = book.name
        const bookInfo = document.createElement('div')
        bookInfo.classList.add('book-info')
        const bookAuthor = document.createElement('p')
        bookAuthor.innerText = book.author
        const bookAvailable = document.createElement('p')
        bookAvailable.innerText = book.available

        bookInfo.append(bookAuthor, bookAvailable)

        bookButton.append(bookImg, bookName, bookInfo)

        bookContent.appendChild(bookButton)

        book.appendChild(bookContent)

    }
}

renderBooks(bookList)
