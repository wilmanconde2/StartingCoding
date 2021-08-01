import java.util.Scanner;

public class TiendaLibros {

    public static void main(String[] args) {
        // Se solicita capturar la siguiente información de una tienda de libros:
        // nombre (String)
        // id (int)
        // precio (double)
        // envioGratuito (boolean)

        // <nombre> #<id>
        // Precio: <simbolo><precio>
        // Envio Gratuito: <envioGratuito>

        Scanner teclado = new Scanner(System.in);
        System.out.println("Proporciona el nombre del libro:");
        var nombre = teclado.nextLine();
        System.out.println("Proporciona el Id del libro:");
        var id = teclado.nextInt();
        System.out.println("Proporciona el precio del libro:");
        var precio = teclado.nextDouble();
        System.out.println("Proporciona envío gratuito:");
        var envio = teclado.nextBoolean();

        System.out.println(nombre + " #" + id);
        System.out.println("Precio: $" + precio);
        System.out.println("Envío gratuito: " + envio);
    }
}
