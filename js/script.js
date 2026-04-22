const toggleBtn = document.querySelector('.toggle-form');
const contactForm = document.querySelector('.contact-form');
 
/* Toggle the contact form visibility on button click and the color*/
toggleBtn.addEventListener('click', () => {
    if (contactForm.style.display === 'none') {
        contactForm.style.display = 'block';
        toggleBtn.style.color = '#e6ccb2';
    } else {
        contactForm.style.display = 'none';
        toggleBtn.style.color = '';
    }
});
 
/* Show a welcome message when the page finishes loading */
window.onload = function () {
    alert("Welcome to my website, hope you enjoy it =)");
};