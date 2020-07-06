window.onload = async function changeName(){
    $.get("https://www.thebluealliance.com/api/v3/team/frc" + {{user.team_num}} + "/simple", {"X-TBA-Auth-Key": "PzOW8s1DYGlVkgAsikwVlhy5wZ5Tm85fKSjd0DfiUJFQOGhsReyZEf88EEoAU1Cw"}, function(data){
        var jObject = (data);
        var name = jObject['nickname'];
        $("#team_welcome").html('"' + name + '"');
        })
    }