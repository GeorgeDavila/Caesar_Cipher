# Caesar_Cipher
Caesarian Cipher written in python. An ancient cipher used by Julius Caesar himself. 

Just type python caesar_main.py in command line to run.
It will then ask you to type something. Type your text then press enter. 
It will then ask for a Permutation Value. This is the amount we shift the alphabet by, ie if you enter 1 then a-->b & b-->c  etc., if 2 then a-->c & b-->d and so on. Make sure you enter a Number! Then press enter.

You will then see the results: your string Caesarian ciphered by shifting the letters of the alphabet. 
The ciphered text will be stored in caesar_encrypted_texts.txt and the keys in caesar_keylog.txt


# Randomized Permutation Cipher 
Note how the Caesar cipher is fairly easy to decipher if you know whats going on. You only need to keep shifting letters until you hit something.

So we'll make a stronger cipher. Here we permute the alphabet randomly. I.e. letter a could become x or z or anything. also knowing a doesnt tell us what b has become, every letter is random.  
This one is much more secure!

Just type python main.py in command line to run.
It will then ask you to type something. Type your text then press enter. 

You will then see the results: your string randomly permuted by shifting the letters of the alphabet (but randomly this time!). 
The ciphered text will be stored in encrypted_texts.txt and the keys in keylog.txt


