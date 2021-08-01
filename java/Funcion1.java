public class Funcion1 {
    public static void mensaje(){               // No recibe ni retorna datos
        System.out.println("Hola Mundo");
    }
    public static void sumar(int a, int b, String c){       // Recibe pero no retorna datos
        var resultado = a + b;
        System.out.println(c + resultado);
    }
    public static double multiplicacion(double a, double b){        // Recibe y retorna datos
        return a * b;
    }
    public static void main(String[] args) {
        mensaje();
        mensaje();
        var a = 3;
        var b = 5;
        sumar(a, b, "La suma de " + a + " + " + b + " es: ");
        sumar(2, 7, "La suma de 2 + 7 es: ");
        var res = multiplicacion(a, b);
        System.out.println("La multiplicacion de " + a + " * " + b + " es " + res);

    }
}
