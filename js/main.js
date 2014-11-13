var putInCountries = function() {
    //this function is in data.js
    forEachAddress(function(addr) {
        $("#companies ul").append("<li>Coordinates: " + addr.COORD_LAT + 
                                  " " + addr.COORD_LON + "</li>");
    });
}

//this gets run onload
$(function() {
    putInCountries();
});
