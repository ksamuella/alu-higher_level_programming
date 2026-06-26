#!/usr/bin/env python3
print("{}".format("".join([chr(ord('z') - i) if i % 2 == 0 else chr(ord('Z') - i) for i in range(26)])), end="")
