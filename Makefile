OUT = vuln easy
CFLAGS += -m32 -fno-stack-protector

all: exec

exec: $(OUT)
	execstack -s $(OUT)

clean:
	rm -f $(OUT)
