let keyState = {
    "x": 0,
    "y": 0
};

let keyAlreadyPressed = false;

let speed = 1;

let keyStatus = {
    ArrowUp: false,
    ArrowDown: false,
    ArrowLeft: false,
    ArrowRight: false
};

let socket = io();
socket.on('connect', function () {
    console.log("Starting connection");
});

document.addEventListener("keydown", function (event) {
    handleKeyEvent(event);
});

document.addEventListener("keyup", function (event) {
    handleKeyEvent(event);
});

function handleKeyEvent(event) {
    const isKeyDown = event.type === "keydown";
    const { key } = event;

    if (keyStatus[key] !== isKeyDown) {
        keyStatus[key] = isKeyDown;

        if (key === ",") {
            speed = parseFloat(Math.max(0, speed - 0.1).toFixed(3));
            if (keyStatus["ArrowUp"] && isKeyDown) {
                keyState["y"] = speed;
            } else if (keyStatus["ArrowDown"] && isKeyDown) {
                keyState["y"] = -speed;
            }
        } else if (key === ".") {
            speed = parseFloat(Math.min(1, speed + 0.1).toFixed(3));
            if (keyStatus["ArrowUp"] && isKeyDown) {
                keyState["y"] = speed;
            } else if (keyStatus["ArrowDown"] && isKeyDown) {
                keyState["y"] = -speed;
            }
        }

        switch (key) {
            case "ArrowUp":
            case "w":
                keyState["y"] = isKeyDown ? speed : 0;
                break;
            case "ArrowDown":
            case "s":
                keyState["y"] = isKeyDown ? -speed : 0;
                break;
            case "ArrowLeft":
            case "a":
                keyState["x"] = isKeyDown ? -1 : 0;
                break;
            case "ArrowRight":
            case "d":
                keyState["x"] = isKeyDown ? 1 : 0;
                break;
        }
        if (keyState["y"] == 0) {
            if (keyState["x"] > 0)
                keyState["x"] = speed;
            else if (keyState["x"] < 0)
                keyState["x"] = -speed;
        }     
        socket.emit("keyState", keyState);
        updateButtonStyle(key, isKeyDown);
    }
}

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
