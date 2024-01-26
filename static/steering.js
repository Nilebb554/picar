let keyState = {
    "x": 0,
    "y": 0
};

let keyAlreadyPressed = false;

let keyDown = {
    ArrowUp: false,
    ArrowDown: false,
    ArrowLeft: false,
    ArrowRight: false
};

let socket = io();
socket.on('connect', function(){
    console.log("Starting connection")
});

document.addEventListener("keydown", function(event) {
    if (!keyDown[event.key]) {
        keyDown[event.key] = true;
        if (event.key === "ArrowUp") {
            keyState["y"] = 1;
        }
        if (event.key === "ArrowDown") {
            keyState["y"] = -1;
        }
        if (event.key === "ArrowLeft") {
            keyState["x"] = -1;
        }
        if (event.key === "ArrowRight") {
            keyState["x"] = 1;
        }
        console.log(keyState);
        socket.emit("keyState", keyState);
    }
    updateButtonStyle(event.key, true);
});

document.addEventListener("keyup", function(event) {
    keyDown[event.key] = false;
    if (event.key === "ArrowUp") {
        keyState["y"] = -1;
    }
    if (event.key === "ArrowDown") {
        keyState["y"] = 1;
    }
    if (event.key === "ArrowLeft") {
        keyState["x"] = 1;
    }
    if (event.key === "ArrowRight") {
        keyState["x"] = -1;
    }
    console.log(keyState);
    socket.emit("keyState", keyState);

    updateButtonStyle(event.key, false);
});

function updateButtonStyle(key, isPressed) {
    let buttonId;
    switch (key) {
        case "ArrowUp":
            buttonId = "up";
            break;
        case "ArrowDown":
            buttonId = "down";
            break;
        case "ArrowLeft":
            buttonId = "left";
            break;
        case "ArrowRight":
            buttonId = "right";
            break;
    }

    if (buttonId) {
        const button = document.getElementById(buttonId);
        button.classList.toggle("active", isPressed);
    }
}
