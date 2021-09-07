package empleado;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;

public class Concesionario {

    private ArrayList<Auto> autos = new ArrayList<>();
    private ArrayList<Empleado> empleados = new ArrayList<>();

    public ArrayList<Auto> getAutos() {
        return autos;
    }

    public void setAutos(ArrayList<Auto> autos) {
        this.autos = autos;
    }

    public static SimpleDateFormat getDiasTrabajados() {
        return diasTrabajados;
    }

    public ArrayList<Empleado> getEmpleados() {
        return empleados;
    }

    public void setEmpleados(ArrayList<Empleado> empleados) {
        this.empleados = empleados;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Concesionario{autos=").append(autos);
        sb.append(", empleados=").append(empleados);
        sb.append('}');
        return sb.toString();
    }
    
//    public static int diasTrabajados (String ingreso, String retiro){
//    
//    LocalDate inicio = LocalDate.parse(ingreso);
//    LocalDate fin = LocalDate.parse (retiro);
//        
//    Period diferencia = Period.between(inicio, fin);
//
//    int years = diferencia.getYears();
//    int months = diferencia.getMonths();
//    int days = diferencia.getDays();
//    int diasTrabajados = (years * 360) + (months * 30) + days;
//    
//    return diasTrabajados;
//    }

    private static final SimpleDateFormat diasTrabajados = new SimpleDateFormat("yyyy-MM-dd");

    public static long diasTrabajados(String start, String end) {
        long days;
        try {
            Date dateStart = diasTrabajados.parse(start);
            Date dateEnd = diasTrabajados.parse(end);

            days = Math.round((dateEnd.getTime() - dateStart.getTime()) / (double) 86400000);
        } catch (ParseException e) {
            System.out.println("Fecha invalida");
            return 0;
        }
        return days - 5;

    }

    public static double calcularPagos(Empleado empleado, String ingreso, String retiro) {

        var dias = diasTrabajados(ingreso, retiro);
        double salario = empleado.getSalario();
        double comision = Empleado.comision(empleado);
        double pagoTotalDias = (salario / 30) * dias + comision;
//        System.out.printf("Pago total: " + "%.2f", pagoTotalDias);
//        System.out.println("");

        return pagoTotalDias;
    }

    public static double calcularDeducciones(Empleado empleado, String ingreso, String retiro) {

        double pagoTotal = calcularPagos(empleado, ingreso, retiro);
        double deduccionesTotales = (pagoTotal * 0.08);
//        System.out.printf("Deducciones totales: " + "%.2f", deduccionesTotales);
//        System.out.println("");

        return deduccionesTotales;
    }
    
    public static double costoEmpleadoParaLaEmpresa(Empleado empleado, String ingreso, String retiro){
        return 36547088.11;
    }
}

