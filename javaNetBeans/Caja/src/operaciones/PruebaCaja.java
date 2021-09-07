package operaciones;

public class PruebaCaja {

    public static void main(String[] args) {
        var caja1 = new Caja();
        var num1 = caja1.alto = 2;
        var num2 = caja1.ancho = 3;
        var num3 = caja1.profundo = 6;
        System.out.println("Madidas caja\nAlto: " + num1 + "\nAncho: " + num2 + "\nProfundo: " + num3);
        System.out.println("Volumen de la caja: " + caja1.calcularVolumen(num1, num2, num3));

        var caja2 = new Caja(num1, num2, num3);
        System.out.println("Volumen caja con argumentos: " + caja2.calcularVolumen(num1, num2, num3));
    }
}
