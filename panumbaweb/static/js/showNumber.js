var display

$(document).ready(function() {

   console.log("ready!");
   
  display = new SegmentDisplay("display");
  display.pattern         = "##########";
  display.displayAngle    = 0;
  display.digitHeight     = 60;
  display.digitWidth      = 30;
  display.digitDistance   = 5;
  display.segmentWidth    = 4;
  display.segmentDistance = 0.6;
  display.segmentCount    = 7;
  display.cornerType      = 3;
  display.colorOn         = "#0f0";
  display.colorOff        = "black";
  display.draw();

   
  setInterval(fetchLatestAnswer, 3000);

  fetchLatestAnswer();

});
let lastAnswer = null;
let sameAnswerCount = 0;

function fetchLatestAnswer() {
    $.ajax({
        url: url,
        success: function(data) {
            const formattedAnswer = formatResponseForDisplay(data.answer);

            // Check if the new answer is the same as the last one
            if (data.answer === lastAnswer) {
                sameAnswerCount++;
            } else {
                sameAnswerCount = 0;
            }

            // If the same answer has been fetched 5 times, send a different request
            if (sameAnswerCount === 3) {
                $.ajax({
                    url: anotherUrl,  // Replace with your other URL
                    success: function(data) {
                        console.log("fetched another answer", data.bicycle_count);
                       const formattedAnswer = formatResponseForDisplay(data.bicycle_count);
                        display.setValue(formattedAnswer);
                    }
                });
            }

            lastAnswer = data.answer;

            display.setValue(formattedAnswer);  
            console.log("latest answer fetched", data.answer);
        }
    });
}
/* function fetchLatestAnswer() {
        $.ajax({
            url: url,
            success: function(data) {
                const formattedAnswer = formatResponseForDisplay(data.answer);

                display.setValue(formattedAnswer);  
                console.log("latest answer fetched", data.answer);
            }
        });
    }
 */

function formatResponseForDisplay(data) {
    let formattedString = String(data);

    // Truncate if longer than 10 characters
    if (formattedString.length > 10) {
        formattedString = formattedString.substring(0, 10);
    }
    // Pad with leading spaces if shorter than 10 characters
    else if (formattedString.length < 10) {
        const padding = 10 - formattedString.length;
        formattedString = ' '.repeat(padding) + formattedString;
    }

    return formattedString;
}