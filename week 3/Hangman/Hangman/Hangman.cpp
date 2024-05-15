// Hangman.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>
#include <vector>
using namespace std;

string getRandomWord(int difficulty) {
   // Define lists of words for each difficulty level
   vector<std::string> easyWords = {
       "apple", "banana", "cat", "dog", "bird", "fish", "tree", "house", "book", "chair",
       "table", "sun", "moon", "star", "cloud", "flower", "grass", "bird", "fish", "turtle",
       "car", "boat", "hat", "shoe", "shirt", "pants", "sock", "glove", "cake", "candy",
       "cookie", "milk", "juice", "bread", "cheese", "egg", "tomato", "potato", "carrot",
       "banana", "orange", "lemon", "strawberry", "grape", "peach", "pear", "watermelon",
       "pineapple", "cherry", "plum"
   };

   vector<string> mediumWords = {
       "elephant", "giraffe", "lion", "tiger", "zebra", "monkey", "kangaroo", "hippo", "rhino", "crocodile",
       "snake", "lizard", "spider", "ant", "bee", "butterfly", "ladybug", "caterpillar", "dragonfly", "grasshopper",
       "cricket", "frog", "turtle", "snail", "octopus", "jellyfish", "seahorse", "dolphin", "whale", "shark",
       "penguin", "polarbear", "seal", "walrus", "otter", "bat", "owl", "eagle", "hawk", "falcon",
       "vulture", "crow", "flamingo", "pelican", "swan", "goose", "duck", "parrot", "toucan", "peacock"
   };

   vector<string> hardWords = {
       "astronomy", "biology", "chemistry", "physics", "mathematics", "geography", "history", "literature", "philosophy", "psychology",
       "sociology", "economics", "politics", "anthropology", "linguistics", "archaeology", "criminology", "theology", "engineering",
       "computer", "technology", "medicine", "dentistry", "pharmacy", "nursing", "radiology", "surgery", "psychiatry", "neurology",
       "cardiology", "dermatology", "ophthalmology", "orthopedics", "pediatrics", "oncology", "gastroenterology", "pulmonology",
       "urology", "nephrology", "endocrinology", "immunology", "rheumatology", "hematology", "oncologist", "psychiatrist",
       "cardiologist", "neurologist", "dermatologist", "ophthalmologist", "orthopedist"
   };
   int randomindex = rand() % easyWords.size();

   if (difficulty == 1)
   {
      return easyWords[randomindex];
   }
   else if (difficulty == 2)
   {
      return mediumWords[randomindex];
   }
   else
   {
      return hardWords[randomindex];
   }
}

int isInWord(char input, string word)
{
   if (word.find(input) != std::string::npos)
   {
      return word.find(input);
   }
   else
   {
      return -1;
   }
}

void displayMan(int life, int difficulty)
{
   if (life == 0)
   {
      cout << "      ________" << endl;
      cout << "      |      |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "_____________|" << endl;
   }
   else if (life == 1 && difficulty == 1)
   {
      cout << "      ________" << endl;
      cout << "      |      |" << endl;
      cout << "      |      |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "_____________|" << endl;
   }
   else if (life == 2 && difficulty == 1)
   {
      cout << "      ________" << endl;
      cout << "      |      |" << endl;
      cout << "      |      |" << endl;
      cout << "     (       |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "_____________|" << endl;
   }
   else if ((life == 3 && difficulty == 1) || (life == 1 && difficulty == 2) || (life == 1 && difficulty == 3))
   {
      cout << "      ________" << endl;
      cout << "      |      |" << endl;
      cout << "      |      |" << endl;
      cout << "     ()      |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "_____________|" << endl;
   }
   else if (life == 4 && difficulty == 1)
   {
      cout << "      ________" << endl;
      cout << "      |      |" << endl;
      cout << "      |      |" << endl;
      cout << "     ()      |" << endl;
      cout << "      |      |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "_____________|" << endl;
   }
   else if (life == 5 && difficulty == 1)
   {
      cout << "      ________" << endl;
      cout << "      |      |" << endl;
      cout << "      |      |" << endl;
      cout << "     ()      |" << endl;
      cout << "      |/     |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "_____________|" << endl;
   }
   else if ((life == 6 && difficulty == 1) || (life == 2 && difficulty == 2) || (life == 2 && difficulty == 3))
   {
      cout << "      ________" << endl;
      cout << "      |      |" << endl;
      cout << "      |      |" << endl;
      cout << "     ()      |" << endl;
      cout << "     \\|/     |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "_____________|" << endl;
   }
   else if (life == 7 && difficulty == 1)
   {
      cout << "      ________" << endl;
      cout << "      |      |" << endl;
      cout << "      |      |" << endl;
      cout << "     () /    |" << endl;
      cout << "     \\|/     |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "_____________|" << endl;
   }
   else if ((life == 8 && difficulty == 1) || (life == 3 && difficulty == 2) || (life == 3 && difficulty == 3))
   {
      cout << "      ________" << endl;
      cout << "      |      |" << endl;
      cout << "      |      |" << endl;
      cout << "    \\() /    |" << endl;
      cout << "     \\|/     |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "_____________|" << endl;
   }
   else if (life == 9 && difficulty == 1)
   {
      cout << "      ________" << endl;
      cout << "      |      |" << endl;
      cout << "      |      |" << endl;
      cout << "    \\() /    |" << endl;
      cout << "     \\|/     |" << endl;
      cout << "      |      |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "_____________|" << endl;
   }
   else if ((life == 10 && difficulty == 1) || (life == 4 && difficulty == 2) || (life == 4 && difficulty == 3))
   {
      cout << "      ________" << endl;
      cout << "      |      |" << endl;
      cout << "      |      |" << endl;
      cout << "    \\() /    |" << endl;
      cout << "     \\|/     |" << endl;
      cout << "      |      |" << endl;
      cout << "      |      |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "_____________|" << endl;
   }
   else if (life == 11 && difficulty == 1)
   {

      cout << "      ________" << endl;
      cout << "      |      |" << endl;
      cout << "      |      |" << endl;
      cout << "    \\() /    |" << endl;
      cout << "     \\|/     |" << endl;
      cout << "      |      |" << endl;
      cout << "      |      |" << endl;
      cout << "       \\     |" << endl;
      cout << "             |" << endl;
      cout << "             |" << endl;
      cout << "_____________|" << endl;
   }
   else if ((life == 12 && difficulty == 1) || (life == 5 && difficulty == 2))
   {
      cout << "      ________" << endl;
      cout << "      |      |" << endl;
      cout << "      |      |" << endl;
      cout << "    \\() /    |" << endl;
      cout << "     \\|/     |" << endl;
      cout << "      |      |" << endl;
      cout << "      |      |" << endl;
      cout << "       \\     |" << endl;
      cout << "        |    |" << endl;
      cout << "             |" << endl;
      cout << "_____________|" << endl;
   }
   else if (life == 13 && difficulty == 1)
   {
      cout << "      ________" << endl;
      cout << "      |      |" << endl;
      cout << "      |      |" << endl;
      cout << "    \\() /    |" << endl;
      cout << "     \\|/     |" << endl;
      cout << "      |      |" << endl;
      cout << "      |      |" << endl;
      cout << "       \\     |" << endl;
      cout << "        |    |" << endl;
      cout << "        |    |" << endl;
      cout << "_____________|" << endl;
   }
   else if ((life == 14 && difficulty == 1) || (life == 6 && difficulty == 2) || (life == 5 && difficulty == 3))
   {
      cout << "      ________" << endl;
      cout << "      |      |" << endl;
      cout << "      |      |" << endl;
      cout << "    \\() /    |" << endl;
      cout << "     \\|/     |" << endl;
      cout << "      |      |" << endl;
      cout << "      |      |" << endl;
      cout << "       \\     |" << endl;
      cout << "        |    |" << endl;
      cout << "        |_   |" << endl;
      cout << "_____________|" << endl;
   }
   else if (life == 15 && difficulty == 1)
   {
      cout << "      ________" << endl;
      cout << "      |      |" << endl;
      cout << "      |      |" << endl;
      cout << "    \\() /    |" << endl;
      cout << "     \\|/     |" << endl;
      cout << "      |      |" << endl;
      cout << "      |      |" << endl;
      cout << "     / \\     |" << endl;
      cout << "        |    |" << endl;
      cout << "        |_   |" << endl;
      cout << "_____________|" << endl;
   }
   else if ((life == 16 && difficulty == 1) || (life == 7 && difficulty == 2))
   {
      cout << "      ________" << endl;
      cout << "      |      |" << endl;
      cout << "      |      |" << endl;
      cout << "    \\() /    |" << endl;
      cout << "     \\|/     |" << endl;
      cout << "      |      |" << endl;
      cout << "      |      |" << endl;
      cout << "     / \\     |" << endl;
      cout << "    |   |    |" << endl;
      cout << "        |_   |" << endl;
      cout << "_____________|" << endl;
   }
   else if (life == 17 && difficulty == 1)
   {
      cout << "      ________" << endl;
      cout << "      |      |" << endl;
      cout << "      |      |" << endl;
      cout << "    \\() /    |" << endl;
      cout << "     \\|/     |" << endl;
      cout << "      |      |" << endl;
      cout << "      |      |" << endl;
      cout << "     / \\     |" << endl;
      cout << "    |   |    |" << endl;
      cout << "    |   |_   |" << endl;
      cout << "_____________|" << endl;
   }
   else if ((life == 18 && difficulty == 1) || (life == 8 && difficulty == 2) || (life == 6 && difficulty == 3))
   {
      cout << "      ________" << endl;
      cout << "      |      |" << endl;
      cout << "      |      |" << endl;
      cout << "    \\() /    |" << endl;
      cout << "     \\|/     |" << endl;
      cout << "      |      |" << endl;
      cout << "      |      |" << endl;
      cout << "     / \\     |" << endl;
      cout << "    |   |    |" << endl;
      cout << "   _|   |_   |" << endl;
      cout << "_____________|" << endl;
   }
   else if ((life == 19 && difficulty == 1) || (life == 9 && difficulty == 2))
   {
      cout << "      ________" << endl;
      cout << "      |      |" << endl;
      cout << "      |      |" << endl;
      cout << "    \\() /    |" << endl;
      cout << "     \\|/     |" << endl;
      cout << "      |      |" << endl;
      cout << "      |      |" << endl;
      cout << "     / \\     |" << endl;
      cout << "    |   |    |" << endl;
      cout << "   _|  *|_   |" << endl;
      cout << "_____________|" << endl;
   }
   else if ((life == 20 && difficulty == 1) || (life == 10 && difficulty == 2) || (life == 7 && difficulty == 3))
   {
      cout << "      ________" << endl;
      cout << "      |      |" << endl;
      cout << "      |      |" << endl;
      cout << "    \\() /    |" << endl;
      cout << "     \\|/     |" << endl;
      cout << "      |      |" << endl;
      cout << "      |      |" << endl;
      cout << "     / \\     |" << endl;
      cout << "    |   |    |" << endl;
      cout << "   _|* *|_   |" << endl;
      cout << "_____________|" << endl;
   }
}


int main()
{
   int man = 0;
   char guess;
   int difficulty;
   cout << "What difficulty would you like? (from 1 - 3): ";
   cin >> difficulty;
   srand(static_cast<unsigned int>(time(nullptr)));

   string word = getRandomWord(difficulty);
   string blanks;
   for (int i = 0; i < word.size(); i++)
   {
      blanks.append("_");
   }
   while (blanks.find("_") != std::string::npos)
   {
      cout << "guess a letter: ";
      cin >> guess;


      if (isInWord(guess, word) >= 0)
      {
         for (int i = 0; i <= word.size(); i++)
         {
            if (word[i] == guess)
            {
               blanks[i] = guess;
            }
         }
      }
      else
      {
         man++;
      }
      displayMan(man, difficulty);
      cout << blanks << endl;
      if (man > 20 / difficulty)
      {
         cout << "You ran out of trys. too bad."<< endl;
         cout << word;
         return 0;
      }

   }

   return 0;
}
