/* Project specific Javascript goes here. */


function getCSRFToken() {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        if (cookie.substring(0, 10) == "csrftoken=") {
            return decodeURIComponent(cookie.substring(10));
        }
    }
    return "unknown";
}