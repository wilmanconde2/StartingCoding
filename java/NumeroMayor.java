import java.util.Scanner;

public class NumeroMayor {
    public static void main(String[] args) {
        var teclado = new Scanner(System.in);
        System.out.println("Proporciona el numero1:");
        var num1 = Integer.parseInt(teclado.nextLine());
        System.out.println("Proporciona el numero2:");
        var num2 = Integer.parseInt(teclado.nextLine());
        var mayor = (num1 > num2) ? ("El numero mayor es:\n" + num1) : ("E numero mayor es:\n" + num2);
        System.out.println(mayor);
    }
}
