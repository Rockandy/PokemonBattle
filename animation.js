var vid = document.getElementById("background_audio");
vid.volume = 0.2;
var sun = new Image();
var moon = new Image();
var earth = new Image();
var star = new Image();
var x = 0;
var y = 0;
var xy = 0;
var yx = 0;
var i = 0;

function init(){
  sun.src = 'http://i.imgur.com/nXz8W96.png';
  moon.src = 'http://cdn.bulbagarden.net/upload/9/93/Bag_Pok%C3%A9_Ball_Sprite.png';
  earth.src = 'http://cdn.bulbagarden.net/upload/2/2c/Spr_b_4d_026_m.png';
  star.src = 'http://cdn.bulbagarden.net/upload/4/41/Spr_4p_398_m.png';
  window.requestAnimationFrame(draw);
}

function doMouseDown(event) {
  if (x == 0 && y == 0) {
    x = event.pageX;
    y = event.pageY;
  }
  else if (y > 351 && x > 274 && x < 655 && y < 472 && yPos > 200) {
    xy = event.pageX;
    yx = event.pageY;
    x = 0;
    y = 0;
  }
  else if (xy != 0 && yx != 0) {
    x = event.pageX;
    y = event.pageY;
    xy = 0;
    yx = 0;
  }
}

function myFunction() {
  if (i == 0) {
    vid.muted = true;
    i++;
  }
  else if (i == 1) {
    vid.muted = false;
    i--;
  }
}

var xPos = 0;
var yPos = 142;
var oY = 200;
var oX = 60;
var ooY = 200;
var THP = 110;
var HP = 110;
var HP2 = 110;

function draw() {
  var canvas = document.getElementById("canvas");
  var ctx = canvas.getContext("2d");
  ctx.globalCompositeOperation = 'destination-over';
  canvas.addEventListener("mousedown", doMouseDown, false);
  ctx.clearRect(0,0,400,400);

  ctx.save();
  window.addEventListener('mousemove', draw, false);
  if (HP > 110) {HP = 110}
  if (HP2 > 110) {HP2 = 110}
  if (yPos < 200) {ctx.drawImage (moon, xPos, yPos);}
  if (xPos < 50) {xPos += 4; yPos -= 6;}
  if (xPos >= 50 && yPos < 200) {xPos+=2; yPos+=6;}
  ctx.beginPath();
  if (yPos > 200 && oY > 125) {ctx.arc(xPos + 25, oY + 50, 10, 0, 2*Math.PI); xPos+=4; oY-=4;}
  ctx.fill();
  ctx.beginPath();
  if (yPos > 200 && oY > 125) {ctx.arc(oX - 25, ooY + 50, 10, 0, 2*Math.PI); oX-=4; ooY-=4;}
  ctx.fill();
  ctx.fillStyle = "rgba(255, 255, 255, 0.0)";
  if (yPos > 200) {ctx.drawImage(earth, 25, 146, 125, 125);}
  if (HP >= 55) {ctx.fillStyle = "lime";}
  if (HP < 55) {ctx.fillStyle = "yellow";}
  ctx.fillRect (45, 70, HP, 10);
  if (HP2 >= 55) {ctx.fillStyle = "lime";}
  if (HP2 < 55) {ctx.fillStyle = "yellow";}
  if (yPos > 200) {ctx.fillRect (236, 187, HP2, 10);}
  ctx.restore();

  ctx.fillStyle = "black";
  ctx.font = "10px serif";
  if (yPos > 200) {ctx.fillText("HP :", 215, 195);
  ctx.font= "20px serif";
  ctx.fillText("Raichu", 215, 185)
  ctx.font= "10px serif";
  ctx.fillText(HP + '/' + THP, 300, 185)
  ctx.fillStyle= "rgb(0, 230, 230)";
  ctx.fillRect (240, 205, 110, 5);
  }
  ctx.fillStyle= "black";
  ctx.font = "10px serif";
  ctx.fillText("HP :", 24, 78);
  ctx.font= "20px serif";
  ctx.fillText("Staraptor", 24, 68)
  ctx.strokeRect (10,270, 190, 60);
  ctx.fillStyle = "red";
  ctx.fillRect (10,270, 190, 60);
  ctx.fillStyle = "orange";
  ctx.fillRect (10,270, 190, 60);
  ctx.fillStyle = "rgba(255, 255, 255, 0.0)";
  ctx.drawImage (star, 220, 5, 155, 155);
  ctx.fillStyle = "rgb(212, 212, 212)";
  ctx.fillRect
  ctx.strokeRect (19, 38, 144, 54);
  if (yPos > 200) {ctx.strokeRect (210, 155, 144, 54);}
  ctx.fillRect (19, 38, 144, 54);
  if (yPos > 200) {ctx.fillRect (210, 155, 144, 54);}
  ctx.drawImage (sun, -1, 1);
  ctx.fillStyle = "rgb(108, 205, 235)";
  if (y > 351 && x > 274 && x < 655 && y < 472 && yPos > 200) {
  ctx.fillStyle = "rgb(255, 0, 0)";
  }
  ctx.fillRect (10, 270, 380, 120);
  ctx.fillStyle = "rgb(214, 55, 87)";
  ctx.fillRect (0, 260, 400, 140);
  ctx.fillStyle = "rgb(250, 255, 92)";

  window.requestAnimationFrame(draw);
}

init();
