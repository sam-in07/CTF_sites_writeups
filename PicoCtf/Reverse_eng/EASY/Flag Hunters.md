Link : https://learn.cylabacademy.org/library/472


Lyrics jump from verses to the refrain kind of like a subroutine call. There's a hidden refrain this program doesn't print by default. Can you get it to print it? There might be something in it for you.

The program's source code can be [downloaded here ](https://github.com/sam-in07/CTF_sites_writeups/blob/3ed8bee1b77342a55f40fb422c0a0f5aa627acc7/PicoCtf/Reverse_eng/EASY/Files/lyric-reader.py)



Soln : 


The clue comes from combining these two pieces:

1. User input is written back into the song
crowd = input('Crowd: ')
song_lines[lip] = 'Crowd: ' + crowd

Whatever you type becomes part of song_lines.

2. Song lines are later parsed as commands
for line in song_lines[lip].split(';'):

and then:

elif re.match(r"RETURN [0-9]+", line):
    lip = int(line.split()[1])

This means a semicolon (;) separates commands.



some_string;RETURN 0




No puzzle too dark, no challenge too hid.
With every exploit we trigger, every byte we decrypt,
We’re chasing that victory, and we’ll never quit.
Crowd: some_string
Pico warriors rising, puzzles laid bare,
Solving each challenge with precision and flair.
With unity and skill, flags we deliver,
The ether’s ours to conquer, picoCTF{70637h3r_f0r3v3r_a5202532}


picoCTF{70637h3r_f0r3v3r_a5202532}

