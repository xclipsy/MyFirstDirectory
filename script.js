const boton = document.querySelector('.Mostrar');
const form = document.querySelector('.forms');

boton.addEventListener('click', () => {
    if (form.style.display === 'none' ){
        form.style.display = 'block'
    }else{
        form.style.display = 'none'
    }

})

window.onload = function(){
    alert("Se cargo la pagina 🗣️")
}