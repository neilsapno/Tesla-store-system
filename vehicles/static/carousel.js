$(document).ready(function () {
    const color1 = $('#colorOption1')
    const color2 = $('#colorOption2')
    const color3 = $('#colorOption3')
    const color4 = $('#colorOption4')
    const carouselVeh = $('#carouselVeh')

    color1.click(function () {
        carouselVeh.carousel(0);
    })

    color2.click(function () {
        carouselVeh.carousel(1);
    })

    color3.click(function () {
        carouselVeh.carousel(2);
    })

    color4.click(function () {
        carouselVeh.carousel(3);
    })

});