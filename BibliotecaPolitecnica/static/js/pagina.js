console.log("joto")
const prev = document.querySelector('.prev')
const next = document.querySelector('.next')
const slider = document.querySelector('.slider')

prev.addEventListener('click', () => (
    slider.scrollLeft -= 600
))

next.addEventListener('click', () => (
    slider.scrollLeft += 600
))