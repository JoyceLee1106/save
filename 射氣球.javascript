setBackdrop('bg.jpg');
var balloons = [];
var clock = 0;
var score = 0;
var status = 'start';
var target = createSprite('target.png');
forever(function() {
    createBallons();
    move();
    checkClicked();
    target.x = cursor.x;
    target.y = cursor.y;
    target.direction+=1
})
// 造型幫你寫好囉，直接複製吧！
//
function createBallons() {
    if (clock%30 === 0 && status != 'stop') {
        var balloon = createSprite(['0.png', 'a_1.png', 'a_5.png', 'a_10.png', 'a_50.png', 'a_100.png', 'm_2.png', 'e_2.png']);
        balloon.costumeId = Math.floor(Math.random()*8);
        balloon.y = 500;
        balloon.x = Math.random()*640;
        balloons.push(balloon);
    }
    clock += 1;
}
function move() {
    for (var i = 0; i < balloons.length; i += 1) {
        balloons[i].y -= 3;
    }
}
function checkClicked() {
    for (var i = 0; i < balloons.length; i += 1) {
        if (cursor.isDown && balloons[i].touched(cursor)) {
            balloons[i].destroy();
            if (balloons[i].costumeId === 0) {
                score = 0;
            } else if (balloons[i].costumeId == 1) {
                score += 1;
            } else if (balloons[i].costumeId == 2) {
                score += 5;
            } else if (balloons[i].costumeId == 3) {
                score += 10;
            } else if (balloons[i].costumeId == 4) {
                score += 50;
            } else if (balloons[i].costumeId == 5) {
                score += 100;
            } else if (balloons[i].costumeId == 6) {
                score = score*2;
            } else if (balloons[i].costumeId == 7) {
                score = score/2
            }
        }
    }
    print(score, 10, 10, "red", 20);
}
setTimeout(function() {
    status = 'stop';
}, 30000);
