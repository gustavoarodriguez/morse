#### MORSE ####

### Set Code

CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',   ' ': ' ',
        
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }
        
#Get msg
msg = raw_input('Message: ')
msg = msg.strip()
msg2 = '' #Def output var
## Convert

if msg[0] == '.' or msg[0] == '-': #If morse-text
	msg = msg.replace('  ',' ')
	msg = msg.split(' ')
	## Replace empty for whitespace
	for c in range(len(msg)):
		if msg[c] == '':
			msg[c] = ' '
	##
	for char in msg:
		for i in CODE:
			if char == CODE[i]:
				msg2 = msg2+i
else: #if text-morse
	for char in msg:
		msg2 = msg2+CODE[char.upper()]+' '
msg2 = msg2.rstrip()

## Print Result
print(msg2)
