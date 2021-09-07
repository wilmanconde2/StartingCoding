package test;

import empleado.Auto;
import empleado.Empleado;
import empleado.Concesionario;
import static empleado.Empleado.calcularMiNomina;
import empleado.Main_window;

public class Testing {

    public static void main(String[] args) {
        var empleado1 = new Empleado("Diego", "Moreno", 1875000);    //reto2
//        var empleado1 = new Empleado("Diego", "Moreno", 0, 0, 1875000);   //reto1

        System.out.println("nombre: " + empleado1.getNombre() + "\nApellido: " + empleado1.getApellido());
        System.out.println("Salario neto del mes: " + calcularMiNomina(empleado1));
        System.out.println(" ");

//        System.out.println(empleado1.toString());
//        System.out.println("");

//        var empleado1 = new Empleado("Diego", "Moreno", 1875000);
        var carro1 = new Auto("electrico", 2);
        var carro2 = new Auto("camioneta", 1);
        var carro3 = new Auto("deportivo", 1);
//        var carro4 = new Auto("electrico", 2);
//        var carro5 = new Auto("electrico", 2);

        empleado1.getAutos().add(carro1);
        empleado1.getAutos().add(carro2);
        empleado1.getAutos().add(carro3);
//        empleado1.getAutos().add(carro4);
//        empleado1.getAutos().add(carro5);

        System.out.println(empleado1.getAutos());
        System.out.println("Salario neto del mes: " + Empleado.calcularMiNomina(empleado1));
        System.out.println("Comision: " + empleado1.getComision());
        System.out.println("");

        System.out.println("Dias trabajados: " + Concesionario.diasTrabajados("2020-01-01", "2020-12-30"));
        double diasPagados = Concesionario.calcularPagos(empleado1, "2020-01-01", "2020-12-30");
        double deducciones = Concesionario.calcularDeducciones(empleado1, "2020-01-01", "2020-12-30");
        System.out.println("Pagos totales: "
                + Empleado.eliminarNotCientifica(diasPagados)
                + "\nDeducciones totales:  " + Empleado.eliminarNotCientifica(deducciones));
        
        var window = new Main_window();
        window.setVisible(true);
        
    }

}
