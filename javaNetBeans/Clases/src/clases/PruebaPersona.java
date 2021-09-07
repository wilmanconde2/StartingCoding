package clases;

import java.util.Scanner;

public class PruebaPersona {
    public static void main(String[] args) {
        var teclado = new Scanner(System.in);
        var persona1 = new Persona();
        System.out.println("Ingresar nombre: ");
        persona1.setNombre(teclado.nextLine());
//       persona1.nombre = teclado.nextLine();
        System.out.println("Ingresar apellido: ");
        persona1.setApellido(teclado.nextLine());
//       persona1.apellido = teclado.nextLine();
        System.out.println("Ingresar edad: ");
        persona1.setEdad(teclado.nextInt());
//       persona1.edad = Integer.parseInt(teclado.nextLine());
        System.out.println(persona1.toString());


        var persona2 = new Persona();
        System.out.println(persona2.toString());
    }
}
