// document.addEventListener('DOMContentLoaded', function () {
//     var feedbackForm = document.getElementById('feedbackForm');

//     feedbackForm.addEventListener('submit', function (e) {
//         e.preventDefault(); // Prevent the default form submission
        
//         var accuracy = document.getElementById('accuracy').value;
//         var errorsYes = document.getElementById('yes').checked;
//         var errorsNo = document.getElementById('no').checked;

//         if (!accuracy) {
//             alert('Please select the accuracy level.');
//             return;
//         }

//         if (!errorsYes && !errorsNo) {
//             alert('Please indicate if there were any grammatical errors.');
//             return;
//         }

//         alert('Form submitted successfully!');
//     });
// });


function changeStyle() {
    var caption = document.getElementById("captionGenerated");
    var fontSize = document.getElementById("fontSizeInput").value;
    var color = document.getElementById("colorInput").value;

    if (fontSize) {
        fontSize = parseInt(fontSize);

        if (!isNaN(fontSize) && fontSize > 0 && fontSize < 100) {
            caption.style.fontSize = fontSize + 'px';
        }
    }

    caption.style.color = color;
}

