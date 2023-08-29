#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int *bubbleSort(int *arr, int n);
void swap (int *first, int *second);
void printArray(int *arr, int n);
int *newRandArray(int n);
bool isSorted(int *arr, int n);

// takes arr, an array of n integers of size n
// returns a pointer to the in-place sorted array
// uses the bubble sort algorithm
int *bubbleSort(int *arr, int n) {
    for (int i = 0; i < n; i++) {
        bool swapped = false;
        for (int j = 0; j < n - 1; j++) {
            if (arr[j] > arr[i]) {
                swap(&arr[j], &arr[j + 1]);
                swapped = true;
            }
        }
        if (!swapped) break;
    }
    return arr;
}

void swap (int *first, int *second) {
    int temp = *first;
    *first = *second;
    *second = temp;
}

int main(void) {
    int n = 100;
    int *arr = newRandArray(n);
    printf("before sorting, arr is ");
    if (isSorted(arr, n)) printf("SORTED\n");
    else printf("NOT SORTED\n");
    arr = bubbleSort(arr, n);
    printf("after sorting, arr is ");
    if (isSorted(arr, n)) printf("SORTED\n");
    else printf("NOT SORTED\n");
    free(arr);
}

void printArray(int *arr, int n) {
    for (int i = 0; i < n; i++) printf("%d, ", arr[i]);
}

int *newRandArray(int n) {
    int *ptr = malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) ptr[i] = rand() % n;
    return ptr;
}

bool isSorted(int *arr, int n) {
    if (n == 0) return true;
    int curr = arr[0];
    for (int i = 0; i < n; i++) {
        if (arr[i] < curr) {printf("arr[i] is %d, arr[i-1] is %d\n", arr[i], arr[i-1]);return false;}
        
        curr = arr[i];
    }
    return true;
}