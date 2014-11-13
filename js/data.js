var forEachAddress = function(toDoForEach) {
    //query the backend with jquery
    
    $.get("http://thunder.cise.ufl.edu:1111/address", function(res) {
        var addresses = res.addresses;
        for (var i = 0; i < addresses.length; ++i) {
            toDoForEach(addresses[i]);
        }
    });
}
