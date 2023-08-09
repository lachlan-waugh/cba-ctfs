#include <stdio.h>
#include <stdlib.h>

char str[] = "/bin/sh";
void deprecated() {
    system("/bin/whoami");
}

// void win(void) {
//   system("/bin/sh");
// }

void pwn(void) {
    char input[16];
    printf("Here are some helpful pointers &win=%p, &str=%p, &input=%p\n", &win, &str, &input);
    puts("Hello\n");

    fgets(input, 1337, stdin);
}

int main() {
    pwn();
    puts("Bye!\n");
}
