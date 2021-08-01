import java.util.Scanner;

public class Ejercicio2 {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        float notas = 0;
        System.out.println("Cantidad de notas a ingresar-> ");
        var cantidadNotas = teclado.nextInt();
        for(int i=1; i<=cantidadNotas; i++){
            System.out.println("Escriba nota # " + i);
            var nota = teclado.nextFloat();
            notas = notas + nota;
        }
        float promedio = (notas / cantidadNotas);
        System.out.println("Nota definitiva: " + promedio);
        if (promedio < 3){
            System.out.println("Pierde la materia");
        }else{
            System.out.println("Gana la materia");
        }
        teclado.close();
    }
}