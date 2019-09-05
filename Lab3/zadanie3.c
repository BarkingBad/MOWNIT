#include <stdio.h>
#include <stdlib.h>
#include <gsl/gsl_blas.h>
#include <gsl/gsl_blas_types.h>
#include <gsl/gsl_vector.h>
#include <time.h>
#include <sys/time.h>
#include <sys/types.h>
#include <stdint.h>

uint64_t naive_multiplication(int n) {
    double ** A = (double **) malloc (n * sizeof(double *));
    double ** B = (double **) malloc (n * sizeof(double *));
    double ** C = (double **) malloc (n * sizeof(double *));
    for(int i = 0; i < n; i++) {
        A[i] = (double *) malloc (n * sizeof(double));
        B[i] = (double *) malloc (n * sizeof(double));
        C[i] = (double *) calloc (n, sizeof(double));
    }

    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            A[i][j] = i + j + 2;
            B[i][j] = i + j + 2;
        }
    }
    struct timespec start, end;
    uint64_t res;

    clock_gettime(0, &start);
    for(int j = 0; j < n; j++) {
        for(int k = 0; k < n; k++) {
            for(int i = 0; i < n; i++) {
                C[i][j] += A[i][k]*B[k][j];
            }
        }
    }
    clock_gettime(0, &end);
    res = (end.tv_sec - start.tv_sec) * 1000000 + (end.tv_nsec - start.tv_nsec) / 1000;


    for(int i = 0; i < n; i++) {
        free(A[i]);
        free(B[i]);
        free(C[i]);
    }
    free(A);
    free(B);
    free(C);
    return res;
}

uint64_t better_multiplication(int n) {
    double ** A = (double **) malloc (n * sizeof(double *));
    double ** B = (double **) malloc (n * sizeof(double *));
    double ** C = (double **) malloc (n * sizeof(double *));
    for(int i = 0; i < n; i++) {
        A[i] = (double *) malloc (n * sizeof(double));
        B[i] = (double *) malloc (n * sizeof(double));
        C[i] = (double *) calloc (n, sizeof(double));
    }

    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            A[i][j] = i + j + 2;
            B[i][j] = i + j + 2;
        }
    }
    struct timespec start, end;
    uint64_t res;

    clock_gettime(0, &start);
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            for(int k = 0; k < n; k++) {
                C[i][j] += A[i][k]*B[k][j];
            }
        }
    }
    clock_gettime(0, &end);
    res = (end.tv_sec - start.tv_sec) * 1000000 + (end.tv_nsec - start.tv_nsec) / 1000;
    

    for(int i = 0; i < n; i++) {
        free(A[i]);
        free(B[i]);
        free(C[i]);
    }
    free(A);
    free(B);
    free(C);
    return res;
}

uint64_t dgemm(int n) {
    gsl_matrix * matrix1, * matrix2, * result;
    int i, j;
    struct timespec start, end;
    uint64_t res;
    matrix1 = gsl_matrix_alloc(n, n);
    matrix2 = gsl_matrix_alloc(n, n);
    result = gsl_matrix_alloc(n, n);
    for(i = 0; i < n; i++) {
        for(j = 0; j < n; j++) {
            gsl_matrix_set(matrix1, i, j, (double) i+j+2);
            gsl_matrix_set(matrix2, i, j, (double) i+j+2);
        }
    }
    clock_gettime(0, &start);
    gsl_blas_dgemm(CblasNoTrans, CblasNoTrans, 1.0, matrix1, matrix2, 0.0, result);
    clock_gettime(0, &end);
    res = (end.tv_sec - start.tv_sec) * 1000000 + (end.tv_nsec - start.tv_nsec) / 1000;
    gsl_matrix_free(result);
    gsl_matrix_free(matrix1);
    gsl_matrix_free(matrix2);
    return res;
}

int main() {
    uint64_t result;
    FILE * file;
    file = fopen("./csv.csv", "w+");
    fprintf(file, "N;TYPE;TIME\n");



    int n = 100;
    for(int j=0; j<=9; j++) {
        for(int i=0; i<10; i++) {
            result = naive_multiplication(n);
            fprintf(file, "%d;naive;%jd\n", n, result);
        }
        for(int i=0; i<10; i++) {
            result = better_multiplication(n);
            fprintf(file, "%d;better;%jd\n", n, result);
        }
        for(int i=0; i<10; i++) {
            result = dgemm(n);
            fprintf(file, "%d;blas;%jd\n", n, result);
        }
        n += 100;
    }

   fclose(file);
   return 0;
}