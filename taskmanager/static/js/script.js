document.addEventListener('DOMContentLoaded', function() {
    //sidenav initilization
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    // datepicker initialization
    let datepicker = document.querySelectorAll(".datepicker");
    M.Datepicker.init(datepicker, {
    format: "dd mmmm, yyyy",
    // internationalization option, to help translate text when dealing with a foreign language.
    i18n: {done: "Select"}
    });
    
    // select initialization
    let selects = document.querySelectorAll("select");
    M.FormSelect.init(selects);
});