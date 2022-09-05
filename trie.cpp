#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>
#include <ctype.h>
#define NUM_CHAR 256

typedef struct trienode{
    bool terminal;//whether the node is a terminal node
    struct trienode *children[NUM_CHAR];


} trienode;

trienode *createnode(){
    trienode *newnode = malloc(sizeof(*newnode));

}


int main(){

    return 0;
}