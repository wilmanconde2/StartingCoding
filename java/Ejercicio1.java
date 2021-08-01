import java.util.Scanner;

public class Ejercicio1 {
    public static void main(String[] args) {
        var teclado = new Scanner(System.in);       // crea objeto TECLADO (<nombre>) para usar el scanner
        System.out.println("Ingresa tu edad");          // imprime en pantalla
        var edad = teclado.nextInt();                   // se declara variable para ingresar por teclado
        System.out.println("Tienes " + edad + " años\nEquivalen a " + (edad * 12) + " meses o " 
                            + (edad * 24 * 365) + " horas.");
        teclado.close();
    }
}
