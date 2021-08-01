import java.util.Scanner;

public class Calificaciones {
    public static void main(String[] args) {
        var teclado = new Scanner(System.in);
        System.out.println("Ingresa valor para nota final:");
        var nota = Double.parseDouble(teclado.nextLine());
        var notaFinal = "Valor desconocido";
        if (nota >= 9 && nota <= 10){
            notaFinal = "A";
        } else if (nota >= 8 && nota <= 9){
            notaFinal = "B";
        } else if (nota >= 7 && nota < 8){
            notaFinal = "C";
        } else if (nota >= 6 && nota < 7){
            notaFinal = "D";
        } else if (nota >= 0 && nota < 6){
            notaFinal = "F";
        }
        System.out.println("Nota: " + notaFinal);
    }
}
