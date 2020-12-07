$('document').ready(function() {
    var checkBox = document.getElementById("cbx");


    if (checkBox.checked == false) {
        $('#matchNumber').attr("required", "false")

    }
});