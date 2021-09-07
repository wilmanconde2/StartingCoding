package empleado;

import java.text.DecimalFormat;
import java.util.ArrayList;

public class Empleado {

    private int id;
//    private static int contadorId;
    private String nombre;
    private String apellido;
    private ArrayList<Auto> autos = new ArrayList<>();
    private static int comision;
    private int horasExtra;
    private int salario;

    //constructor reto2
    public Empleado(String nombre, String apellido, int salario) {
//        Empleado.contadorId++;
//        this.id = Empleado.contadorId;
        this.nombre = nombre;
        this.apellido = apellido;
        this.salario = salario;
    }

    //constructor reto1
    public Empleado(String nombre, String apellido, int comision,
            int horasExtra, int salario) {

        this.nombre = nombre;
        this.apellido = apellido;
        Empleado.comision = comision;
        this.horasExtra = horasExtra;
        this.salario = salario;
    }

    public int getId() {
        return this.id;
    }

//    public static int getContadorId() {
//        return Empleado.contadorId;
//    }
    public String getNombre() {
        return this.nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getApellido() {
        return this.apellido;
    }

    public void setApellido(String apellido) {
        this.apellido = apellido;
    }

    public ArrayList<Auto> getAutos() {
        return this.autos;
    }

    public void setAutos(ArrayList<Auto> autos) {
        this.autos = autos;
    }

    public int getComision() {
        return Empleado.comision;
    }

    public void setComision(int comision) {
        Empleado.comision = comision;
    }

    public int getHorasExtra() {
        return this.horasExtra;
    }

    public void setHorasExtra(int horasExtra) {
        this.horasExtra = horasExtra;
    }

    public int getSalario() {
        return this.salario;
    }

    public void setSalario(int salario) {
        this.salario = salario;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Empleado{id=").append(id);
        sb.append(", nombre=").append(nombre);
        sb.append(", apellido=").append(apellido);
        sb.append(", autos=").append(autos);
        sb.append(", comision=").append(comision);
        sb.append(", horasExtra=").append(horasExtra);
        sb.append(", salario=").append(salario);
        sb.append(", ").append(super.toString());
        sb.append('}');
        return sb.toString();
    }

    public static String eliminarNotCientifica(double numero) {
        return new DecimalFormat("#.####################################").format(numero);
    }

    public static double comision(Empleado empleado) {
        Empleado.comision = 0;
        for (int i = 0; i < empleado.autos.size(); i++) {
            switch (empleado.getAutos().get(i).getTipo()) {

                case 1:
                    Empleado.comision = Empleado.comision + 750000;
                    break;
                case 2:
                    Empleado.comision = Empleado.comision + 500000;
                    break;
                case 3:
                    Empleado.comision = Empleado.comision + 350000;
                    break;
                default: {
                }
            }
        }
        return Empleado.comision;
    }

    public static double calcularMiNomina(Empleado empleado) {
        var aportes = 0.08;
        var devengadoBruto = (comision(empleado) + empleado.getHorasExtra() + empleado.getSalario());
        System.out.println("Salario bruto del mes: " + devengadoBruto);
        var devengadoNeto = devengadoBruto - (devengadoBruto * aportes);
//        var devengadoNeto = (devengadoBruto * 0.92);  //otra opcion
        return devengadoNeto;

    }

}
