let mediaRecorder;
let audioChunks = [];

function startRecording() {
    const stream = navigator.mediaDevices.getUserMedia({ audio: true });
    console.log("Started Recording")

    stream.then(function (mediaStream) {
        mediaRecorder = new MediaRecorder(mediaStream);
        mediaRecorder.ondataavailable = function (e) {
            audioChunks.push(e.data);
        };

        mediaRecorder.onstop = function () {
            const audioBlob = new Blob(audioChunks, { 'type': 'audio/wav' });
            const audioUrl = URL.createObjectURL(audioBlob);
            const audio = document.getElementById("audio");
            audio.src = audioUrl;

            // If you want to send the audioBlob to your server, you can do it here.
            // Example:
            // uploadAudioToServer(audioBlob);
        };

        mediaRecorder.start();

        // Stop recording after 5 seconds (or adjust as needed)
        setTimeout(function () {
            mediaRecorder.stop();
        }, 5000);
    }).catch(function (err) {
        console.error("Error accessing the microphone:", err);
    });
}

// Optional: Upload recorded audio to server
// function uploadAudioToServer(blob) {
//     const formData = new FormData();
//     formData.append('audio', blob, 'audio.wav');

//     fetch('/upload_endpoint/', {
//         method: 'POST',
//         body: formData
//     }).then(response => {
//         if (response.ok) {
//             console.log("Audio uploaded!");
//         }
//     });
// }
