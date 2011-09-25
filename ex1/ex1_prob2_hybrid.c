#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#define MAXITER 50
#define A 0
#define B 3

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

	int useNewton=1;
	int a = A;
	int b = B;
	int u = func(a);
	int v = func(b);


	printf("i 	  	x		f(x)\n");

	for(iter=0; iter<=MAXITER; iter++){
		if(useNewton==1){
			printf("%d  	%10.6f	%12.6f\n",iter,x,fx);
			fp=func_prime(x);
			if(fabs(fp) <= mindelta){
				printf("Error: derivative too small\n");
				exit(1);
			}
			d=fx/fp;
			if(fabs(d) <= eps){
				printf("Found root at %f\n", x);
				break;
			}
			if((x-d)<=B && (x-d)>=A){
				x=x-d;
				fx=func(x);
			}
			else{
				useNewton=0;
				iter-=1;
			}
		} else {
			if(b-a <= mindelta) break;
			x = 0.5*(a+b);

			fx = func(x);
			if(fabs(fx) <= eps) break;
			if(fx*u < 0) {
				b = x;
				v = fx;
			}
			else {
				a = x;
				u = fx;
			}
			useNewton=1;
		}
	}
}

double func(double x){ return x*x*x-x-5; }	
double func_prime(double x){ return 3*x*x-1; }
