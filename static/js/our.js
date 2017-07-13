$(document).ready(function () {
    var isHidden = false;
    $("#clicker").click(function () {
        if (isHidden) {
            $(".list").fadeTo(1000, 0.1)

        } else {
            $(".list").fadeTo(1000, 0.9)
        }
        isHidden = !isHidden;
    })

    $('#my_name').t({
        speed:70
        blink:400
        mistype:0
    })
})