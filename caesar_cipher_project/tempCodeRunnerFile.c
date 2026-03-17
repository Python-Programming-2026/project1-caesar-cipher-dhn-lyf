#include <stdio.h>

void swap(int *a,int *b){
    int c = *a;
    *a = *b;
    *b = c;
}

void qSort(int a[], int p, int r){
    if(p<r){
        int q = partition(a[], p, r);
        qSort(a[], p, q-1);
        qSort(a[], q+1, r);
    }
}

int partition(a[], int p, int r){
    int i = p;
    int j = r+1;
    int x = a[p];
    while(i<j){
        while(a[i]<=x && i<j) i++;
        while(a[j]>=x && i<j) j--;
        if(i<j){
            swap(&a[i], &a[j]);
        }
    }
    a[p] = a[j];
    a[j] = x;
    return j;
}

int main() {
    int arr[] = {3, 1, 4, 1, 5, 9, 2, 6};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    qSort(arr, 0, n - 1);
    
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    
    return 0;
}