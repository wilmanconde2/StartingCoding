package operaciones;

import java.util.Scanner;

public class PruebaAritmetica {
    public static void main(String[] args) {
        //
        var inicio = new Aritmetica();
        inicio.saludo();
        
        var operacion1 = new Aritmetica();
        var teclado = new Scanner(System.in);
        System.out.println("Ingresa entero1: ");
        var num1 = teclado.nextInt();
        System.out.println("Ingresa entero2: ");
        var num2 = teclado.nextInt();
        var cadena = " Resultado final";
        System.out.println("La suma de " + num1 + " + " + num2 + " es: " + 
                operacion1.sumarArgumentos(num1, num2, cadena));
        
        var operacion2 = new Aritmetica();
        operacion2.sumar(32, 4);
                
        System.out.println(new Aritmetica(2, 34));
        System.out.println(new Aritmetica().sumar(2.4, 6));
    }
}
