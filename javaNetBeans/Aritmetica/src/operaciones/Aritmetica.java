package operaciones;

public class Aritmetica {

    //atributos de la clase
    int a;
    int b;
    double c;
    double d;
    

    //constructor vacio
    public Aritmetica() {
    }

    //recarga de constructores
    public Aritmetica(int a, int b) {
        System.out.println("Constructor con argumentos");
        System.out.println("Variable entero1: " + a);
        System.out.println("Variable entero2: " + b);
    }

    public Aritmetica(double c, double d) {
        System.out.println("Constructor con argumentos");
        System.out.println("Variable double1: " + a);
        System.out.println("Variable double2: " + b);
    }

    //metodo no recibe ni retorna datos
    public void saludo() {
        System.out.println("Calculadora");
    }

    //metodo recibe pero no retorna datos
    public void sumar(int a, int b) {
        System.out.println("La suma de " + a + " + " + b + " es: " + (a + b));
    }

    //metodo recibe y retorna datos
    public double sumar(double a, double b) {
        System.out.println("Suma de:\nDouble1: " + a + "\nDouble2: " + b);
        return a + b;
    }

    //metodo recibe y retorna datos
    public Object sumarArgumentos(float a, float b, String c) {
        return (a + b + c);
    }
}
