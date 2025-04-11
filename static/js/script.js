const video = document.getElementById("video");
const responseBox = document.getElementById("response");
const questionInput = document.getElementById("question");
const askBtn = document.getElementById("askBtn");

// Get webcam stream
navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        video.srcObject = stream;
    })
    .catch(err => {
        alert("Camera access denied: " + err.message);
    });

function captureFrame() {
    const canvas = document.createElement("canvas");
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    const ctx = canvas.getContext("2d");
    ctx.drawImage(video, 0, 0);
    return canvas.toDataURL("image/jpeg").split(",")[1]; // base64 without prefix
}

askBtn.addEventListener("click", async () => {
    const frame = captureFrame();
    const question = questionInput.value;

    const payload = {
        frame: frame,
        question: question
    };

    try {
        const res = await fetch("/api/learn/adaptive-answer", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });

        const data = await res.json();
        responseBox.innerHTML = `
            <strong>Detected Emotion:</strong> ${data.emotion}<br>
            <strong>Comprehension Score:</strong> ${data.comprehension_score}<br><br>
            <strong>AI Response:</strong><br>${data.response}
        `;
    } catch (err) {
        responseBox.innerHTML = "An error occurred. Please try again.";
        console.error(err);
    }
});
