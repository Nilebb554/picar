let keyState = {
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
        keyState["x"] = 1;
    }
    else if (event.key === "ArrowLeft" || event.key === "a" || event.key === "A") {
        keyState["x"] = -1;
    }
    else if (event.key === "ArrowUp" || event.key === "w" || event.key === "W") {
        keyState["y"] = speed;
    }
    else if (event.key === "ArrowDown" || event.key === "s" || event.key === "S") {
        keyState["y"] = -speed;
    }
    else if (event.key === ",") {
        speed -= 0.1;
        speed = Math.max(0.0001, Math.min(speed, 1));
        console.log("Speed:", speed);
        if (keyState["y"] > 0) {
            keyState["y"] = speed;
        } else if (keyState["y"] < 0) {
            keyState["y"] = -speed
        }
    }
    else if (event.key === ".") {
        speed += 0.1;
        speed = Math.max(0.0001, Math.min(speed, 1));
        console.log("Speed:", speed);
        if (keyState["y"] > 0) {
            keyState["y"] = speed;
        } else if (keyState["y"] < 0) {
            keyState["y"] = -speed
        }
    }
});

document.addEventListener("keyup", function (event) {
    if ((event.key === "ArrowRight" || event.key === "d" || event.key === "D" || event.key === "ArrowLeft" || event.key === "a" || event.key === "A")) {
        keyState["x"] = 0;
    }
    if ((event.key === "ArrowUp" || event.key === "w" || event.key === "W" || event.key === "ArrowDown" || event.key === "s" || event.key === "S")) {
        keyState["y"] = 0;
    }
});

function update() {
    if (keyState["x"] !== 0 && keyState["y"] === 0) {
        if (keyState["x"] > 0) {
            socket.emit("keyState", {
                "x": -speed,
                "y": 0
            });
        } else if (keyState["x"] < 0) {
            socket.emit("keyState", {
                "x": -speed,
                "y": 0
            });
        }
    } else {
        socket.emit("keyState", keyState);
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
