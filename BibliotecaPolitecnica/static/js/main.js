const booksContainer = document.querySelector('.box-container')

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
        const bookCard = document.createElement('div')
        bookCard.classList.add('book-card')

        const bookContent = document.createElement('div')
        bookContent.classList.add('book-content')

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

        bookCard.appendChild(bookContent)

        booksContainer.appendChild(bookCard)
    }
}

renderBooks(bookList)
