package test;

import domain.*;

public class testing {

    public static void main(String[] args) {
                
        var producto1 = new Producto("Camisa", 50000);
        var producto2 = new Producto("Pantalon", 100000);
        var producto3 = new Producto("Short", 70000);
        
        var orden1 = new Orden();
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        orden1.agregarProducto(producto3);
        orden1.agregarProducto(producto2);
        orden1.mostrarOrden();
        
        var orden2 = new Orden();
        orden2.agregarProducto(producto1);
        orden2.agregarProducto(producto2);
        orden2.mostrarOrden();
    }
}
