/* ==========================================================
   Developer Work Pattern Analyzer
   Version 1.0
========================================================== */

"use strict";

/* ==========================================================
   Disable Button During Analysis
========================================================== */

const form = document.querySelector("form");

if (form) {

    form.addEventListener("submit", function () {

        const button = document.querySelector(".analyze-btn");

        if (button) {

            button.disabled = true;

            button.innerHTML = "Analyzing...";

        }

    });

}


/* ==========================================================
   Auto Hide Flash Messages
========================================================== */

setTimeout(function () {

    const flash = document.querySelector(".flash-container");

    if (!flash)
        return;

    flash.style.transition = "0.5s";

    flash.style.opacity = "0";

    setTimeout(function () {

        flash.remove();

    }, 500);

}, 3000);


/* ==========================================================
   Smooth Card Hover
========================================================== */

document.querySelectorAll(".card").forEach(card => {

    card.addEventListener("mouseenter", function () {

        card.style.transform = "translateY(-5px)";

        card.style.transition = "0.3s";

    });

    card.addEventListener("mouseleave", function () {

        card.style.transform = "translateY(0px)";

    });

});