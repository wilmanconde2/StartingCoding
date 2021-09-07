package test;

import domain.Persona;
import javax.swing.JOptionPane;

public class TestArrays {

    public static void main(String[] args) {

        System.out.println("Arreglo de 5 elementos ->");
        int edades[] = new int[5];
        edades[1] = 23;
        edades[3] = 12;
        for (int i = 0; i < 5; i++) {
            System.out.println("Indice " + i + " " + edades[i]);
        }
        System.out.println("");

        System.out.println("Arreglo de numeros aleatorios e impresion de "
                + "numeros pares ->");
        var aleatorios = Integer.parseInt(JOptionPane.showInputDialog("Cantidad "
                + "de numeros en arreglo"));
        int arreglo[] = new int[aleatorios];
        for (int i = 0; i < arreglo.length; i++) {
            arreglo[i] = (int) (Math.random() * 100);
            System.out.println("Indice " + i + " --> " + arreglo[i]);
            if (arreglo[i] % 2 == 0) {
                System.out.println(arreglo[i] + " es par");
            }
        }
        System.out.println("");

        //iniciar valores de un arreglo en la misma linea
        String frutas[] = {"banano", "melon", "sandia", "mango"};
        System.out.println("Arreglo frutas");
        for (int i = 0; i < frutas.length; i++) {
            System.out.println("Fruta " + i + ": " + frutas[i]);
        }
        System.out.println("");

        //se puede crear instancia de objeto con VAR
        var persona = new Persona("Pedro");
        System.out.println("Instancia " + persona);
        System.out.println("");

    }
}
