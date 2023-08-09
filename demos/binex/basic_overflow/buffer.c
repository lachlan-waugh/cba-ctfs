#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int fail = 0;

int main(void) {
  char input[40];
  int success = 0;

  printf("Enter your password: ");
  fgets(input, 100, stdin);

  if (strcmp("secretpassword123", input) == 0) {
    fail = success = 1;
  }

  if (success) {
    printf("-----------------------\n");
    printf("-- LOGIN SUCCESSFULL --\n");
    printf("-----------------------\n");

    if (fail) {
      printf("Try to login WITHOUT entering the correct password...\n");
    } else {
      printf("-----------------------\n");
      printf("--    LEET HACKER    --\n");
      printf("-----------------------\n");
    }
  } else {
    printf("-----------------------\n");
    printf("--    LOGIN FAILED   --\n");
    printf("-----------------------\n");
  }

  return 0;
}
