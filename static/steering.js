const keyState = {
    "forward": 0,
    "backward": 0,
    "left": 0,
    "right": 0
};

let socket = io();
socket.on('connect', function(){
    console.log("Starting connection")
});

document.addEventListener("keydown", function(event) {
    if (event.key === "ArrowUp") {
        keyState["forward"] = 1;
    }
    if (event.key === "ArrowDown") {
        keyState["backward"] = 1;
    }
    if (event.key === "ArrowLeft") {
        keyState["left"] = 1;
    }
    if (event.key === "ArrowRight") {
        keyState["right"] = 1;
    }
    console.log(keyState);
    socket.emit("keyState", keyState)
});

document.addEventListener("keyup", function(event) {
    if (event.key === "ArrowUp") {
        keyState["forward"] = 0;
    }
    if (event.key === "ArrowDown") {
        keyState["backward"] = 0;
    }
    if (event.key === "ArrowLeft") {
        keyState["left"] = 0;
    }
    if (event.key === "ArrowRight") {
        keyState["right"] = 0;
    }
    console.log(keyState);
    socket.emit("keyState", keyState)
});
