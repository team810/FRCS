$(document).ready(function(){
        $("#team_num_reg").keyup(function() {
        console.log("TEST")
        var teamNumber = $("#team_num_reg").val();
        $.get("https://www.thebluealliance.com/api/v3/team/frc" + teamNumber + "/simple", {"X-TBA-Auth-Key": "PzOW8s1DYGlVkgAsikwVlhy5wZ5Tm85fKSjd0DfiUJFQOGhsReyZEf88EEoAU1Cw"}, function(data){
            var jObject = (data);
            $("#welcome-team").html("Welcome" + " " + '"' + jObject['nickname'] + '"');
        }).fail(function(){
            $("#welcome-team").html("Invalid team number...");
        });
    })

    $("#id_username").keyup(function() {

        user = $("#id_username").val()
        var settings = {
        "url": "http://127.0.0.1:8000/api/User/" + user,
        "method": "GET",
        "timeout": 0,
        "error": function(status){
            if(status = 404){
            $("#user-match").text(" ");
            $('.user-label').css({"background-image": "linear-gradient(90deg, #8A2387, #e94057,#F27121)", "-webkit-background-clip": "text", "-webkit-text-fill-color": "transparent"});

            
        }
        }
        };
        $.ajax(settings).done(function (response) {
        if(response['username'] == user){
            $("#user-match").text('Username is already in use')
            $('.user-label').css({"background-image": "", "-webkit-background-clip": "", "-webkit-text-fill-color": ""});
            
        }
        });         
    })

    $("#email-form").keyup(function() {

        email = $("#email-form").val()
        user = $("#id_username").val()
        var settings = {
        "url": "http://127.0.0.1:8000/api/User/" + user,
        "method": "GET",
        "timeout": 0,
        "error": function(status){
            if(status = 404){
            $("#email-exist").text(" ");
        }
        }
        };
        $.ajax(settings).done(function (response) {

        if(response['email'] == email){
            $("#email-exist").text('Username is already in use')
            $('.email-label').css({"background-image": "", "-webkit-background-clip": "", "-webkit-text-fill-color": ""});

            
        }
        else{
            $("#email-exist").text(' ')
            
        }
        });         
    })

    
        $("#password-form").keyup(function() {


            var goodColor = "#66cc66";
            var badColor = "#ff6666";

            var email = $('#email-form').val()

            var name = email.substring(0, email.lastIndexOf("@"));
            
            if(name == this.value){
                document.getElementById('pass-similar').style.color  = badColor
            }
            else{
                document.getElementById('pass-similar').style.color  = goodColor
            }
            
            
            //check if password is long enough
            if(this.value.length >= 6) {
                document.getElementById('pass-character').style.color  = goodColor
            }
            else{
                document.getElementById('pass-character').style.color  = badColor
            }

            //check if password has a number
            var hasNumber = /\d/;
            if(hasNumber.test($("#password-form").val())) {
                document.getElementById('pass-number').style.color  = goodColor

            }
            else{
                document.getElementById('pass-number').style.color  = badColor
            }

            var hasUppercase = /[A-Z]/

            if(hasUppercase.test($("#password-form").val())){
                document.getElementById('pass-letter').style.color  = goodColor
            }
            else{
                document.getElementById('pass-letter').style.color  = badColor
            }

            if(hasUppercase.test($("#password-form").val()) && hasNumber.test($("#password-form").val()) && this.value.length >= 6){
                $('.pass-label').css({"background-image": "linear-gradient(90deg, #8A2387, #e94057,#F27121)", "-webkit-background-clip": "text", "-webkit-text-fill-color": "transparent"});
            }
            else{
                $('.pass-label').css({"background-image": "", "-webkit-background-clip": "", "-webkit-text-fill-color": ""});
            }


            
    });

    $("#email-form").keyup(function() {
        

        var goodColor = "#66cc66";
        var badColor = "#ff6666";

        if(name == $("#password-form").val()){
            document.getElementById('pass-similar').style.color  = badColor
            }
        else{
            document.getElementById('pass-similar').style.color  = goodColor
            
            }

            var email_validity = new RegExp(/^(("[\w-\s]+")|([\w-]+(?:\.[\w-]+)*)|("[\w-\s]+")([\w-]+(?:\.[\w-]+)*))(@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$)|(@\[?((25[0-5]\.|2[0-4][0-9]\.|1[0-9]{2}\.|[0-9]{1,2}\.))((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\.){2}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\]?$)/i);
            if(email_validity.test($('#email-form').val())){
                $('.email-label').css({"background-image": "linear-gradient(90deg, #8A2387, #e94057,#F27121)", "-webkit-background-clip": "text", "-webkit-text-fill-color": "transparent"});
            }
            else{
                $('.email-label').css({"background-image": "", "-webkit-background-clip": "", "-webkit-text-fill-color": ""});
            }

    })
        setInterval(function(){
        if($('#welcome-team').html() != 'Invalid team number...'){
            $('.team-label').css({"background-image": "linear-gradient(90deg, #8A2387, #e94057,#F27121)", "-webkit-background-clip": "text", "-webkit-text-fill-color": "transparent"});
        }
        else{
            
            $('.team-label').css({"background-image": "", "-webkit-background-clip": "", "-webkit-text-fill-color": ""});
        }
    }, 300);
    });


    $(document).ready(function(){

        $("#password-match").keyup(function() {


            var goodColor = "#66cc66";
            var badColor = "#ff6666";

            
            if($("#password-match").val() == $("#password-form").val()){
                document.getElementById('pass-match').style.color  = goodColor
                $('.verify-pass-label').css({"background-image": "linear-gradient(90deg, #8A2387, #e94057,#F27121)", "-webkit-background-clip": "text", "-webkit-text-fill-color": "transparent"});
            }
            else{
                document.getElementById('pass-match').style.color  = badColor
               
            }
                   
            
        })
        setInterval(function(){
            var goodColor = "#66cc66";

            if($("#user-match").text() == ' ' && $('#pass-letter').css("color") == 'rgb(102, 204, 102)' && $('#pass-number').css("color") == 'rgb(102, 204, 102)' && $('#pass-similar').css("color") == 'rgb(102, 204, 102)' && $('#pass-character').css("color") == 'rgb(102, 204, 102)' && $("#password-match").val() == $("#password-form").val() && $('#welcome-team').html() != 'Invalid team number...'){
                document.getElementById("submit").disabled = false;
                $('#submit').css({"background-image": "linear-gradient(90deg, #8A2387, #e94057,#F27121)", "-webkit-background-clip": "", "-webkit-text-fill-color": ""});
            }
            else{
                document.getElementById("submit").disabled = true;
                
                $('#submit').css({"background-image": "linear-gradient(90deg, grey, grey)", "-webkit-background-clip": "", "-webkit-text-fill-color": ""});
            }
        }, 30);
}); 

window.onload = async function changeRegName(){
    var teamNumber = $("#team_num_reg").val();
    $.get("https://www.thebluealliance.com/api/v3/team/frc" + teamNumber + "/simple", {"X-TBA-Auth-Key": "PzOW8s1DYGlVkgAsikwVlhy5wZ5Tm85fKSjd0DfiUJFQOGhsReyZEf88EEoAU1Cw"}, function(data){
        var jObject = (data);
        $("#welcome-team").html("Welcome to the" + " " + '"' + jObject['nickname'] + '"');
    }).fail(function(){
        $("#welcome-team").html("Invalid team number...");
    });
}