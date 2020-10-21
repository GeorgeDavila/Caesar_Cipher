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

my_string = 'Hi, World. My Name Is George!!!!!!!'
#my_string = my_string.lower() #Force to lowercase. Case doesnt really affect meaning, so simplify.
#my_string = re.sub(r'[^\w\s]','',my_string) #Remove punctuation.

def string_cleaning(string1): #make the string acceptable as input for our cipher
    string1 = string1.lower() #Force to lowercase. Case doesnt really affect meaning, so simplify.
    string1 = re.sub(r'[^\w\s]','',string1) #Remove punctuation.
    return string1

my_string = string_cleaning(my_string)

print(my_string)


alphabet_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print(len(alphabet_list))

#Forward +n permutation cipher
def forward_permutation_cipher(n):
    n = n % len(alphabet_list) # set n = n mod(len(alphabet_list)) = n mod(26) so we only need to deal with n = 0, ... , len(alphabet_list) cases
    cipher_list = [None] * len(alphabet_list)

    for i in range(len(alphabet_list)):
        cipher_list[i] = alphabet_list[ i - n ]
    return cipher_list

'''
apply the cipher by replacing stringinput[i] with forward_permutation_cipher(n)[i]
redefine a as b by doing stringinput[50] = a = forward_permutation_cipher(1)[1]

stringinput is by assertion aligned with alphabet_list, since its written in normal language
to reverse the function we could just do it with a negative n, -n 
'''

def apply_cipher(stringinput , n): 
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
def apply_decipher(ciphered_text , n):
    deciphered_text = apply_cipher( ciphered_text , n)
    return deciphered_text

print('========================Forward Cipher=================================')

n = 2 
print( forward_permutation_cipher(n) )
#for j in range(26):
#    print( forward_permutation_cipher(j) )

print( my_string )

cipher1 = apply_cipher(my_string, n)
print( cipher1 )

print( apply_decipher( cipher1 , -n) )



'''
#example code used to help construct apply_cipher() function
cipherex1 = list('hiworldmynameisgeorge')
print(cipherex1[3])
forward_permutation_cipher(1)
permutedex1 = forward_permutation_cipher(1)[ alphabet_list.index( cipherex1[3] ) ]
print( permutedex1 )
'''

# -------------------------------------Random Cipher-------------------------------------
'''Now want to randomly permute the alphabet and decipher that (under the assumption that we know the mapping)
We do #import random above to use random package
'''

#Random permutation cipher with non repeating mappings, ie random 1 to 1 mapping
def random_permutation_cipher(s1):
    #create the cipher list, ie the mapping
    cipher_list = alphabet_list[0:] #write it this way to prevent it from setting an equivalence cipher_list = alphabet_list, which means if we edited cipher alphabet would also be edited. Dont want that 
    random.shuffle( cipher_list ) #randomly shuffles list
    key = cipher_list #cipher_list is now our key 
    print(alphabet_list)
    print(key)
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

def known_cipher(s1, preknownkey):
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


print('========================Random Cipher=================================')

print( my_string )

[key, random_ciphered_text] = random_permutation_cipher( my_string )
print(key)
print(random_ciphered_text)


def random_permutation_decipher(s2, key1):
    #key1 = key1[0:]
    L2 = list( s2 )

    for k in range(len( L2 )):
        L2[k] = alphabet_list[ key.index( L2[k] ) ] #just invert the original ciphering
    
    #turn modified list back into string
    s2 = ''.join(L2)
    return s2

print('Deciphering: ')
print( random_permutation_decipher( random_ciphered_text, key ) )
#it works!

print('Apply known_cipher with pre-known key: ')
print( known_cipher( my_string , key) )



print('========================Save to file =================================')
#save key to file called codex labeled as key_number 
#takes an integer label as input 
def savetofiles(s1, mykey): # key and a label, label just an integer 
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





#get key using label generated above 
def decipherfromfile(label): #need your label otherwise cant decode, ie cipher works well 
    #Find key from label
    label = str(label)
    keylogfilename = 'keylog.txt'
    keylogfile = open(keylogfilename, 'r')
    
    keylogstring = keylogfile.read()
    keylist_startindex = keylogstring.find( label ) + 9 #finds the unique 8-digit string saved by savetofiles() add 9 to get to the key
    keylist_endindex = keylist_startindex + 140  -10 #set at this string, do 140 for length of whole list -10 for length of label + [ + , 

    knownkey = keylogstring[keylist_startindex : (keylist_endindex )]  #index is at 140 but do +1 for [: ] operation
    #if using alphabet length = 26, else keep in mid each char adds 3 length ie 'z' in this string, so if using alphabet of len = 50 need to add 24*3 = 72 so this term becomes 140 + 72 = 212
    #under the structure we defined in savetofiles(), the list position will begin at 1  less than the label
    print( 'key = ' + knownkey )

    #Find string from label
    textlogfilename = 'encrypted_texts.txt'
    textlogfile = open(textlogfilename, 'r')
    textlogstring = textlogfile.read()


    textlist_startindex = textlogstring.find( label ) + 9 #finds the unique 8-digit string saved by savetofiles()
    textlist_endindex = textlogstring.find(']', textlist_startindex) - 1 #Finds the next bracket starting from the unique label

    text_to_decipher = textlogstring[ textlist_startindex : (textlist_endindex + 1)]
    print( 'ciphered text = ' + text_to_decipher )
    #return str( known_cipher( text_to_decipher , knownkey) )
    return print( 'the translation for the text of label = ' + label + ' is: ' + random_permutation_decipher( text_to_decipher , knownkey) ) 




[key, random_ciphered_text] = random_permutation_cipher( my_string )
print(key)
print(random_ciphered_text)



print('-----------------------------Custom Input---------------------------------------------')
input_text = input('Type a string to encrypt: ')
print(input_text)

[key, ciphered_input_text] = random_permutation_cipher( string_cleaning( input_text ) )


savedKey = savetofiles( ciphered_input_text , key )[1] #key is at this index

#input_cipher = random_permutation_cipher( string_cleaning( input_text ) )[0]
#print(input_text)
#print(input_cipher)



#def final_encrypt_input():
#    savetofiles( 
# random_permutation_cipher( string_cleaning( input('Type a string to encrypt: ') ) )[0]
# )

print('-----------------------------Decipher the custom input from its label---------------------------------------------')
#decipherfromfile(56486268)

decipherfromfile(savedKey) #pull in the cached key, use to test this function
