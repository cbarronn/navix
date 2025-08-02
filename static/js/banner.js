// Banner Slider
const slideItems = document.querySelectorAll('.slide-item');
const staticText = document.querySelector('.static-text');
const dynamicText = document.querySelector('.dynamic-text');

let currentSlide = 0;
const totalSlides = slideItems.length;

function updateSlide() {
    // Limpiar el slide actual
    slideItems.forEach(item => item.classList.remove('active'));
    
    // Mostrar el siguiente slide
    currentSlide = (currentSlide + 1) % totalSlides;
    slideItems[currentSlide].classList.add('active');
}

// Iniciar la animación
function startBannerAnimation() {
    // Mostrar el primer slide
    slideItems[0].classList.add('active');
    
    // Iniciar el temporizador
    setInterval(updateSlide, 3000); // Cambiar cada 3 segundos
}

// Iniciar la animación cuando el banner sea visible
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            startBannerAnimation();
        }
    });
}, { threshold: 0.1 });

observer.observe(dynamicText);
