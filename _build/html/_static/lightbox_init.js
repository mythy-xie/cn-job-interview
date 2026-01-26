// Initialize GLightbox for TikZ diagram enlargement
document.addEventListener('DOMContentLoaded', function() {
  // Find all TikZ-generated images and make them clickable
  const tikzImages = document.querySelectorAll('img[src*="tikz"]');
  
  tikzImages.forEach(img => {
    // Wrap image in a lightbox-compatible link
    const link = document.createElement('a');
    link.href = img.src;
    link.setAttribute('data-glightbox', '');
    link.setAttribute('title', img.alt || 'Diagram');
    link.style.cursor = 'pointer';
    link.style.display = 'inline-block';
    
    // Copy image attributes
    link.appendChild(img.cloneNode(true));
    img.parentNode.replaceChild(link, img);
  });
  
  // Initialize GLightbox with basic features
  const lightbox = GLightbox({
    selector: '[data-glightbox]',
    openEffect: 'fade',
    closeEffect: 'fade',
    width: '95vw',
    height: '95vh',
    touchNavigation: true,
    keyboardNavigation: true,
  });
});