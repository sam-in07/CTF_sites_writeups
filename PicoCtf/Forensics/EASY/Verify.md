https://learn.cylabacademy.org/library/450 

People keep trying to trick my players with imitation flags. I want to make sure they get the real thing! I'm going to provide the SHA-256 hash and a decrypt script to help you know that my flags are legitimate.



soln : 

https://github.com/noamgariani11/picoCTF-2024-Writeup/blob/main/Forensics/Verify.md   


The checksum.txt provides a SHA256 encryption checksum and the decrypt is a bash script. So the decrypt.sh provides decryption of the file that are matched to the checksum.txt encryption. Looking at the third if statement the script checks if the file would match to the checksum it will print the flag as indicated the “picoCTF” other wise print Error: Failed to decrypt ‘$file_name’. This flag is fake! Keep looking”

sha256sum files/* | grep 55b983afdd9d10718f1db3983459efc5cc3f5a66841e2651041e25dec3efd46a

ctf-player@pico-chall$ sha256sum files/* | grep 55b983afdd9d10718f1db3983459efc5cc3f5a66841e2651041e25dec3efd46a
55b983afdd9d10718f1db3983459efc5cc3f5a66841e2651041e25dec3efd46a  files/2cdcb2de
ctf-player@pico-chall$ 


./decrypt.sh files/2cdcb2de

55b983afdd9d10718f1db3983459efc5cc3f5a66841e2651041e25dec3efd46a  files/2cdcb2de
ctf-player@pico-chall$ ./decrypt.sh files/2cdcb2de

picoCTF{trust_but_verify_2cdcb2de}


ctf-player@pico-chall$ 
