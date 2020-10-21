'''
Given string 'hi world my name is george' want to cipher and decipher it 
(dont say encode decode since those have their own meanings in some programs)
can later make a fn to give unciphers of unknown cipher input
if a common word like 'the' or a singular 'a', can have it flag hey this interpret gives common words
also look for common pairings. ie if 'xds' appears commonly in a long text it might be 'the' 
Seeing as how there are 26! (factorial) > 10^26 combinations this is probably our best hope

Assert that its a one-to-one lowercase letter to letter only cipher. 
ie no punctuation or number cipher ? = a, 4=b. 
No uppercase conversion A = m, both for simplicity and also Ancient Roman Latin was written in one case anyway (uppercase but i'd rather look at lowercase here)
Also remove spaces. Ancient Latin actually didnt have any spaces. 
Alsohereitcanhelpcutdowncomputetime. You can also probably read that. 

We'll make this cipher a simple forward permutation cipher. ie its just the alhabet shifted by +n letters. 
ie if n = 3 then a -> d, d-> g, z -> c

will also use english alphabet represented as list. 
This way you can easily bring in your own greek, hindi, spanish with an n tilde, etc. 
Simply replace alphabet_list with your own alphabet. 
Can also assert your own order for the alphabet for additional security. ie alphabet_list = [z,a,t,g....]
Note we also use alphabet_list in some definitions, dont change the name 'alphabet_list'. 

s = "string. With. Punctuation?"
s = re.sub(r'[^\w\s]','',s)
print(s)
This snippet from https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string
'''

import re
import random

#
class CaesarCipher:
    my_string = 'Hi, World. My Name Is George!!!!!!!'

    def string_cleaning(self, string1): #make the string acceptable as input for our cipher
        string1 = string1.lower() #Force to lowercase. Case doesnt really affect meaning, so simplify.
        string1 = re.sub(r'[^\w\s]','',string1) #Remove punctuation.
        return string1

    my_string = string_cleaning(my_string)

    alphabet_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    #Forward +n permutation cipher
    def forward_permutation_cipher(self, n):
        n = n % len(alphabet_list) # set n = n mod(len(alphabet_list)) = n mod(26) so we only need to deal with n = 0, ... , len(alphabet_list) cases
        cipher_list = [None] * len(alphabet_list)

        for i in range(len(alphabet_list)):
            cipher_list[i] = alphabet_list[ i - n ]
        return cipher_list

    def apply_cipher(self, stringinput , n): 
        n = n % len(alphabet_list) # set n = n mod(len(alphabet_list)) = n mod(26) so we only need to deal with n = 0, ... , len(alphabet_list) cases
        #change to list so we can operate on it as below
        listof_stringinput = list( stringinput )
        while(' ' in listof_stringinput):
            listof_stringinput.remove(' ') #remove is a list operation so do it here 
        # print(len(listof_stringinput)) <--- wont equal to 26, so need to use it in for loop
        for k in range(len(listof_stringinput)):
            listof_stringinput[k] = forward_permutation_cipher(-n)[ alphabet_list.index( listof_stringinput[k] ) ]
        #turn modified mist back into string
        stringinput = ''.join(listof_stringinput)
        return stringinput

    #to decipher apply same (but effectivel negative) permutation value n as you use to create the cipher
    # NOTICE we dont make n negative here since we made it neg in the for loop of the apply_cipher() function
    def apply_decipher(self, ciphered_text , n):
        deciphered_text = apply_cipher( ciphered_text , n)
        return deciphered_text


    #Random permutation cipher with non repeating mappings, ie random 1 to 1 mapping
    def random_permutation_cipher(self, s1):
        #create the cipher list, ie the mapping
        cipher_list = alphabet_list[0:] #write it this way to prevent it from setting an equivalence cipher_list = alphabet_list, which means if we edited cipher alphabet would also be edited. Dont want that 
        random.shuffle( cipher_list ) #randomly shuffles list
        key = cipher_list #cipher_list is now our key 
        #apply the cipher 
        L1 = list( s1 )
        while(' ' in L1 ):
            L1.remove(' ') #remove is a list operation so do it here to remove whitespace
    
        # print(len( L1 )) <--- wont equal to 26, so need to use it in for loop
        for k in range(len( L1 )):
            L1[k] = key[ alphabet_list.index( L1[k] ) ]
        #turn modified list back into string
    
        s1 = ''.join(L1)
        return [cipher_list, s1]

    def known_cipher(self, s1, preknownkey):
        #cipher in which the user already has a key to input
        #ie you generated a key earlier, you put your key in here to use it again
        # Note that forward_permutation_cipher(n)  AND random_permutation_cipher(s1)[0]  gives the keys
        key = preknownkey #cipher_list is now our key 
    
        #apply the cipher 
        L1 = list( s1 )
        while(' ' in L1 ):
            L1.remove(' ') #remove is a list operation so do it here to remove whitespace

        # print(len( L1 )) <--- wont equal to 26, so need to use it in for loop
        for k in range(len( L1 )):
            L1[k] = key[ alphabet_list.index( L1[k] ) ]
        #turn modified list back into string
    
        s1 = ''.join(L1)
        return s1 #only outputs string since key was input

    def random_permutation_decipher(self, s2, key1):
        L2 = list( s2 )

        for k in range(len( L2 )):
            L2[k] = alphabet_list[ key.index( L2[k] ) ] #just invert the original ciphering

        #turn modified list back into string
        s2 = ''.join(L2)
        return s2

#save key to file called codex labeled as key_number 


