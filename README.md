# Intro to Binary Exploitation

Mark Mossberg  
NU Hacks  
3/31/2016

Workshop Server: http://104.131.171.115:1337. Check the services.txt file for what
ports the services are running on.

## Setup

- gdbinit: Run `cat gdbinit >> ~/.gdbinit` to get gdb set up
- no_aslr.sh: When you're ready to locally exploit `vuln`, run this script
  which disables ASLR, so the buffer will be at the same address every
  run.

## Binaries

There are two binaries in this repo.

- easy: This is a simple binary that illustrates what buffer overflows are,
  but is not exploitable.
- vuln: This is the challenge binary, which has an exploitable stack buffer
  overflow.

## Services

These binaries are also hosted on the workshop server to simulate vulnerable
network services.

The easy and vuln services are exactly the same binaries, and ASLR is off
for vuln.

vuln2 is the same binary as vuln, except ASLR has been turned on. You will
need to modify your exploit to read the address of the buffer (which it
prints) and dynamically construct your exploit based on it before you send
it.

## Exploit Scripts

This repo includes some template exploit scripts for you to get started.

## Troubleshooting

If bash says it can't find the file when you try to execute them, it's
probably because these are 32 bit binaries, and you're on 64 bit Linux.
Check out http://stackoverflow.com/questions/2716702/no-such-file-or-directory-error-when-executing-a-binary


