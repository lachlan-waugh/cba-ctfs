CC         := gcc
CFLAGS     := -ggdb -O0 -std=gnu99 -m32 -z relro -z now
INTEL_ASM  := -masm=intel

all: clean build

build:
	$(CC) $(INTEL_ASM) $(CFLAGS) -o chal chal.c

clean:
	rm -f chal
