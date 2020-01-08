
//get team number and name
window.onload = async function getTeamNumber(){
        
	var team = prompt("Enter Team Number")
	$("#teamNumberHeader").html(team);
	$.get("https://www.thebluealliance.com/api/v3/team/frc" + team + "/events/2020/simple", {"X-TBA-Auth-Key": "PzOW8s1DYGlVkgAsikwVlhy5wZ5Tm85fKSjd0DfiUJFQOGhsReyZEf88EEoAU1Cw"}, function(data) {
	var jObject = (data);
    for(var i=0; i<data.length; i++){
    var obj = jObject[i];
    key = obj.event_code;
    var date = obj.start_date;
	console.log(date)
    console.log(key)
    }
})}

	if(team == null){
        $("#teamNumberHeader").html("Error");
        
	}
	

//Change teams in dropdown list


async function changeTeams(){
    var matchType = $( "#matchTypeOp option:selected" ).val();
    var matchNumber = document.getElementById("matchNumber").value;
    var matchId = "2019nyli2_";

    var qm = "qm"
    var qf = "qf";
    var sf = "sf";
    var f = "f";
    var ef = "ef";

    if(matchType === "qf"){
        var sel = '<input class="form-control" type="number" name="teamNumbert" id="teamNumber"/>';

        document.getElementById('teamNumberInput').innerHTML = sel;
    }
    if(matchType === "sf"){
        var sel = '<input class="form-control" type="number" name="teamNumbert" id="teamNumber"/>';

        document.getElementById('teamNumberInput').innerHTML = sel;
    }
    if(matchType === "f"){
        var sel = '<input class="form-control" type="number" name="teamNumbert" id="teamNumber"/>';

        document.getElementById('teamNumberInput').innerHTML = sel;
    }if(matchType === "ef"){
        var sel = '<input class="form-control" type="number" name="teamNumbert" id="teamNumber"/>';

        document.getElementById('teamNumberInput').innerHTML = sel;
    }
    else if(matchType === "qm"){
        document.getElementById('teamNumberInput').innerHTML = "";

    }
    

    console.log(matchType)
    $(document).ready(function () {
    document.getElementById('teamNumber').innerHTML = "";
    $.get("https://www.thebluealliance.com/api/v3/match/" + matchId + matchType + matchNumber + "/simple", {"X-TBA-Auth-Key": "PzOW8s1DYGlVkgAsikwVlhy5wZ5Tm85fKSjd0DfiUJFQOGhsReyZEf88EEoAU1Cw"}, function(data) {    
    var jObject = (data);
    console.log(data);
    var alliance = jObject.alliances;
    console.log(alliance)
    var blue = alliance.blue.team_keys;
    var red = alliance.red.team_keys;
    

    blue.forEach(function(name){
    var option = "<option isd='teamNumber' value='" + name + "'>" + name + "</option>";
    document.getElementById('teamNumber').innerHTML += option; 
        })

    red.forEach(function(name){
    var option = "<option value='" + name + "'>" + name + "</option>"
    document.getElementById('teamNumber').innerHTML += option; 
        })
    });
});
}

//change name
async function changeName(){
    var teamOp = $("#teamNumber option:selected").text();  
    $(document).ready(function () {
    $.get("https://www.thebluealliance.com/api/v3/team/" + teamOp + "/simple",{"X-TBA-Auth-Key": "PzOW8s1DYGlVkgAsikwVlhy5wZ5Tm85fKSjd0DfiUJFQOGhsReyZEf88EEoAU1Cw"}, function(data) {
    var jObject = (data);
    console.log(data)
    var name = (jObject['nickname']);
    document.getElementById("teamName").innerHTML = name;
    });
});
}
