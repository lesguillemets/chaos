#include <stdio.h>
#include <math.h>

int main(void){
	
	double x0 = 0.1, y0 = 0, x1,y1; //variables
	double a,b;   //parameters
	int i;
	FILE *fp;

	if ((fp = fopen("tsubasa_c_-1.77_0.989.dat","w")) == NULL) {
		printf("error\n");

	} else {
/*		printf("input a\n>");
		a = scanf("%lf",&a);
		printf("input b\n>");
		b = scanf("%lf",&b);
*/
		a = -1.77;
		b = 0.989;
		for(i=0;i<50000;i++){
			x1 = y0 + a*x0 - 5.0/(x0*x0 +1) + 6.0 + 0.2*exp(-y0*y0);
			y1 = -b*x0;
			fprintf(fp,"%lf\t%lf\n",x1+y1,x1-y1);
			x0 = x1;
			y0 = y1;
			}
	}

	fclose(fp);
	return 0;
	}




