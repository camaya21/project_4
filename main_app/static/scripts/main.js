$(".navbar-burger").click(function () {
    // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
    $(".navbar-burger").toggleClass("is-active");
    $(".navbar-menu").toggleClass("is-active");
});

const exAmount = document.querySelectorAll('ex-amount')
const budAmount = document.querySelectorAll('bud-amount')

function subtract(exAmount, budAmount){
    return exAmount-budAmount;
}
subtract()