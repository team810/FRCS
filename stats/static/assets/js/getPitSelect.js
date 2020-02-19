function getTankOp(){
    var tank = $("#DTT option:selected").html();

    var op = '<p id="label">Tank Type</p><select onchange="getTankOp2()" name="TT" id="TT" class="custom-select"><option id="tank" value="6Wheel:6Wheel,8Wheel,TankTread,Other">6 Wheel</option><option value="8Wheel:6Wheel,8Wheel,TankTread,Other">8 Wheel</option><option value="TankTread:6Wheel,8Wheel,TankTread,Other">Tank Treads</option><option value="Other:6Wheel,8Wheel,TankTread,Other">Other</option></select>'

    if(tank === "Tank"){
        document.getElementById('tank1').innerHTML = op;
    }
    else{
        document.getElementById('tank1').innerHTML = "";
    }
    

}

function getTankOp2(){
    var tank1 = $("#TT option:selected").html();

    var op2 = '<p id="label">Tread Type</p><select name="weight" id="weight" class="custom-select"><option id="tank" value="Rhino:Rhino,Raptor,Other">Rhino</option><option value="Raptor:Rhino,Raptor,Other">Raptor</option><option value="Other:Rhino,Raptor,Other">Other</option></select>'

    if(tank1 === "Tank Treads"){
        document.getElementById('tank2').innerHTML = op2;
    }
    else{
        document.getElementById('tank2').innerHTML = "";
    }
}