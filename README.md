# Arduino Liquid Crystal Character Creator
An app to help create custom characters for the **LiquidCrystal.h arduino library**.
Instructions:

To create custom characters using ALCCC, you must first create a **template**,
Press 2 to create a template, and specify the number of characters.
The template will be exported under the name **"Output.png"**, open it in your favorite photo editing software (if you dont have one you can use- https://www.piskelapp.com/). <br>
  this is an example for a 3 character template ![Example Template](/pics/Output.png). <br>
Draw your desired characters (black colored) in the **brighter** parts of the image.
Save the new image and place it in the **same folder** as "Output.png" (this is your **input** file).  <br>
![Example ETemplate](/pics/Input.png)<br>

Press 3 to create the Character Array, specify the name of the input file.
ALCCC will create a text file named the same as the input file, this is your character array. <br>

**Example:**

  byte char0[8] = {B00000,B01110,B10001,B10001,B00010,B00100,B00000,B00100,} <br>
  byte char1[8] = {B00000,B00100,B00100,B00100,B00100,B00100,B00000,B00100,} <br>
  byte char2[8] = {B00000,B00000,B01110,B10001,B10101,B10111,B10000,B01110,} <br>


All thats left is to copy it into your project!
