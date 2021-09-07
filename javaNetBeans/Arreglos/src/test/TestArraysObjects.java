package test;

import domain.Persona;

public class TestArraysObjects {

    public static void main(String[] args) {

        //para crear arrays no se puede usar VAR, se usa el nombre 
        //de la clase a instanciar
        Persona personas[] = new Persona[3];
        personas[0] = new Persona("Salome");
        personas[1] = new Persona("Paul");
        personas[2] = new Persona(null);
        System.out.println("Arreglo personas");
        for (int i = 0; i < personas.length; i++) {
            System.out.println("Persona " + i + " : " + personas[i]);
        }
    }
}
