
// document.getElementById("id_image").title = 'image'
// document.getElementById("id_body").title = ''
// if (window.history.replaceState) {
//     window.history.replaceState(null, null, window.location.href);
// }

var dropdowns = document.querySelectorAll("[data-toggle=dropdown]"); // $("btn")
var i;
var j;
for (i = 0, lendropdowns = dropdowns.length; i < lendropdowns; i++) {
    var elm = dropdowns[i];
    elm.addEventListener("click", function () {
        // this loop hides the previously clicked dropdowns
        for (j = 0, z = dropdowns.length; j < z; j++) {
            if (dropdowns[j] != this) {  // this = btn
                var elm = document.querySelector(dropdowns[j].getAttribute("data-target"));
                var str = elm.className.replace("d-block");
                elm.className = str;
            }
        }
    });
}


function ellipsisFunction(id) {
    document.getElementById("tweet-" + id).classList.toggle("d-block");
}
