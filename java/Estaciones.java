import java.util.Scanner;

public class Estaciones {
    public static void main(String[] args) {
        var teclado = new Scanner(System.in);
        System.out.println("Ingresa mes para saber estación:");
        var mes = Integer.parseInt(teclado.nextLine());
        var estacion = "Fuera de rango";

        switch (mes) {
            case 1: case 2: case 12:
                estacion = "Invierno";
                break;
            case 3: case 4: case 5:
                estacion = "Primavera";
                break;
            case 6: case 7: case 8:
                estacion = "Verano";
                break;
            case 9: case 10: case 11:
                estacion = "Otoño";
                break;
        }
        System.out.println("Estación = " + estacion);
    }
}
