
// VRIKHSHAM MOBILE NAVIGATION

const menuToggle = document.getElementById("menu-toggle");
const navLinks = document.getElementById("nav-links");

if (menuToggle && navLinks) {

    menuToggle.addEventListener("click", function () {

        navLinks.classList.toggle("show");

        const isExpanded = navLinks.classList.contains("show");

        menuToggle.setAttribute("aria-expanded", isExpanded);

    });

    // Close menu after clicking a navigation link
    navLinks.querySelectorAll("a").forEach(function (link) {

        link.addEventListener("click", function () {

            navLinks.classList.remove("show");
            menuToggle.setAttribute("aria-expanded", "false");

        });

    });

}


// =====================================
// VRIKHSHAM - PART 7 INTERACTIONS
// =====================================

// SCROLL REVEAL ANIMATION

const revealElements = document.querySelectorAll(
    ".section-heading, .feature-card, .about, .cta"
);

revealElements.forEach(function(element) {
    element.classList.add("reveal");
});

if ("IntersectionObserver" in window) {

    const revealObserver = new IntersectionObserver(function(entries, observer) {

        entries.forEach(function(entry) {

            if (entry.isIntersecting) {
                entry.target.classList.add("visible");
                observer.unobserve(entry.target);
            }

        });

    }, {
        threshold: 0.12
    });

    revealElements.forEach(function(element) {
        revealObserver.observe(element);
    });

} else {

    revealElements.forEach(function(element) {
        element.classList.add("visible");
    });

}


// BACK TO TOP BUTTON

const backToTop = document.getElementById("backToTop");

if (backToTop) {

    window.addEventListener("scroll", function() {

        if (window.scrollY > 350) {
            backToTop.classList.add("show");
        } else {
            backToTop.classList.remove("show");
        }

    });

    backToTop.addEventListener("click", function() {

        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });

    });

}
