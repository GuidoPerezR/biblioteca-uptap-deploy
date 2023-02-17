/*Programacion interfaz anadir Alumno */

const buttonAddUser = document.querySelector('.add-user-icon')
const addUserPage = document.querySelector('.add-user-page')

buttonAddUser.addEventListener('click', openAddUserPage)

function openAddUserPage(){
    addUserPage.classList.toggle('inactive');
}