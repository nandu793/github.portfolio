const status = document.getElementById('status');
const exploreBtn = document.getElementById('exploreBtn');
const backendBtn = document.getElementById('openBackendBtn');

exploreBtn.addEventListener('click', () => {
    window.location.href = 'frontend/index.html';
});

backendBtn.addEventListener('click', () => {
    status.textContent = 'Run backend with: cd backend && npm start';
    status.style.color = '#7dd3fc';
});
