import java.util.Scanner;

public class TiposDatos {
    public static void main(String[] args) {
        
        boolean c, d;
        c = false;
        d = true;
        var f = false;
        var t = true;
        System.out.println(f + "\n" + t);
        System.out.println("Booleanos\n" + c + ", " + d);

        var x = 127384;
        var cadena = "Wilman Conde";
        System.out.println(x + "\n" + cadena);

        Scanner entrada = new Scanner(System.in);
        System.out.println("Proporciona el titulo");
        var titulo = entrada.nextLine();
        System.out.println("Proporciona el autor");
        var autor = entrada.nextLine();
        System.out.println(titulo + " fue escrito por "+ autor);
        System.out.println("Edad actual");
        var edad = entrada.nextInt();
        System.out.println(edad);
        if (edad > 18){
            System.out.println("Mayor de edad");
        }
        else{
            System.out.println("No puedes ingresar");
        }
        entrada.close();        
    }
}
