import java.util.Scanner;

public class Conversion {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        System.out.println("Ingresa edad");
        var edad = teclado.nextLine();
        var edad1 = Integer.parseInt(edad);     // variable modificada a int
        System.out.println("La edad " + edad + " +" +" 8, es igual a " + (edad1 + 8));         // variable ingresada como string
        System.out.println("Ingresa valor de pi");
        var pi = Double.parseDouble(teclado.nextLine());       // modifica string a double
        System.out.println("Súmele algún valor a pi");
        var num = teclado.nextInt();
        System.out.println("Pi "+ pi + num + " es igual a " + (pi + num));
    }
}
