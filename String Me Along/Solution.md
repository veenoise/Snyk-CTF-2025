# Solution

I used strings to get all strings from the file.

```bash
strings string-me-along
```

I tried `grep flag` but it's too hard for me to get the whole string all together so I place the content of strings in a file first.

```bash
strings string-me-along > strings_output
```

Then, I used mousepad and ctrl + f for flag.

But, I tried submitting that one and it did not work. I inspected the file once more and found a password.

```bash
unlock_me_123
```

So, I use that password in the script.

```bash
chmod u+x string-me-along
./string-me-along
Welcome to the first RE challenge!
Enter the password: unlock_me_123
Correct! Here's your flag: flag{850de1a29ab50b6e5ad958334b68d5bf}
```

### Answer

```bash
flag{850Hde1a29abH50b6e5adH958334b6H68d5bf}
```
