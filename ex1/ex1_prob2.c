#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#define MAXITER 50

double func(double x);
double func_prime(double x);
int main(){
	double x = 0.57735;
	double mindelta = 0.00000001;
	double eps = 0.000001;
	double d = 0;
	int iter=0;
	double fp=1;
	printf("Hello!\n");
	double fx = func(x);
	printf("i 	  	x		f(x)\n");

	for(iter=0; iter<=MAXITER; iter++){
		printf("%d  	%10.6f	%12.6f\n",iter,x,fx);
		fp=func_prime(x);
		if(fabs(fp) <= mindelta){
			printf("Error: derivative too small\n");
			exit(1);
		}
		d=fx/fp;
		x=x-d;
		if(fabs(d) <= eps){
			printf("Found root at %f\n", x);
			break;
		}
		fx=func(x);
	}
}

double func(double x){ return x*x*x-x-5; }	
double func_prime(double x){ return 3*x*x-1; }
