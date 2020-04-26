.PHONY = all clean

CC = gcc

SRCS := $(wildcard *.c)
BINS := $(SRCS:%.c=%)

all: ${BINS}

vuln1: vuln1.c
	${CC} -g -fno-stack-protector -z execstack -mpreferred-stack-boundary=2 -o $@ $<
	sudo chown root $@
	sudo chgrp root $@
	sudo chmod +s $@

%: %.c
	${CC} -g -fno-stack-protector -mpreferred-stack-boundary=2 -o $@ $<
	sudo chown root $@
	sudo chgrp root $@
	sudo chmod +s $@

clean:
	rm -rvf *.o ${BINS}
