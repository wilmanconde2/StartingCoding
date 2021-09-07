package domain;

public class Empleado extends Persona {

    private final int idEmpleado;
    private double sueldo;
    private static int contadorEmpleados;

    public Empleado() {
        this.idEmpleado = ++Empleado.contadorEmpleados; 
    }

    public Empleado(String nombre, double sueldo) {
//        super(nombre);        //llama todos los atributos de la clase padre
        this();     //inicializo otro constructor, que a su vez inicializa 
                    //la variable idEmpleado
        this.nombre = nombre;       //atributo de la clase padre
        this.sueldo = sueldo;
    }

    public int getIdEmpleado() {
        return this.idEmpleado;
    }

    public double getSueldo() {
        return this.sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }

    public static int getContadorEmpleados() {
        return contadorEmpleados;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Empleado{idEmpleado=").append(idEmpleado);
        sb.append(", nombre=").append(nombre);
        sb.append(", sueldo=").append(sueldo);
        sb.append(",{").append(super.toString());
        sb.append('}');
        return sb.toString();
    }

}
