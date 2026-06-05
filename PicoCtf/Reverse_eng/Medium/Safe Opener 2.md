Link : https://learn.cylabacademy.org/library/375

What can you do with this file?

I forgot the key to my safe but this file(PicoCtf/Reverse_eng/Medium/Files/SafeOpener.class)
is supposed to help me with retrieving the lost key. Can you help me unlock my safe?

Soln : 

Open on Ghidra decompiler eash 3 file on 3rd one "openSafe_java.lang.String_boolean" 
on decompile part code u find flag :

  bVar2 = param1.equals("**picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_0e57c117}**");
  if (bVar2) {
    pPVar1 = System.out;
    pPVar1.println("Sesame open");
    return true;
  }

Alternate way :

┌──(samin㉿kali)-[~/…/PicoCtf/Reverse_eng/Medium/Files]
└─$ strings -t x SafeOpener.class | grep picoCTF
    31d ,picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_0e57c117}
                                                                                                                                                                                                                                           
┌──(samin㉿kali)-[~/…/PicoCtf/Reverse_eng/Medium/Files]
└─$ 


