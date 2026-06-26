https://learn.cylabacademy.org/library/458

Ans :

https://prasanth26.medium.com/picoctf-perplexed-writeup-11a7e7296893

```c++
undefined8 check(char *param_1)

{
  size_t sVar1;
  undefined8 uVar2;
  size_t sVar3;
  char local_58 [36];
  uint local_34;
  uint local_30;
  undefined4 local_2c;
  int local_28;
  uint local_24;
  int local_20;
  int local_1c;
  
  sVar1 = strlen(param_1);
  if (sVar1 == 27) {
    local_58[0] = -0x1f;
    local_58[1] = -0x59;
    local_58[2] = '\x1e';
    local_58[3] = -8;
    local_58[4] = 'u';
    local_58[5] = '#';
    local_58[6] = '{';
    local_58[7] = 'a';
    local_58[8] = -0x47;
    local_58[9] = -99;
    local_58[10] = -4;
    local_58[0xb] = 'Z';
    local_58[0xc] = '[';
    local_58[0xd] = -0x21;
    local_58[0xe] = 'i';
    local_58[0xf] = 0xd2;
    local_58[0x10] = -2;
    local_58[0x11] = '\x1b';
    local_58[0x12] = -0x13;
    local_58[0x13] = -0xc;
    local_58[0x14] = -0x13;
    local_58[0x15] = 'g';
    local_58[0x16] = -0xc;
    local_1c = 0;
    local_20 = 0;
    local_2c = 0;
    for (local_24 = 0; local_24 < 0x17; local_24 = local_24 + 1) {
      for (local_28 = 0; local_28 < 8; local_28 = local_28 + 1) {
        if (local_20 == 0) {
          local_20 = 1;
        }
                local_30 = 1 << (7U - (char)local_28 & 31);
        local_34 = 1 << (7U - (char)local_20 & 31);;
        if (0 < (int)((int)param_1[local_1c] & local_34) !=
            0 < (int)((int)local_58[(int)local_24] & local_30)) {
          return 1;
        }
        local_20 = local_20 + 1;
        if (local_20 == 8) {
          local_20 = 0;
          local_1c = local_1c + 1;
        }
        sVar3 = (size_t)local_1c;
        sVar1 = strlen(param_1);
        if (sVar3 == sVar1) {
          return 0;
        }
      }
    }
    uVar2 = 0;
  }
  else {
    uVar2 = 1;
  }
  return uVar2;
}


```



 if (sVar1 == 27) 27 bit 


     local_58[0] = '\xe1';
    local_58[1] = '\xa7';
    local_58[2] = '\x1e';
    local_58[3] = '\xf8';
    local_58[4] = 0x75;
    local_58[5] = 0x23;
    local_58[6] = 0x7b;
    local_58[7] = 0x61;
    local_58[8] = '\xb9';
    local_58[9] = '\x9d';
    local_58[10] = '\xfc';
    local_58[0xb] = 0x5a;
    local_58[0xc] = 0x5b;
    local_58[0xd] = '\xdf';
    local_58[0xe] = 0x69;
    local_58[0xf] = 0xd2;
    local_58[0x10] = '\xfe';
    local_58[0x11] = 0x1b;
    local_58[0x12] = -0x13;
    local_58[0x13] = -0xc;
    local_58[0x14] = -0x13;
    local_58[0x15] = 0x67;
    local_58[0x16] = -0xc;
    local_1c = 0;
    local_20 = 0;
    local_2c = 0;

     "\xe1\xa7\x1e\xf8\x75\x23\x7b\x61\xb9\x9d\xfc\x5a\x5b\xdf\x69\xd2\xfe\x1b\xed\xf4\xed\x67\xf4", 