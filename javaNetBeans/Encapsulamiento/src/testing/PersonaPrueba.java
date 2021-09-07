package testing;

import domain.Persona;

public class PersonaPrueba {

    public static void main(String[] args) {
        var cliente1 = new Persona("Wilman", 750000, false);
        System.out.println("Cliente: " + cliente1.toString());
        cliente1.setNombre("Thiago");
        System.out.println("Cliente: " + cliente1.toString());
        var cliente2 = new Persona("Holmes", 250000, true);
        Imprimir(cliente2);
        var cliente3 = new Persona("Karla", 1000000, false);
        Imprimir(cliente3);

    }

    public static void Imprimir(Persona persona) {
        System.out.println("Cliente: " + persona.toString());
    }
}
