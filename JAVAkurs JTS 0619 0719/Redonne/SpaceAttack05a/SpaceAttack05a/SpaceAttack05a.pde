color white  = color(255, 255, 255);
color black  = color(0, 0, 0);
color green  = color(0, 200, 0);
color yellow = color(200, 200, 0);
color red    = color(200, 0, 0);
color purple = color(200, 0, 200);

color screenC = black;
color playerC = green;
color bulletC = green;
color textC = green;
color targetC = green;

PImage bg;
PImage hard;

int playerSize = 50;

int sizeX = 500;
int sizeY = 500;

int playerX = sizeX / 2;
int playerY = sizeY - 10 - playerSize;
int playerSpeed = 7;

int bulletX = 0;
int bulletY = 0;
int bulletSpeed = 20;

int targetX = 0;
int targetY = 0;
int targetSpeed = 6;
int targetActive = 0;
int targetSize = playerSize;

int score = 0;
int life = 0;

int playerDirection = 0; // direction: -1 left, 0 stop, 1 right
int playerFire = 0;      // 0 stop, 1 active

int titleAni = 1;
int ideeAni  = 1;
int ichAni   = 1;
int pressAni = 1;
int kursAni  = 1; 
int playAni  = 1;
int letsAni  = 1;
int gameAni  = 1;
int overAni  = 1;
int javaAni  = 1;

int gameMode = 1; // 0 = game over, 1 = intro, 2 - init game, 3 = in game, 4 = pause, 5 = end game, 6 = enter highscore, 7 = finalize, 8-9 = not used 

void setup()
{
  size(500, 500);
  textSize(36);
  bg    = loadImage("bg.png");
  hard = loadImage("hard.png");
}

void draw()
{
  background(screenC); // erase screen


  switch (gameMode)
  {
    case 1: // intro
      // put the paddles back to start
      playerX = sizeX / 2;
      playerY = sizeY - 10 - playerSize;

      fill(green);
      textSize(titleAni);
      textAlign(CENTER);
      text("Space Attack", 250, 240);

      textAlign(CENTER);
      fill(green);
      textSize(ichAni);
      text("Magnus Küderli Dez2019 Javakurs", 250, 280);
      
      textAlign(LEFT);
      fill(green);
      textSize(ideeAni);
      text("Nach einer Idee von Andreas Bucher", 85, 170);
      
      textAlign(CENTER);
      fill(green);
      textSize(pressAni);
      text("Press S to start", 250, 310);
      
      textAlign(CENTER);
      fill(green);
      textSize(javaAni);
      text("VHS JAVA Kurs 2019", 250, 140);
      
      fill(green);
      textSize(gameAni);
      textAlign(CENTER);
      text("Game", 250, 350);
      
      fill(green);
      textSize(playAni);
      textAlign(CENTER);
      text("Play it", 250, 115);
      
      fill(green);
      textSize(letsAni);
      textAlign(CENTER);
      text("Let's", 250, 85);
      
      textSize(overAni);
      text("Over", 250, 385);
      
      textSize(javaAni);
      text("Java", 250, 410);
      textAlign(LEFT);
      if (titleAni <= 76) {
      titleAni += 3;
      }
      if (ideeAni <= 20) {
      ideeAni ++;
      }
      if (ichAni <= 20) {
      ichAni ++;
      }
      if (pressAni <= 26) {
      pressAni ++;
      }
      if (kursAni <= 26) {
      kursAni ++;
      }
      if (playAni <= 31) {
      playAni ++;
      }
      if (letsAni <= 24) {
      letsAni ++;
      }
      if (gameAni <= 35) {
      gameAni ++;
      }
      if (overAni <= 24) {
      overAni ++;
      }
      if (javaAni <= 17) {
      javaAni ++;
      }

    break;  

    case 2: //init
      score = 0;
      life = 6;
      gameMode = 3;  // switch to inGame mode
    break;  

    case 3: // inGame - we do all active gaming stuff here
    
      imageMode(CENTER);
      image(bg, 250, 250, 600, 500);
    
      if (playerDirection == -1) // left
      {
        if (playerX > (0 + playerSize) )
        {
          playerX = playerX - playerSpeed;
        }
      }
    
      if (playerDirection == 1) // down
      {
        if (playerX + playerSize < sizeY)
        {
          playerX = playerX + playerSpeed;
        }
      }
      
      if (targetActive == 0)
      {
        targetActive = 1;
        targetX = int(random(25, sizeX - 25));
        targetY = 0;
      }
      
      else
        {

            targetY = targetY + targetSpeed;

            if (targetY >= sizeY) 
              {
                targetActive = 0;
                life --;
              }
              
            if ( ( (targetX >= playerX - playerSize+2) && ( targetX <= playerX + playerSize - 2)) && (targetY >= playerY) )
              {
                targetActive = 0;
                playerFire = 0;
                life --;
              }
              
        }
        
        if (life <= 0)
          {
            gameMode = 1;
          }
         
        bulletY = bulletY - bulletSpeed;
  
      if (bulletY <= 0)
        {
          playerFire = 0;
        }
        
        if ( ( (targetX >= bulletX - playerSize+2) && (targetX <= bulletX + playerSize-2)) && (targetY >= bulletY) && targetActive == 1)
        {
          playerFire = 0;
          targetActive = 0;
          score ++;

        }
      
    break;  

    case 4: //pause
      text("P A U S E", sizeX/2 - 80, sizeY/2 - 18);
    break;  

  }

  // show the objects on screen
  stroke(playerC);
  fill(playerC);
// show the player

if (gameMode == 3)  {
  line(playerX, playerY, playerX + playerSize/2, playerY + playerSize); 
  line(playerX, playerY, playerX - playerSize/2, playerY + playerSize); 
  line(playerX - playerSize/2, playerY + playerSize, playerX + playerSize/2, playerY + playerSize); 
}
  // show the target
    
    if (targetActive == 1)  
    {
      stroke(targetC);
      fill(targetC);
      ellipse(targetX, targetY, playerSize - 20, playerSize - 20);
    }
    
  // show the bullet
  stroke(bulletC);
  line(bulletX, bulletY, bulletX, bulletY - playerSize / 2); 

  // display the score
  fill(textC);
  textSize(25);
//  imageMode(CENTER);
// image(hard, 20, 50, 500, 500);
  text("Score:", 20, 50); 
  text(score, 150, 50); 
  textSize(36);

  // display the lives
  fill(textC);
  textSize(25);
  text("Life:", sizeX - 120, 50); 
  text(life, sizeX - 40, 50); 
  textSize(36);
}


// check if a key has been pressed
void keyPressed(KeyEvent e)
{
  switch (keyCode)
  {
    case 'A': // left
      playerDirection = -1;
    break;
    
    case 'D': // right
      playerDirection = 1;
    break;
    
    case 'Q':
      if (gameMode == 3)
      {
        gameMode = 1;
      }
    break;

    case 32:  // fire
    if (playerFire == 0 && gameMode == 3) 
    {
      playerFire = 1;
      bulletX = playerX;
      bulletY = playerY - playerSize/2;
    }
      
    break;

    case 'S': // go = start game
      if (gameMode == 1)
      {
        gameMode = 2;
      }
    break;

    case 'P': // pause
      if (gameMode == 3)
      {
        gameMode = 4;
      }
      else if (gameMode == 4)
      {
        gameMode = 3;
      }
    break;
  }
}


// check if a key has been released
void keyReleased(KeyEvent e)
{
  switch (keyCode)
  { 
    case 'A':
      playerDirection = 0;
    break;
    
    case 'D':
      playerDirection = 0;
    break;

    case 32:
//      playerFire = 0;
    break;
  }
}
