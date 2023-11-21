// responsive navbar 'hamburger' --------------------------------
var bar = document.getElementById("bar");
var close = document.getElementById("close");
var nav = document.getElementById("navbar");
if (bar) {
    bar.addEventListener("click", () => {
        nav.classList.add("active");
    })
}
if (close) {
    close.addEventListener("click", () => {
        nav.classList.remove("active");
    })
}

// effects on navbar while scrolling -------------------------------------
gsap.to("#header", {
    // backgroundColor: "#0000006e",
    background: "rgba(0,0,0,.7)",
    // duration: 0.5,
    height: "75",
    scrollTrigger: {
        trigger: "#header",
        scroller: "body",
        // markers: true,
        start: "top -10%",
        end: "top -11%",
        scrub: 1.3,

    },

});


// trending trailler slider -----------------------------------

const scrollers = document.querySelectorAll(".trending-movie-head");

// If a user hasn't opted in for recuded motion, then we add the animation
if (!window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    addAnimation();
}

function addAnimation() {
    scrollers.forEach((scroller) => {
        // add data-animated="true" to every `.scroller` on the page
        scroller.setAttribute("data-animated", true);

        // Make an array from the elements within `.scroller-inner`
        const scrollerInner = scroller.querySelector(".trending-movie-content");
        const scrollerContent = Array.from(scrollerInner.children);

        // For each item in the array, clone it
        // add aria-hidden to it
        // add it into the `.scroller-inner`
        scrollerContent.forEach((item) => {
            const duplicatedItem = item.cloneNode(true);
            duplicatedItem.setAttribute("aria-hidden", true);
            scrollerInner.appendChild(duplicatedItem);
        });
    });
}

// preloader

// var loader = document.getElementById("preloader");
// window.addEventListener("load", function() {
//     loader.style.display = "none"
// })



// trailler popup


const posters = document.querySelectorAll('.watch-trailler-1');
const videoPopup = document.getElementById('videoPopup');
const videoIframe = document.getElementById('videoIframe');
const closePopup = document.getElementById('closePopup');

posters.forEach(poster => {
    poster.addEventListener('click', () => {
        const videoId = poster.getAttribute('data-video-id');
        const videoUrl = `https://www.youtube.com/embed/${videoId}?autoplay=1&mute=1&vq=hd1080&modestbranding=1&rel=0&iv_load_policy=3&color=white`;
        videoIframe.src = videoUrl;
        videoPopup.style.display = 'flex';
        videoPopup.style.zIndex = 9999999;
        videoPopup.style.justifyContent = 'center';
        videoPopup.style.position = 'fixed';
        videoPopup.style.alignItems = 'center';

    });
});

closePopup.addEventListener('click', () => {
    videoIframe.src = '';
    videoPopup.style.display = 'none';
});

window.addEventListener('click', (event) => {
    if (event.target === videoPopup) {
        videoIframe.src = '';
        videoPopup.style.display = 'none';
    }
});


// mute/unmute after page load (hot-thrills section)


document.addEventListener('DOMContentLoaded', function() {
    const videos = document.querySelectorAll('.video');
    const muteButtons = document.querySelectorAll('.mute-button');

    function toggleIcon(video, button, index) {
        if (video.muted) {
            button.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-volume-mute" viewBox="0 0 16 16">
                            <path d="M6.717 3.55A.5.5 0 0 1 7 4v8a.5.5 0 0 1-.812.39L3.825 10.5H1.5A.5.5 0 0 1 1 10V6a.5.5 0 0 1 .5-.5h2.325l2.363-1.89a.5.5 0 0 1 .529-.06zM6 5.04 4.312 6.39A.5.5 0 0 1 4 6.5H2v3h2a.5.5 0 0 1 .312.11L6 10.96V5.04zm7.854.606a.5.5 0 0 1 0 .708L12.207 8l1.647 1.646a.5.5 0 0 1-.708.708L11.5 8.707l-1.646 1.647a.5.5 0 0 1-.708-.708L10.793 8 9.146 6.354a.5.5 0 1 1 .708-.708L11.5 7.293l1.646-1.647a.5.5 0 0 1 .708 0z"/>
                          </svg>`; // mute
        } else {
            button.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-volume-up" viewBox="0 0 16 16">
                            <path d="M10.121 12.596A6.48 6.48 0 0 0 12.025 8a6.48 6.48 0 0 0-1.904-4.596l-.707.707A5.483 5.483 0 0 1 11.025 8a5.483 5.483 0 0 1-1.61 3.89l.706.706z"/>
                            <path d="M10.025 8a4.486 4.486 0 0 1-1.318 3.182L8 10.475A3.489 3.489 0 0 0 9.025 8c0-.966-.392-1.841-1.025-2.475l.707-.707A4.486 4.486 0 0 1 10.025 8zM7 4a.5.5 0 0 0-.812-.39L3.825 5.5H1.5A.5.5 0 0 0 1 6v4a.5.5 0 0 0 .5.5h2.325l2.363 1.89A.5.5 0 0 0 7 12V4zM4.312 6.39 6 5.04v5.92L4.312 9.61A.5.5 0 0 0 4 9.5H2v-3h2a.5.5 0 0 0 .312-.11z"/>
                          </svg>`; // unmute
        }
    }
    // Function to save the mute state in localStorage
    function saveMuteState(video, index) {
        localStorage.setItem(`video${index}`, video.muted);
    }

    for (let i = 0; i < muteButtons.length; i++) {
        const video = videos[i];
        const button = muteButtons[i];

        // Add a click event listener to the mute button
        button.addEventListener('click', () => {
            video.muted = !video.muted;
            toggleIcon(video, button, i);
            saveMuteState(video, i);
        });

        // Retrieve the mute state from localStorage and set the video's muted property
        const isMuted = localStorage.getItem(`video${i}`);
        if (isMuted === 'true') {
            video.muted = true;
        } else {
            video.muted = false;
        }

        // Initialize button text/icon based on the initial muted state
        toggleIcon(video, button, i);
    }

    // Listen for Bootstrap carousel slide event
    const carousel = document.getElementById('carouselExampleInterval');
    carousel.addEventListener('slide.bs.carousel', function(event) {
        // Mute all videos when switching to a new slide
        videos.forEach(video => {
            video.muted = true;
        });

        // Update the icons for all mute buttons in the new slide
        muteButtons.forEach((button, index) => {
            toggleIcon(videos[index], button, index);
        });

        // Save the mute state for videos in the current slide
        videos.forEach((video, index) => {
            saveMuteState(video, index);
        });
    });
});


// muteUnmute.js method 2

// document.addEventListener('DOMContentLoaded', function() {
//     const videos = document.querySelectorAll('.video');
//     const muteButtons = document.querySelectorAll('.mute-button');

//     function toggleIcon(video, button, index) {
//         if (video.muted) {
//             button.innerHTML = `
//             <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-volume-mute" viewBox="0 0 16 16">
//             <path d="M6.717 3.55A.5.5 0 0 1 7 4v8a.5.5 0 0 1-.812.39L3.825 10.5H1.5A.5.5 0 0 1 1 10V6a.5.5 0 0 1 .5-.5h2.325l2.363-1.89a.5.5 0 0 1 .529-.06zM6 5.04 4.312 6.39A.5.5 0 0 1 4 6.5H2v3h2a.5.5 0 0 1 .312.11L6 10.96V5.04zm7.854.606a.5.5 0 0 1 0 .708L12.207 8l1.647 1.646a.5.5 0 0 1-.708.708L11.5 8.707l-1.646 1.647a.5.5 0 0 1-.708-.708L10.793 8 9.146 6.354a.5.5 0 1 1 .708-.708L11.5 7.293l1.646-1.647a.5.5 0 0 1 .708 0z"/>
//           </svg>`; // mute
//         } else {
//             button.innerHTML = `
//             <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-volume-up" viewBox="0 0 16 16">
//             <path d="M10.121 12.596A6.48 6.48 0 0 0 12.025 8a6.48 6.48 0 0 0-1.904-4.596l-.707.707A5.483 5.483 0 0 1 11.025 8a5.483 5.483 0 0 1-1.61 3.89l.706.706z"/>
//             <path d="M10.025 8a4.486 4.486 0 0 1-1.318 3.182L8 10.475A3.489 3.489 0 0 0 9.025 8c0-.966-.392-1.841-1.025-2.475l.707-.707A4.486 4.486 0 0 1 10.025 8zM7 4a.5.5 0 0 0-.812-.39L3.825 5.5H1.5A.5.5 0 0 0 1 6v4a.5.5 0 0 0 .5.5h2.325l2.363 1.89A.5.5 0 0 0 7 12V4zM4.312 6.39 6 5.04v5.92L4.312 9.61A.5.5 0 0 0 4 9.5H2v-3h2a.5.5 0 0 0 .312-.11z"/>
//           </svg>`; // unmute
//         }
//     }

//     for (let i = 0; i < muteButtons.length; i++) {
//         const video = videos[i];
//         const button = muteButtons[i];

//         // Add a click event listener to the mute button
//         button.addEventListener('click', () => {
//             video.muted = !video.muted;
//             toggleIcon(video, button, i);
//         });

//         // Initialize button text/icon based on the initial muted state
//         toggleIcon(video, button, i);
//     }

//     // Listen for Bootstrap carousel slide event
//     const carousel = document.getElementById('carouselExampleInterval');
//     carousel.addEventListener('slide.bs.carousel', function(event) {
//         // Mute all videos when switching to a new slide
//         videos.forEach(video => {
//             video.muted = true;
//         });

//         // Update the icons for all mute buttons in the new slide
//         muteButtons.forEach((button, index) => {
//             toggleIcon(videos[index], button, index);
//         });
//     });
// });


//  autoplay when hover the poster -------------------------------------

const movieContainers = document.querySelectorAll('.movie-container');

movieContainers.forEach((container) => {
    const iframe = container.querySelector('iframe');
    const originalSrc = iframe.src;

    container.addEventListener('mouseenter', () => {
        iframe.src = originalSrc;
    });

    container.addEventListener('mouseleave', () => {
        iframe.src = ''; // This will stop the video
    });
});

// back to top button

function addBackToTopButton(buttonId, minScrollY = 1000) {
    const button = document.getElementById(buttonId);

    if (!button) {
        return; // Button not found, do nothing
    }

    window.addEventListener("scroll", function() {
        if (window.pageYOffset > minScrollY) {
            button.style.display = "block";
        } else {
            button.style.display = "none";
        }
    });

    button.addEventListener("click", function() {
        window.scrollTo({
            top: 0,
            behavior: "smooth",
        });
    });
}


// latest movie update


const updateContainer = document.getElementById('latest_movie_update_container');

updateContainer.addEventListener('mouseenter', () => {
    updateContainer.style.animationPlayState = 'paused';
});

updateContainer.addEventListener('mouseleave', () => {
    updateContainer.style.animationPlayState = 'running';
});


// catagories slider


var mySwiper = new Swiper('.swiper', {
    // Optional parameters
    spaceBetween: 8,
    slidesPerView: 2,
    loop: true,
    freeMode: true,
    loopAdditionalSlides: 5,
    speed: 1000,
    // Navigation arrows
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    breakpoints: {
        // when window width is >= 640px
        640: {
            slidesPerView: 5,
            slidesPerGroup: 5,
            freeMode: true,
        }
    }
})



// live search