
//get team number and name
window.onload = async function getTeamNumber(){
        
	var team = prompt("Enter Team Number")
	$("#teamNumberHeader").html(team);
	$.get("https://www.thebluealliance.com/api/v3/team/frc" + team + "/events/2020/simple", {"X-TBA-Auth-Key": "PzOW8s1DYGlVkgAsikwVlhy5wZ5Tm85fKSjd0DfiUJFQOGhsReyZEf88EEoAU1Cw"}, function(data) {
    var jObject = (data);
    console.log(data);
    for(var i=0; i<data.length; i++){
        
    var obj = jObject[i];
    var comp = obj.name;

    key = obj.event_code;
    var date = obj.start_date;
    console.log(date)
    console.log(key)
    var option = "<option id='compValueDrop' value=" + key + ">" + comp + "</option>"
    document.getElementById('getCompDrop').innerHTML += option;
    
    }
})}
	

//Change teams in dropdown list
async function changeTeams(){
    var matchType = $("#matchTypeOp option:selected").val();
    var matchNumber = document.getElementById("matchNumber").value;


    

    

    console.log(matchType)
    $(document).ready(function () {
    document.getElementById('teamNumber').innerHTML = "";
    document.getElementById('teamNumber').innerHTML += "<option>Select Team</option>";
    document.getElementById('teamNumber').innerHTML += "<option value='manual'>Manually Insert Team</option>";
    $.get("https://www.thebluealliance.com/api/v3/match/2019" + matchTypeOp + "_" + matchType + matchNumber + "/simple", {"X-TBA-Auth-Key": "PzOW8s1DYGlVkgAsikwVlhy5wZ5Tm85fKSjd0DfiUJFQOGhsReyZEf88EEoAU1Cw"}, function(data) {    
    var jObject = (data);
    console.log(data);
    var alliance = jObject.alliances;
    console.log(alliance)
    var blue = alliance.blue.team_keys;
    var red = alliance.red.team_keys;
    
    
    
    
    
    blue.forEach(function(name){
    var newstr = JSON.stringify(name)
    var blueStr = newstr.slice(4, -1);
    var option = "<option id='blue' value='"  + name  + "'>" + "Team " + blueStr + " Blue Alliance" + "</option>"
    document.getElementById('teamNumber').innerHTML += option; 


        })

    red.forEach(function(name){
    var newstr = JSON.stringify(name)
    var redStr = newstr.slice(4, -1);
    var option = "<option id='red' value='"  + name  + "'>" + "Team " + redStr + " Red Alliance" + "</option>"
    document.getElementById('teamNumber').innerHTML += option;

        })
    });
});
}

//change name
async function changeName(){
    var teamOp = $("#teamNumber option:selected").val();
    console.log(teamOp)
    if(teamOp = "manual"){
        document.getElementById("failsafe").innerHTML = '<input placeholder="Team Number"z class="form-control" type="number" name="teamNumbert" id="teamNumber"/>';
    }
    $(document).ready(function () {
    $.get("https://www.thebluealliance.com/api/v3/team/" + teamOp + "/simple",{"X-TBA-Auth-Key": "PzOW8s1DYGlVkgAsikwVlhy5wZ5Tm85fKSjd0DfiUJFQOGhsReyZEf88EEoAU1Cw"}, function(data) {
    var jObject = (data);
    console.log(jObject)
    var name = (jObject['nickname']);
    document.getElementById("teamName").innerHTML = name + " ";

    
    
    });
});
}


function getCompData(){
 matchTypeOp = $("#getCompDrop option:selected").val();
 console.log(matchTypeOp);
}

