#include <stdio.h>

void vuln(void)
{
    char name[64];
    printf("%p What's your name?: \n", name);
    fgets(name, 0x64, stdin);
    printf("Hello, %s\n", name);
}

int main(int argc, const char *argv[])
{
    setvbuf(stdout, NULL, _IONBF, 0);
    vuln();
    return 0;
}
