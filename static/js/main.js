window.addEventListener('load', function() {
    if (window.location.pathname === '/') {
        // Check if intro was already shown
        if (!sessionStorage.getItem('introShown')) {
            document.getElementById('intro').style.display = 'flex';
            setTimeout(function() {
                document.getElementById('intro').classList.add('hidden');
                // Mark intro as shown
                sessionStorage.setItem('introShown', 'true');
            }, 2500);
        } else {
            document.getElementById('intro').style.display = 'none';
        }
    } else {
        document.getElementById('intro').style.display = 'none';
    }
});