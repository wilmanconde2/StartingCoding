import java.util.Scanner;

public class Rectangulo {
    public static double area(double a, double b){
        return (a * b);
    }
    public static double perimetro(double a, double b){
        return ((a + b)*2);
    }
    public static void main(String[] args) {
        var teclado = new Scanner(System.in);
        System.out.println("Ingresa alto del rectángulo: ");
        var alto = teclado.nextDouble();
        System.out.println("Ingresa ancho del rectángulo: ");
        var ancho = teclado.nextDouble();
        System.out.println("El area del rectángulo es: " + area(alto, ancho));
        System.out.println("EL perímetro del rectángulo es: " + perimetro(alto, ancho));

    }
}
