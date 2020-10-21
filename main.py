import re
import random

alphabet_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

class MyCipher:

    def string_cleaning(self, string1): #make the string acceptable as input for our cipher
        string1 = string1.lower() #Force to lowercase. Case doesnt really affect meaning, so simplify.
        string1 = re.sub(r'[^\w\s]','',string1) #Remove punctuation.
        return string1

    def random_permutation_cipher(self, s1):
        #create the cipher list, ie the mapping
        cipher_list = alphabet_list[0:] #write it this way to prevent it from setting an equivalence cipher_list = alphabet_list, which means if we edited cipher alphabet would also be edited. Dont want that 
        random.shuffle( cipher_list ) #randomly shuffles list
        key = cipher_list #cipher_list is now our key 
        #apply the cipher 
        L1 = list( s1 )
        while(' ' in L1 ):
            L1.remove(' ') #remove is a list operation so do it here to remove whitespace
    
        # print(len( L1 )) <--- wont necessarily equal to 26, so need to use it in for loop
        for k in range(len( L1 )):
            L1[k] = key[ alphabet_list.index( L1[k] ) ]
        #turn modified list back into string

        s1 = ''.join(L1)
        return [cipher_list, s1]
    
    def random_permutation_decipher(self, s2, key1):
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
        keylogfilename = 'keylog.txt'
        keylogfile = open(keylogfilename, 'a')
        keylogfile.write( '[' + str(keylabel) + ',' + str(mykey) + ']' + '\n' )
        keylogfile.close()

        #Save string to file of its own, stored with keylabel so we know what key to use 
        textlogfilename = 'encrypted_texts.txt'
        textlogfile = open(textlogfilename, 'a')
        textlogfile.write( '[' + str(keylabel) + ',' + str(s1) + ']' + '\n' ) #save it alongside corresponding key label
        textlogfile.close()
        return ['key successfully saved under label ' + str(keylabel), str(keylabel)] 

    def decipherfromfile(self, label): #need your label otherwise cant decode, ie cipher works well #get key using label generated above 
        #Find key from label
        label = str(label)
        keylogfilename = 'keylog.txt'
        keylogfile = open(keylogfilename, 'r')
        keylogstring = keylogfile.read()
        keylist_startindex = keylogstring.find( label ) + 9 #finds the unique 8-digit string saved by savetofiles() add 9 to get to the key
        keylist_endindex = keylist_startindex + 140  -10 #set at this string, do 140 for length of whole list -10 for length of label + [ + , 
        knownkey = keylogstring[keylist_startindex : (keylist_endindex )]  #index is at 140 but do +1 for [: ] operation

        #Find string from label
        textlogfilename = 'encrypted_texts.txt'
        textlogfile = open(textlogfilename, 'r')
        textlogstring = textlogfile.read()
        textlist_startindex = textlogstring.find( label ) + 9 #finds the unique 8-digit string saved by savetofiles()
        textlist_endindex = textlogstring.find(']', textlist_startindex) - 1 #Finds the next bracket starting from the unique label
        text_to_decipher = textlogstring[ textlist_startindex : (textlist_endindex + 1)]
        return [ text_to_decipher , knownkey ]

'''
input_text = input('Type a string to encrypt: ')
#cipher_funcs.string_cleaning( input_text )
print( cipher_funcs.string_cleaning( input_text ) )
'''

#instantiate object 
cipher_funcs = MyCipher()

input_text = input('Type a string to encrypt: ')
[key, ciphered_text] = cipher_funcs.random_permutation_cipher( cipher_funcs.string_cleaning( input_text ) )
print( 'the ciphered text is: ' + str(ciphered_text) )

savedKey = cipher_funcs.savetofiles( ciphered_text , key )[1] #key is at this index
print('Successfully saved text to encrypted_texts.txt !!!!!!!!!!!!!!')
deciphered_text = cipher_funcs.random_permutation_decipher( cipher_funcs.decipherfromfile( savedKey )[0] , cipher_funcs.decipherfromfile( savedKey ) [1] )

print( 'the deciphered text is: ' + str(deciphered_text) ) #just run to see that its all working. If you get your input text then it works!

'''
#To use your own label / decipher past encryptings:
#Uncomment this multiline comment
#then replace both YOUR_KEY_HERE with your 8-digit key that appears next to you text in the encrypted_texts.txt file
deciphered_text2 = cipher_funcs.random_permutation_decipher( cipher_funcs.decipherfromfile( YOUR_KEY_HERE )[0] , cipher_funcs.decipherfromfile( YOUR_KEY_HERE ) [1] )
print( 'Your deciphered text is: ' + str(deciphered_text) )
'''













