const keyState = {
    "forward": 0,
    "backward": 0,
    "left": 0,
    "right": 0
};

document.addEventListener("keydown", function(event) {
    if (event.key === forwardArrow) {
        keyState["forward"] = 1;
    }
    if (event.key === backwardArrow) {
        keyState["backward"] = 1;
    }
    if (event.key === leftArrow) {
        keyState["left"] = 1;
    }
    if (event.key === rightArrow) {
        keyState["right"] = 1;
    }
    console.log(keyState);
});

document.addEventListener("keyup", function(event) {
    if (event.key === forwardArrow) {
        keyState["forward"] = 0;
    }
    if (event.key === backwardArrow) {
        keyState["backward"] = 0;
    }
    if (event.key === leftArrow) {
        keyState["left"] = 0;
    }
    if (event.key === rightArrow) {
        keyState["right"] = 0;
    }
});


