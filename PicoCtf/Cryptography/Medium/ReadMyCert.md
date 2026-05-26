Problem : https://learn.cylabacademy.org/library/367
How about we take you on an adventure on exploring certificate signing requests

Take a look at this CSR file here.
file :PicoCtf/Cryptography/flagelemts/ReadMyCert/readmycert.csr


Soln :   

base 64 

 ┌──(samin㉿kali)-[~/…/PicoCtf/Cryptography/flagelemts/ReadMyCert]
└─$ ls
readmycert.csr
                                                                                                                                                                                                                                           
┌──(samin㉿kali)-[~/…/PicoCtf/Cryptography/flagelemts/ReadMyCert]
└─$ file readmycert.csr
readmycert.csr: PEM certificate request
                                                                                                                                                                                                                                            
┌──(samin㉿kali)-[~/…/PicoCtf/Cryptography/flagelemts/ReadMyCert]
└─$ cat readmycert.csr                                                                                             
-----BEGIN CERTIFICATE REQUEST-----
MIICpzCCAY8CAQAwPDEmMCQGA1UEAwwdcGljb0NURntyZWFkX215Y2VydF81YWVi
MGQ0Zn0xEjAQBgNVBCkMCWN0ZlBsYXllcjCCASIwDQYJKoZIhvcNAQEBBQADggEP
ADCCAQoCggEBAMCkf11rmV8rgqPvC2ZiPA6W+5RfOTwU6u3WpGvLA+2YFzocBPut
aATTxTPB+uaN2ZN3Z5J2CTFGmPzI4sUQfSqhZGuAqbfMyDDR8pRswmIYVJ6s0Apc
Toi7H8m3IShSbeE0pZUSIJpbK1a7V6lJqgwFMDI1qrgNhGgZaMA/l+d2J0vC3EYd
AijwSs8APcp6woWbFGYwdw5KaBsjn23oVz2G4h3/TmdB5g5e6Oq+kgi38NEpRDS0
ylXo9mUko3FqS4I6y9gOtDEI4uZaCJZuXHDmBpqZ04MfXbIVlHjF9NMOjDvXLonN
650oaANBm4bhBlgid0Fx48Z36tbtAVivZEcCAwEAAaAmMCQGCSqGSIb3DQEJDjEX
MBUwEwYDVR0lBAwwCgYIKwYBBQUHAwIwDQYJKoZIhvcNAQELBQADggEBAHZx6h9r
G/SE7RCoX6ndk5BOJprRiHpxOqPLAWcDyKHfStln0/HcQZzIrRVRsmoHiOmch+md
PBA1b+M5aj+3BWtPR9jOY4vht+ZmHAKa0WfQxwb2dBxsRPKTTDea0wN2u8BHLlSM
PbWPNuz+TKySL41xfwFuM4VN/ywn58GTvdb7HXgwNZCGgo2N1WhRq/dBMiagXMah
yb6gX4erugCu61T5tyD80hgsNBjaqyIdy/whRfC/Pmn3QHmdkqB5ZCPezwb2OLm4
5RDGv3WOB5q0BofoUGhVq757QE8qhL3oTvV2WlLoi3YWaZkJMCeR3vnH92cKC1Ov
FxdQuLOH8GMvl7U=
-----END CERTIFICATE REQUEST-----
                                                                                                                                                                                                                                            
┌──(samin㉿kali)-[~/…/PicoCtf/Cryptography/flagelemts/ReadMyCert]
└─$ openssl req -in readmycert.csr -noout -text
Certificate Request:
    Data:
        Version: 1 (0x0)
        Subject: CN=picoCTF{read_mycert_5aeb0d4f}, name=ctfPlayer
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (2048 bit)
                Modulus:
                    00:c0:a4:7f:5d:6b:99:5f:2b:82:a3:ef:0b:66:62:
                    3c:0e:96:fb:94:5f:39:3c:14:ea:ed:d6:a4:6b:cb:
                    03:ed:98:17:3a:1c:04:fb:ad:68:04:d3:c5:33:c1:
                    fa:e6:8d:d9:93:77:67:92:76:09:31:46:98:fc:c8:
                    e2:c5:10:7d:2a:a1:64:6b:80:a9:b7:cc:c8:30:d1:
                    f2:94:6c:c2:62:18:54:9e:ac:d0:0a:5c:4e:88:bb:
                    1f:c9:b7:21:28:52:6d:e1:34:a5:95:12:20:9a:5b:
                    2b:56:bb:57:a9:49:aa:0c:05:30:32:35:aa:b8:0d:
                    84:68:19:68:c0:3f:97:e7:76:27:4b:c2:dc:46:1d:
                    02:28:f0:4a:cf:00:3d:ca:7a:c2:85:9b:14:66:30:
                    77:0e:4a:68:1b:23:9f:6d:e8:57:3d:86:e2:1d:ff:
                    4e:67:41:e6:0e:5e:e8:ea:be:92:08:b7:f0:d1:29:
                    44:34:b4:ca:55:e8:f6:65:24:a3:71:6a:4b:82:3a:
                    cb:d8:0e:b4:31:08:e2:e6:5a:08:96:6e:5c:70:e6:
                    06:9a:99:d3:83:1f:5d:b2:15:94:78:c5:f4:d3:0e:
                    8c:3b:d7:2e:89:cd:eb:9d:28:68:03:41:9b:86:e1:
                    06:58:22:77:41:71:e3:c6:77:ea:d6:ed:01:58:af:
                    64:47
                Exponent: 65537 (0x10001)






**    Flag/Option: openssl
        This is the command-line tool used to perform various cryptographic operations using the OpenSSL library.

    Flag/Option: req
        It is a subcommand of OpenSSL specifically used for working with certificate requests, including CSRs.

    Flag/Option: -in your_csr_file.csr
        This flag specifies the input file for the CSR. Replace your_csr_file.csr with the actual path and filename of your CSR file.

    Flag/Option: -noout
        This flag instructs OpenSSL not to output the actual certificate but only display the CSR’s text representation. It prevents generating any output other than the textual information.

    Flag/Option: -text
        This flag tells OpenSSL to display the CSR details in a human-readable format. It provides a comprehensive view of the CSR’s contents, including the subject’s distinguished name (DN), public key information, and any other attributes included in the request.**