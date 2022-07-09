# PNG file LSB steganography tool 
***LSB PNG文件LSB隐写工具***\
*Author : localh0st*

## usage:
* ***Encrypt***
```commandline
import Steganography

str_to_be_encrypted = 'Sad story was that she rejected me unconciously on July 6th, 2022.But I still wish to befrend her'
file_input = './images/car.png'     # set input png file with path
file_output = './img_edited/car_with_secret.png'    # set output file name with path
Steganography.encrypt(file_input, file_output, str_to_be_encrypted, mod='R')  # execute
```
*To explain mod, I offered 3 kind of mods, namely 'R'/'G'/'B', the only difference between the 3 mods is the color channel it uses.*\
After you execute, command line would tell you 'Done'.
* ***Decrypt***
```commandline
import Steganography

file_to_be_decrypted = './img_edited/car_with_secret.png'   # set file_to_be_decrypted
Steganography.decrypt(file_to_be_decrypted)     # execute
```
After you execute, command line would tell you the result like:
```commandline
Sad story was that she rejected me unconciously on July 6th, 2022.But I still wish to befrend her
```