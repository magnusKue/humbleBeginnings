color white  = color(255, 255, 255);
color black  = color(0, 0, 0);
color green  = color(0, 200, 0);
color yellow = color(200, 200, 0);
color red    = color(200, 0, 0);

color screenC = black;
color playerC = white;
color bulletC = white;
color textC = green;

int playerSize = 20;

int sizeX = 500;
int sizeY = 500;

int playerX = sizeX / 2;
int playerY = sizeY - 10 - playerSize;

int score = 0;
int life = 3;

int playerDirection = 0; // direction: -1 left, 0 stop, 1 right
int playerFire = 0;      // 0 stop, 1 active

int gameMode = 1; // 0 = game over, 1 = intro, 2 - init game, 3 = in game, 4 = pause, 5 = end game, 6 = enter highscore, 7 = finalize, 8-9 = not used 

void setup()
{
  size(500, 500);
  textSize(36);
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
      // nothing special to do here, could add a text like Game Over, or some intro animation (self-play)
      fill(red);
      textSize(50);
      text("Space Attack", 100, 200);
      fill(green);
      textSize(20);
      text("V1.0 (c) AcB of BITS 05/2017", 110, 240);
      fill(yellow);
      textSize(36);
      text("Game", 200, 300);
      text("Over", 210, 350);
    break;  

    case 2: //init
      score = 0;
      life = 3;
      gameMode = 3;  // switch to inGame mode
    break;  

    case 3: // inGame - we do all active gaming stuff here
      if (playerDirection == -1) // left
      {
        if (playerX > (0 + playerSize) )
        {
          playerX = playerX - 5;
        }
      }
    
      if (playerDirection == 1) // down
      {
        if (playerX + playerSize < sizeY)
        {
          playerX = playerX + 5;
        }
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
  line(playerX, playerY, playerX + playerSize/2, playerY + playerSize); 
  line(playerX, playerY, playerX - playerSize/2, playerY + playerSize); 
  line(playerX - playerSize/2, playerY + playerSize, playerX + playerSize/2, playerY + playerSize); 

  // show the target
  
  // show the bullet
 
  // display the score
  fill(textC);
  textSize(25);
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
    case 37: // left
      playerDirection = -1;
    break;
    
    case 39: // right
      playerDirection = 1;
    break;
    
    case 'Q':
      if (gameMode == 3)
      {
        gameMode = 1;
      }
    break;

    case 32:  // fire
      playerFire = 1;
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
    case 37:
      playerDirection = 0;
    break;
    
    case 39:
      playerDirection = 0;
    break;

    case 32:
      playerFire = 0;
    break;
  }
}