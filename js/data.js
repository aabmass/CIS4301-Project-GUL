var forEachCountry = function(toDoForEach) {
    //query the backend with jquery
    
    $.get("http://thunder.cise.ufl.edu:1111/country", function(res) {
        var countries = res.results;
        for (var i = 0; i < countries.length; ++i) {
            toDoForEach(countries[i]);
        }
    });
}
