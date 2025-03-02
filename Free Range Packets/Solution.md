# Solution

I used wireshark to look at the packets. I have no idea about bluetooth but upon closer inspection I noticed that the capture file is simply a communication between two devices. I tried to ctrl + f and { to search for strings and I was right. The bluetooth capture file captured the communication between the devices. I sorted the packets by Protocol as I only need the `L2CAP` and read the payload one by one.

### Answer

```bash
flag{b5be72ab7e0254c056ffb57a0db124ce}
```

