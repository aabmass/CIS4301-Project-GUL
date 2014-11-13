var putInCountries = function() {
    //this function is in data.js
    forEachCountry(function(country) {
        $("#companies ul").append("<li>" + country.NAME + "</li>");
    });
}

//this gets run onload
$(function() {
    putInCountries();
});
