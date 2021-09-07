package domain;

public class Orden {

    private final int idOrden;
    private static int contadorOrdenes;
    private Producto productos[];
    private int contadorProductos;
    private final int MAX_PRODUCTOS = 10;

    public Orden() {
        this.idOrden = ++Orden.contadorOrdenes;
        this.productos = new Producto[Orden.this.MAX_PRODUCTOS];

    }

    public int getIdOrden() {
        return this.idOrden;
    }

    public static int getContadorOrdenes() {
        return Orden.contadorOrdenes;
    }

    public Producto[] getProductos() {
        return this.productos;
    }

    public void setProductos(Producto[] productos) {
        this.productos = productos;
    }

    public int getContadorProductos() {
        return this.contadorProductos;
    }

    public void agregarProducto(Producto producto) {
        if (this.contadorProductos < Orden.this.MAX_PRODUCTOS) {
            this.productos[this.contadorProductos++] = producto;
        } else {
            System.out.println("Ha superado la cantidad maxima de productos: " + Orden.this.MAX_PRODUCTOS);
        }
    }

    public double calcularTotal() {
        var total = 0;
        for (int i = 0; i < this.contadorProductos; i++) {
            total += this.productos[i].getPrecio();
        }
        return total;
    }

    public void mostrarOrden() {
        System.out.println("Id Orden: " + this.idOrden);
        System.out.println("Total Orden: $" + this.calcularTotal());
        System.out.println("Productos de la orden: ");
        for (int i = 0; i < this.contadorProductos; i++) {
            System.out.println(this.productos[i]);

        }
    }
}
