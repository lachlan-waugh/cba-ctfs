#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NAME_LEN 0x14

typedef struct user {
    char name[NAME_LEN];
    void (*fptr)(void);
} * user_t;

user_t users[100];
int n_users;

void win(void) {
    printf("You win!\n");
    exit(0);
}

void lose(void) {
    printf("You lose!\n");
}

void flush(void) {
    char ch;
    while ((ch = getchar()) && ch != EOF && ch != '\n');
}

user_t get_user(void) {
    int number;
    char buffer[4];

    printf("which user?\n$ ");
    number = atoi(fgets(buffer, 4, stdin));
    if (number < 0 || number >= n_users || users[number] == NULL) {
        printf("invalid. that user isn't allocated.\n");
        exit(0);
    }

    return users[number];
}

void create_user(void) {
    user_t new_user = malloc(24);
    if (new_user == NULL) {
        fprintf(stderr, "oh no, malloc failed\n");
        exit(1);
    }

    printf("whats the name\n$ ");
    fgets(new_user->name, NAME_LEN, stdin);

    new_user->fptr = lose;

    printf("okay, you're user #%d\n", n_users);
    users[n_users] = new_user;
    ++n_users;
}

void delete_user(void) {
    user_t user = get_user();
    free(user);
}

void set_name(void) {
    user_t user = get_user();
    printf("what's your name\n$ ");
    fgets(user->name, NAME_LEN, stdin);
}

void print_name(void) {
    user_t user = get_user();
    printf("name is: %s\n", user->name);
}

void try(void) {
    user_t user = get_user();
    user->fptr();
}

int menu(void) {
    printf("[C]reate\n");
    printf("[D]elete\n");
    printf("[S]et name\n");
    printf("[P]rint name\n");
    printf("[T]ry your luck\n");
    printf("[Q]uit\n");
    printf("$ ");

    char c = getchar();
    switch (c) {
    case EOF:
    case 'q':
    case 'Q':
        return 0;
    case 'c':
    case 'C':
        flush();
        create_user();
        break;
    case 'd':
    case 'D':
        flush();
        delete_user();
        break;
    case 's':
    case 'S':
        flush();
        set_name();
        break;
    case 'p':
    case 'P':
        flush();
        print_name();
        break;
    case 't':
    case 'T':
        flush();
        try();
        break;
    default:
        printf("\n");
        break;
    }

    return 1;
}

int main(void) { 
    setbuf(stdout, NULL);
    puts("welcome to user login service");
    do {} while (menu());
    return 0;
}
