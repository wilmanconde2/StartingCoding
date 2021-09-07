package testing;

import domain.Cliente;
import domain.Empleado;
import java.util.Date;

public class Testing {

    public static void main(String[] args) {

        var empleado1 = new Empleado("Wilman", 100000);
        Imprimir(empleado1);
        empleado1.setNombre("Andres");
        empleado1.setEdad(20);
        empleado1.setGenero('m');
        empleado1.setDireccion("calle ramon");
        Imprimir(empleado1);
        System.out.println("");
        
        var empleado2 = new Empleado("Luisa", 150000);
        Imprimir(empleado2);
        System.out.println("");
       
        var cliente1 = new Cliente(new Date(), true, "Cami", 'F', 15, "Calle 5ta");
        var cliente2 = new Cliente(new Date(), false, "Sandra", 'F', 20, null);
        Imprimir(cliente1);
        Imprimir(cliente2);
        
        var empleado3 = new Empleado("Raul", 500000);
        Imprimir(empleado3);
    }

    public static void Imprimir(Empleado empleado) {
        System.out.println(empleado);
    }

    public static void Imprimir(Cliente cliente) {
        System.out.println(cliente);
    }
}
