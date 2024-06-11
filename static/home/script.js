const hero = document.querySelector('[data-hero]');

window.addEventListener('mousemove', (e) => {
    const { clientX, clientY } = e;
    const x = Math.round((clientX / window.innerWidth) * 100);
    const y = Math.round((clientY / window.innerHeight) * 100);

    gsap.to(hero, {
        '--x': `${x}%`,
        '--y': `${y}%`,
        duration: 0.3,
        ease: 'sine.out',
    });
});

const buttons = document.querySelectorAll('.btn');
const overlay = document.createElement('div');
overlay.className = 'transition-overlay';
document.body.appendChild(overlay);

buttons.forEach(button => {
    button.addEventListener('click', (e) => {
        if (button.href) {
            e.preventDefault();
            const { clientX, clientY } = e;
            overlay.style.left = `${clientX}px`;
            overlay.style.top = `${clientY}px`;
            overlay.classList.add('expand');

            setTimeout(() => {
                window.location.href = button.href;
            }, 1000); // 전환 시간과 일치하도록 설정

            /* 
            ---------------------------------------
            just to reset without having to refresh..
            --------------------------------*/
            setTimeout(() => { overlay.classList.remove('expand'); }, 1500);
        }
    });
});