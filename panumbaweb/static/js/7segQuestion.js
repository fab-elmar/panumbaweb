var display

$(document).ready(function() {

   
   
  display = new SegmentDisplay("display");
  display.pattern         = "###########";
  display.displayAngle    = 0;
  display.digitHeight     = 60;
  display.digitWidth      = 30;
  display.digitDistance   = 5;
  display.segmentWidth    = 4;
  display.segmentDistance = 0.6;
  display.segmentCount    = 7;
  display.cornerType      = 3;
  display.colorOn         = getRandomColor() ;
  display.colorOff        = "black";
  display.draw();

   
  display.setValue(formatResponseForDisplay(numba));

});


function formatResponseForDisplay(data) {
    let formattedString = String(data);

    // Truncate if longer than 1 characters
    if (formattedString.length > 11) {
        formattedString = formattedString.substring(0, 10);
    }
    // Pad with leading spaces if shorter than 11 characters
    else if (formattedString.length < 11) {
        const padding = 11 - formattedString.length;
        formattedString = ' '.repeat(padding) + formattedString;
    }

    return formattedString;
}


function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

