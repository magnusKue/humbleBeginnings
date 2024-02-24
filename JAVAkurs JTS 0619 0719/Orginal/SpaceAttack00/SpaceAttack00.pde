/*

SpaceAttack00.pde

31.05.2017  V1.0    A.Bucher     created

Space attack game.

Cannon is at bottom, move left/right with A/D keys, fire with X key.
Enemy (Target) attacks from the top, moves down. If target hits player: Reduce life. If bullet hits Target: Add score.
If enemy passes bottom: Do nothing.
G to start, P for pause, Q to quit

Step 00: Basic program structure, color definitions, definition of vars, draw player, show score

*/

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
int playerFire = 0;      // 0: stop, 1: active

int gameMode = 1; // 0 = game over, 1 = intro, 2 - init game, 3 = in game, 4 = pause, 5 = end game, 6 = enter highscore, 7 = finalize, 8-9 = no used 

void setup()
{
  size(500, 500);
  textSize(36);
}

void draw()
{
  background(screenC); // erase screen
  
  // println(playerDirection);
  // println(playerX);
  
  // show the objects on screen

  stroke(playerC); // define player color

  // show the player
  line(playerX, playerY, playerX + playerSize/2, playerY + playerSize);
  line(playerX, playerY, playerX - playerSize/2, playerY + playerSize);
  line(playerX + playerSize/2, playerY + playerSize, playerX - playerSize/2, playerY + playerSize);

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
  switch (key)
  {
    case 'a': // left
    {
      playerDirection = -1;
      break;
    }
  
    case 'd': // right
    {
      playerDirection = 1;
      break;
    }
  }
}


// check if a key has been released
void keyReleased(KeyEvent e)
{
  switch (key)
  {
    case 'a': // left
    {
      playerDirection = 0;
      break;
    }
  
    case 'd': // right
    {
      playerDirection = 0;
      break;
    }
  }
}