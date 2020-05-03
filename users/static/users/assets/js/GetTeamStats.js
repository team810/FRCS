window.onload = async function changeState(){
    $(".page-wrapper").removeClass("toggled");

      $.get("https://www.thebluealliance.com/api/v3/team/frc" + team_num + "/simple", {"X-TBA-Auth-Key": "PzOW8s1DYGlVkgAsikwVlhy5wZ5Tm85fKSjd0DfiUJFQOGhsReyZEf88EEoAU1Cw"}, function(data){
          var jObject = (data);
          $("#city").html(jObject['city']);
          console.log(jObject)
      })
      $.get("https://www.thebluealliance.com/api/v3/team/frc" + team_num + "/simple", {"X-TBA-Auth-Key": "PzOW8s1DYGlVkgAsikwVlhy5wZ5Tm85fKSjd0DfiUJFQOGhsReyZEf88EEoAU1Cw"}, function(data){
          var jObject = (data);
          $("#country").html(jObject['country']);
      })
      $.get("https://www.thebluealliance.com/api/v3/team/frc" + team_num + "/simple", {"X-TBA-Auth-Key": "PzOW8s1DYGlVkgAsikwVlhy5wZ5Tm85fKSjd0DfiUJFQOGhsReyZEf88EEoAU1Cw"}, function(data){
          var jObject = (data);
          $("#nickname").html(jObject['nickname']);
      })
      $.get("https://www.thebluealliance.com/api/v3/team/frc" + team_num + "/simple", {"X-TBA-Auth-Key": "PzOW8s1DYGlVkgAsikwVlhy5wZ5Tm85fKSjd0DfiUJFQOGhsReyZEf88EEoAU1Cw"}, function(data){
          var jObject = (data);
          $("#state").html(jObject['state_prov']);
      })
      $.get("https://www.thebluealliance.com/api/v3/team/frc" + team_num + "/simple", {"X-TBA-Auth-Key": "PzOW8s1DYGlVkgAsikwVlhy5wZ5Tm85fKSjd0DfiUJFQOGhsReyZEf88EEoAU1Cw"}, function(data){
          var jObject = (data);
          $("#num").html(jObject['team_number']);
          
      })
      $.get("https://www.thebluealliance.com/api/v3/team/frc" + team_num + "/events/2020", {"X-TBA-Auth-Key": "PzOW8s1DYGlVkgAsikwVlhy5wZ5Tm85fKSjd0DfiUJFQOGhsReyZEf88EEoAU1Cw"}, function(data){
          var jObject = (data);
          for(i = 0; i<5; i++){
          events = jObject[i]['name']
          $('#events').append('<p>' +  events.replace("***SUSPENDED***", " ") + "</p>")
          }    
          }      
  )}