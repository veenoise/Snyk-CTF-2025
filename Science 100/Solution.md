# Solution

For this one I tried all the words visible in the output from top to bottom. 

```bash
┌──(kali㉿kali)-[~/Documents/CTF/Snyk]
└─$ nc challenge.ctf.games 30784

Welcome to Robco Industries (TM) Termlink
                                                                                                                    
>SET TERMINAL/INQUIRE                                                                                               
                                                                                                                    
RIT-V300                                                                                                            
                                                                                                                    
>SET FILE/PROTECTION=OWNER:RWED ACCOUNTS.F                                                                          
>SET HALT RESTART/MAINT                                                                                             
0xF4F0  {_%+}.,]$$/|  0xF5F0  .{!|/=}|${-}
0xF4FC  =;#[;*!}-,.?  0xF5FC  $][]*-@;,&])                                                                          
0xF508  :[(/^SUNTAN:  0xF608  =!#_]}[}.?=]                                                                          
0xF514  =^{{(:<_]?%/  0xF614  }DEVOTE}$>|_                                                                          
0xF520  |@$:>^;,;@]^  0xF620  >(#?{*%-/{;_                                                                          
0xF52C  *{:*+.|?$#_>  0xF62C  _^:]/.*&<]?&                                                                          
0xF538  {@@!FINGER>?  0xF638  |*:-$^&#@&$)                                                                          
0xF544  [.+%{@]:[]&&  0xF644  [BULLET;;:_]                                                                          
0xF550  (/__?);--{{|  0xF650  ^(?%(-)!?%).                                                                          
0xF55C  <%<*/&{(,]]>  0xF65C  ?(|]]@_@_&-)                                                                          
0xF568  <&@();@@*,>|  0xF668  {{;@[!>?=)?/                                                                          
0xF574  ]]+_-:<=<>-|  0xF674  .=|SUBWAY$&@                                                                          
0xF580  ?<=ACTIVE;|:  0xF680  ]/-${%$,,#=!                                                                          
0xF58C  @;-^()*:&%|@  0xF68C  [$&^#+*}<;?]                                                                          
0xF598  @$)=&.())*;@  0xF698  ?&_[?<]?&}&_                                                                          
0xF5A4  AFFECT)|#;#[  0xF6A4  STROLL]&,,?!                                                                          
[!] ATTEMPTS REMAINING: 4
> suntan                                                                                                            
ENTRY DENIED. LIKENESS: 0/6
[!] ATTEMPTS REMAINING: 3
> finger                                                                                                            
ENTRY DENIED. LIKENESS: 0/6
[!] ATTEMPTS REMAINING: 2
> active                                                                                                            
ENTRY DENIED. LIKENESS: 1/6
[!] ATTEMPTS REMAINING: 1
> affect                                                                                                            

[!] ACCESS GRANTED                                                                                                  
                                                                                                                    
Robco Industries Termlink (TM) Mail Protocol Initiated                                                              
                                                                                                                    
User: j.hammond@robcoindustries.org                                                                                 
                                                                                                                    
INBOX                                                                                                               
1) h.hacks@robcoindustries.org SUBJ: new CTF game idea                                                              
2) flag.txt                                                                                                         
3) Paella recipe                                                                                                    
                                                                                                                    

Select an option (1, 2, or 3): 2                                                                                    

flag.txt                                                                                                            
flag{89e575e7272b07a1d33e41e3647b3826}                                                                              
                                                                                                                    

Select an option (1, 2, or 3):  
```

### Answer

```bash
flag{89e575e7272b07a1d33e41e3647b3826}                                                                             
```


