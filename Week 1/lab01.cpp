/*************************************************************
 * 1. Name:
 *      Bryce Chesley
 * 2. Assignment Name:
 *      Lab 01: Hello World
 * 3. Assignment Description:
 *      Please the text "Hello world" on the screen
 * 4. What was the hardest part? Be as specific as possible.
 *      Nothing really, this is quite a simple task
 * 5. How long did it take for you to complete the assignment?
 *      20 minutes
 *****************************************************************/


#include <iostream>
#include <conio.h>
#include <string>
using namespace std;



/******************************
* A function to pause the terminal
* until any character is entered.
******************************/

void pause()
{
   char c;
   c = _getch();

}

/*********************************
* The main function. It displays
* Hello World then calls pause so
* we can view the output in the terminal.
**********************************/

int main() 
{
   cout << "Hello World\n";

   pause();

   return 0;
}