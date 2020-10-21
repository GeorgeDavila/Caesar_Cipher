import re
import random

alphabet_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

class MyCaesarCipher:

    def string_cleaning(self, string1): #make the string acceptable as input for our cipher
        string1 = string1.lower() #Force to lowercase. Case doesnt really affect meaning, so simplify.
        string1 = re.sub(r'[^\w\s]','',string1) #Remove punctuation.
        string1 = re.sub(r'[0-9]+', '', string1) #remove digits
        return string1

    def forward_caesar_permutation_cipher(self, s1, n): #ie classical Caesar Cipher
        n = int(n) % len(alphabet_list) # set n = n mod(len(alphabet_list)) = n mod(26) so we only need to deal with n = 0, ... , len(alphabet_list) cases
        cipher_list = alphabet_list[0:]
        L1 = list( s1 )
        while(' ' in L1 ):
            L1.remove(' ') #remove is a list operation so do it here to remove whitespace
            
        for i in range(len(alphabet_list)):
            cipher_list[i] = alphabet_list[ i - n ]
        print(cipher_list)
        key = cipher_list #cipher_list is now our key 

        for k in range(len( L1 )):
            L1[k] = key[ alphabet_list.index( L1[k] ) ]

        s1 = ''.join(L1)
        return [cipher_list, s1]
    
    def random_permutation_decipher(self, s2, key1): #not random here, but keep name from main.py for consistency, same function
        #key1 = key1[0:]
        L2 = list( s2 )

        for k in range(len( L2 )):
            L2[k] = alphabet_list[ key.index( L2[k] ) ] #just invert the original ciphering
    
        #turn modified list back into string
        s2 = ''.join(L2)
        return s2

    def savetofiles(self, s1, mykey): # key and a label, label just an integer #save key to file called codex labeled as key_number 
        #Save key to file containing keys
        keylabel = random.randint(10000000, 99999999) #Creates a 8-digit label for the key, Note that we use this to call the key
        keylogfilename = 'caesar_keylog.txt'
        keylogfile = open(keylogfilename, 'a')
        keylogfile.write( '[' + str(keylabel) + ',' + str(mykey) + ']' + '\n' )
        keylogfile.close()

        #Save string to file of its own, stored with keylabel so we know what key to use 
        textlogfilename = 'caesar_encrypted_texts.txt'
        textlogfile = open(textlogfilename, 'a')
        textlogfile.write( '[' + str(keylabel) + ',' + str(s1) + ']' + '\n' ) #save it alongside corresponding key label
        textlogfile.close()
        return ['key successfully saved under label ' + str(keylabel), str(keylabel)] 

    def decipherfromfile(self, label): #need your label otherwise cant decode, ie cipher works well #get key using label generated above 
        #Find key from label
        label = str(label)
        keylogfilename = 'caesar_keylog.txt'
        keylogfile = open(keylogfilename, 'r')
        keylogstring = keylogfile.read()
        keylist_startindex = keylogstring.find( label ) + 9 #finds the unique 8-digit string saved by savetofiles() add 9 to get to the key
        keylist_endindex = keylist_startindex + 140  -10 #set at this string, do 140 for length of whole list -10 for length of label + [ + , 
        knownkey = keylogstring[keylist_startindex : (keylist_endindex )]  #index is at 140 but do +1 for [: ] operation

        #Find string from label
        textlogfilename = 'caesar_encrypted_texts.txt'
        textlogfile = open(textlogfilename, 'r')
        textlogstring = textlogfile.read()
        textlist_startindex = textlogstring.find( label ) + 9 #finds the unique 8-digit string saved by savetofiles()
        textlist_endindex = textlogstring.find(']', textlist_startindex) - 1 #Finds the next bracket starting from the unique label
        text_to_decipher = textlogstring[ textlist_startindex : (textlist_endindex + 1)]
        return [ text_to_decipher , knownkey ]

'''
input_text = input('Type a string to encrypt: ')
#caesar_cipher_funcs.string_cleaning( input_text )
print( caesar_cipher_funcs.string_cleaning( input_text ) )
'''

#instantiate object 
caesar_cipher_funcs = MyCaesarCipher()


input_text = input('Type a string to encrypt: ')
permutation_value = int( input('Permutation value? Enter the amount you want to shift the alphabet by: ') )   #eg if you want a --> c type in 2. 
[key, ciphered_text] = caesar_cipher_funcs.forward_caesar_permutation_cipher( caesar_cipher_funcs.string_cleaning( input_text ) , permutation_value )
print( 'the ciphered text is: ' + str(ciphered_text) )

savedKey = caesar_cipher_funcs.savetofiles( ciphered_text , key )[1] #key is at this index
print('Successfully saved text to encrypted_texts.txt !!!!!!!!!!!!!!')
deciphered_text = caesar_cipher_funcs.random_permutation_decipher( caesar_cipher_funcs.decipherfromfile( savedKey )[0] , caesar_cipher_funcs.decipherfromfile( savedKey ) [1]  )

print( 'the deciphered text is: ' + str(deciphered_text) ) #just run to see that its all working. If you get your input text then it works!

'''
#To use your own label / decipher past encryptings:
#Uncomment this multiline comment
#then replace both YOUR_KEY_HERE with your 8-digit key that appears next to you text in the encrypted_texts.txt file
deciphered_text2 = caesar_cipher_funcs.random_permutation_decipher( caesar_cipher_funcs.decipherfromfile( YOUR_KEY_HERE )[0] , caesar_cipher_funcs.decipherfromfile( YOUR_KEY_HERE ) [1] )
print( 'Your deciphered text is: ' + str(deciphered_text) )
'''













