#include <stdio.h>
#include <stdlib.h>

void vuln(void)
{
    int flag = 0;
    char name[32];
    printf("What's your name?: \n");
    fgets(name, 82, stdin);
    if (flag == 0) {
        printf("No overflow!\n");
        exit(0);
    } else {
        printf("Whoa, there was an overflow!\n");
        exit(1);
    }
}

int main(int argc, const char *argv[])
{
    setvbuf(stdout, NULL, _IONBF, 0);
    vuln();
    return 0;
}
