# Solution

I tried using strings but I did not see a good entry of exploit. Since this is an executable, I figured I would patch it so I can get win condition every time. 

I used IDA Free for this.

I analyzed the decompiled code and look for main function. I noticed the conditional `jnz`. Based on a youtube video the byte for this is 75 and I need to change it to 74 for it to be `jz`. After patching the file was now printing the win condition.

### Answer

```bash
flag{c54315482531c11a76aeaa828e43807c}
```
