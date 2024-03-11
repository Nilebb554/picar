let steeringState = {
    "x": 0,
    "y": 0
};

let speed = 1;

let socket = io();
socket.on('connect', function () {
    console.log("Starting connection");
});

//steering change

document.addEventListener("keydown", function (event) {
    if (event.key === "ArrowRight" || event.key === "d" || event.key === "D") {
        steeringState["x"] = 1;
    }
    else if (event.key === "ArrowLeft" || event.key === "a" || event.key === "A") {
        steeringState["x"] = -1;
    }
    else if (event.key === "ArrowUp" || event.key === "w" || event.key === "W") {
        steeringState["y"] = speed;
    }
    else if (event.key === "ArrowDown" || event.key === "s" || event.key === "S") {
        steeringState["y"] = -speed;
    }
    else if (event.key === ",") {
        speed -= 0.1;
        speed = Math.max(0.0001, Math.min(speed, 1));
        console.log("Speed:", speed);
        if (steeringState["y"] > 0) {
            steeringState["y"] = speed;
        } else if (steeringState["y"] < 0) {
            steeringState["y"] = -speed
        }
    }
    else if (event.key === ".") {
        speed += 0.1;
        speed = Math.max(0.0001, Math.min(speed, 1));
        console.log("Speed:", speed);
        if (steeringState["y"] > 0) {
            steeringState["y"] = speed;
        } else if (steeringState["y"] < 0) {
            steeringState["y"] = -speed
        }
    }
});

document.addEventListener("keyup", function (event) {
    if ((event.key === "ArrowRight" || event.key === "d" || event.key === "D" || event.key === "ArrowLeft" || event.key === "a" || event.key === "A")) {
        steeringState["x"] = 0;
    }
    if ((event.key === "ArrowUp" || event.key === "w" || event.key === "W" || event.key === "ArrowDown" || event.key === "s" || event.key === "S")) {
        steeringState["y"] = 0;
    }
});

//Gamepad

function gamepadState() {
    const gamepads = navigator.getGamepads();
    for (let i = 0; i < gamepads.length; i++) {
        const gamepad = gamepads[i];
        if (gamepad) {
            const leftJoystickX = gamepad.axes[0];
            const triggerY = gamepad.buttons[7].value - gamepad.buttons[6].value;

            steeringState.x = leftJoystickX;
            steeringState.y = triggerY;
        }
    }
}

//Update
function update() {
    const gamepads = navigator.getGamepads();
    if (gamepads.length > 0) {
        gamepadState();
        socket.emit("steeringData", steeringState);
        console.log("Gamepad", steeringState);
    } else if (steeringState["y"] === 0) {
        const x = steeringState["x"];
        if (x !== 0) {
            socket.emit("steeringData", {
                "x": speed * Math.sign(x),
                "y": 0
            });
            console.log("y = 0 speed sent on x", speed * Math.sign(x))
        } else {
            socket.emit("steeringData", steeringState);
            console.log("Other");
        }
    } else {
        socket.emit("steeringData", steeringState);
        console.log("Other");
    }
}

setInterval(update, 1000 / 180);


//Color change up down right left

document.addEventListener("keydown", function (event) {
    if (event.key === "ArrowUp" || event.key === "w" || event.key === "W") {
        document.getElementById("up").classList.add("active");
    }
    else if (event.key === "ArrowDown" || event.key === "s" || event.key === "S") {
        document.getElementById("down").classList.add("active");
    }
    else if (event.key === "ArrowLeft" || event.key === "a" || event.key === "A") {
        document.getElementById("left").classList.add("active");
    }
    else if (event.key === "ArrowRight" || event.key === "d" || event.key === "D") {
        document.getElementById("right").classList.add("active");
    }
});

document.addEventListener("keyup", function (event) {
    if (event.key === "ArrowUp" || event.key === "w" || event.key === "W") {
        document.getElementById("up").classList.remove("active");
    }
    else if (event.key === "ArrowDown" || event.key === "s" || event.key === "S") {
        document.getElementById("down").classList.remove("active");
    }
    else if (event.key === "ArrowLeft" || event.key === "a" || event.key === "A") {
        document.getElementById("left").classList.remove("active");
    }
    else if (event.key === "ArrowRight" || event.key === "d" || event.key === "D") {
        document.getElementById("right").classList.remove("active");
    }
});
