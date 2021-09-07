package test;

import domain.*;

public class Testing {

    public static void main(String[] args) {

        var teclado1 = new Teclado("usb", "sony");
        var teclado2 = new Teclado("bluetooth", "LG");
        var raton1 = new Raton("bluetooth", "elios");
        var raton2 = new Raton("usb", "panasonic");
        var monitor1 = new Monitor("samsung", 150.8);
        var monitor2 = new Monitor("vaio", 175.5);
        var pc1 = new Computador("razer", monitor1, teclado1, raton1);
        var pc2 = new Computador("giga", monitor2, teclado2, raton2);
        var pc3 = new Computador("mix", monitor1, teclado2, raton1);

        var orden1 = new Orden();
        orden1.agregarComputador(pc1);
        orden1.agregarComputador(pc2);
        orden1.agregarComputador(pc3);
        orden1.mostrarOrden();

    }
}
