package domain;

public class Orden {

    private final int idOrden;
    private static int contadorOrdenes;
    private final Computador computadores[];
    private final int MAX_COMPUTADORAS = 10;
    private int contadorComputadores;

    public Orden() {
        this.idOrden = ++Orden.contadorOrdenes;
        this.computadores = new Computador[Orden.this.MAX_COMPUTADORAS];

    }

    public void agregarComputador(Computador computador) {

        if (this.contadorComputadores < Orden.this.MAX_COMPUTADORAS) {
            this.computadores[this.contadorComputadores++] = computador;
        } else {
            System.out.println("Ha superado la cantidad maxima de computadores: " + Orden.this.MAX_COMPUTADORAS);
        }

    }

    public void mostrarOrden() {

        System.out.println("Orden id= " + this.idOrden);
        System.out.println("Computadoras de la orden #:" + this.idOrden);
        for (int i = 0; i < this.contadorComputadores; i++) {
            System.out.println(this.computadores[i]);
        }

    }
}
