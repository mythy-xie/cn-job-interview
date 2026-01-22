// Initialize GLightbox for image enlargement
window.addEventListener('load', function() {
  const lightbox = GLightbox({
    selector: 'img[data-enlargeable]',
    openEffect: 'fade',
    closeEffect: 'fade',
    width: '90vw',
    height: '90vh'
  });
});