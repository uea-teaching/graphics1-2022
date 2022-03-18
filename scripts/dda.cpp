#include <stdlib.h>
#include <math.h>

inline int round (const float a)  { return int (a + 0.5); }

// Assume a function setPixel exists.

void naiveDDA (int x0, int y0, int xEnd, int yEnd){
    int x = x0;
    float y = float (y0);
    float m = float (yEnd - y0) / float (xEnd - x0);

   for (x = x0; x <= xEnd; x++) {
        setPixel (x, round (y));
        y += m;
} }


void lineDDA (int x0, int y0, int xEnd, int yEnd){
    int dx=xEnd-x0, dy=yEnd-y0, steps, k; 
    float xIncrement, yIncrement, x = x0, y = y0;

   if (fabs (dx) > fabs (dy))
      steps = fabs (dx);
   else
      steps = fabs (dy);

   xIncrement = float (dx) / float (steps);
   yIncrement = float (dy) / float (steps);

   setPixel (round (x), round (y));
   for (k = 0; k < steps; k++) {
        x += xIncrement;
        y += yIncrement;
        setPixel (round (x), round (y));
} }

void lineMid(int x0, int y0, int xEnd, int yEnd){  
    int dx=xEnd-x0, dy=yEnd-y0, x=x0, y=y0;  
    int E_inc = 2*dy, NE_inc = 2*(dy-dx), D = 2*dy-dx;

    setPixel(x,y);
    while(x<xEnd){
        if (D > 0){
            D += NE_inc;
            x++; y++;
        } else {
            D += E_inc;
            x++;
        }
    setPixel(x,y);
}  }
