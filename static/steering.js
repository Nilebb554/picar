const keyState = {
    "forward": 0,
    "backward": 0,
    "left": 0,
    "right": 0
};

let keyAlreadyPressed = false;

document.addEventListener("keydown", function(event) {
    if (keyAlreadyPressed) return;
    keyAlreadyPressed = true;

    if (event.key === "ArrowUp") {
        keyState["forward"] = 1;
    } else if (event.key === "ArrowDown") {
        keyState["backward"] = 1;
    } else if (event.key === "ArrowLeft") {
        keyState["left"] = 1;
    } else if (event.key === "ArrowRight") {
        keyState["right"] = 1;
    }

    console.log(keyState);
});

document.addEventListener("keyup", function(event) {
    keyAlreadyPressed = false;

    if (event.key === "ArrowUp") {
        keyState["forward"] = 0;
    } else if (event.key === "ArrowDown") {
        keyState["backward"] = 0;
    } else if (event.key === "ArrowLeft") {
        keyState["left"] = 0;
    } else if (event.key === "ArrowRight") {
        keyState["right"] = 0;
    }

    console.log(keyState);
});
