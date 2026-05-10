public class FunctionEngine {
    public static double f(double x) {
        return Math.pow(x,3) - 2* Math.pow(x,2) + x;
    }
    public static double derivative (double x ,double h) {
            return (f(x +h) - f(x)) / h ;
    }
    public static void main (String[] args) {
        double start = -2.0;
        double end = 3.0;
        double step = 0.1;
        double h = 0.0001;
        System.out.println("x\t\tf(x)\t\tf'(x)");
        System.out.println("-----------------------------------------------------------------");
        for (double x = start; x<= end ; x += step ) {
            double fx = f(x);
            double dfx = derivative(x,h);
System.out.printf("%.2f\t\t%.4f\t\t%.4f%n",x,fx,dfx);
        }
    }
    }

    
