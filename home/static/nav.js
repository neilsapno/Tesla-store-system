$(document).ready(function () {
    $('.dropdown-toggle-vh').hover(function () {
        $('.collapse-discover').collapse('hide');
        $('.collapse-vehicles').collapse('show');
    });
    $('.dropdown-toggle-dscvr').hover(function () {
        $('.collapse-vehicles').collapse('hide');
        $('.collapse-discover').collapse('show');
    });
    $('.content').mouseover(function () {
        $('.collapse-vehicles').collapse('hide');
        $('.collapse-discover').collapse('hide');
    });
});