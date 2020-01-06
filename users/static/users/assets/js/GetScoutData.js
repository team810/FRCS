
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
    $(document).ready(function () {
    $.get("https://www.thebluealliance.com/api/v3/event/2019" + key + "/matches", {"X-TBA-Auth-Key": "PzOW8s1DYGlVkgAsikwVlhy5wZ5Tm85fKSjd0DfiUJFQOGhsReyZEf88EEoAU1Cw"}, function(data) {    
    var matchNumber = document.getElementById("matchNumber").value;
    var match = document.getElementById('matchNumber').value;
    var jObject = (data);
    console.log(data);
    var data = jObject[match];
    var teamsB = data.alliances.blue.team_keys;
    var teamsR = data.alliances.red.team_keys;
    var MT = data.comp_level;
    var qm = "qm";
    var qf = "qf"
    var sf = "sf"
    var f = "f"
    if(MT == qm){
        document.getElementById("matchType").innerHTML = "Qualifing Match";
    }
    if(MT == qf){
        document.getElementById("matchType").innerHTML = "Quarter-Final";
    }
    if(MT == sf){
        document.getElementById("matchType").innerHTML = "Semi-Final";
    }
    if(MT == f){
        document.getElementById("matchType").innerHTML = "Final";
    }

    teamsB.forEach(function(name){
    var option = "<option  value='" + name + "'>" + name + "</option>";
    document.getElementById('teamNumber').innerHTML += option; 
        })

    teamsR.forEach(function(name){
    var option = "<option value='" + name + "'>" + name + "</option>"
    document.getElementById('teamNumber').innerHTML += option; 
        })
    });
});
}

//change name
async function changeName(){
    var value = $("#teamNumber option:selected").text();      
    $(document).ready(function () {
    $.get("https://www.thebluealliance.com/api/v3/team/" + value + "/simple",{"X-TBA-Auth-Key": "PzOW8s1DYGlVkgAsikwVlhy5wZ5Tm85fKSjd0DfiUJFQOGhsReyZEf88EEoAU1Cw"}, function(data) {
    var jObject = (data);
    var name = (jObject['nickname']);
    document.getElementById("teamName").innerHTML = name
    });
});
}
