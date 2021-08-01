import java.util.Scanner;

public class Calculadora {
    public static double sumar(double a, double b){
        return (a + b);
    }
    public static double restar(double a, double b){
        return (a - b);
    }
    public static double multiplicar(double a, double b){
        return (a * b);
    }
    public static Object dividir(double a, double b){
        return (b == 0) ? "No se puede dividir por 0" : (a / b);
    }
    public static double numeros(){
        Scanner teclado = new Scanner(System.in);
        System.out.println("Ingrese numero:");
        return teclado.nextDouble();
    }
    public static void main(String[] args) {
        var teclado = new Scanner(System.in);
        System.out.println("\nMenu calculadora\n1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Salir");
        var opcion = teclado.nextInt();
        while (opcion > 0 && opcion <=5){
            if (opcion == 5){
                System.out.println("Gracias");
                Runtime.getRuntime().exit(0);
            }
            double a = numeros();
            double b = numeros();
            switch (opcion) {
                case 1:
                System.out.println("La suma de " + a + " + " + b + " es: " + sumar(a, b));
                    break;
                case 2:
                System.out.println("La resta de " + a + " - " + b + " es: " + restar(a, b));
                    break;
                case 3:
                System.out.println("La multiplicacion de " + a + " * " + b + " es: " + multiplicar(a, b));
                    break;
                case 4:
                System.out.println("La division de " + a + " / " + b + " es: " + dividir(a, b));
                    break;
                }
            System.out.println("\nMenu calculadora\n1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Salir");
            opcion = teclado.nextInt();
            }
        teclado.close();
        }
    }