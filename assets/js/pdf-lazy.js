(function() {
  document.addEventListener('click', function(e) {
    var btn = e.target.closest('.pdf-lazy-btn');
    if (!btn) return;
    var container = btn.closest('.pdf-lazy');
    if (!container) return;
    var src = container.getAttribute('data-src');
    var embed = document.createElement('embed');
    embed.setAttribute('src', src);
    embed.setAttribute('type', 'application/pdf');
    embed.setAttribute('width', '100%');
    embed.setAttribute('height', container.style.height || '800px');
    container.replaceWith(embed);
  });
})();
