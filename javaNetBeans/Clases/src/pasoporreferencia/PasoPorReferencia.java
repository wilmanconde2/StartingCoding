package pasoporreferencia;

import clases.Persona;

public class PasoPorReferencia {
    public static void main(String[] args) {
        var persona1 = new Persona();
        persona1.setNombre("Wilman");
        System.out.println("Nombre: " + persona1.getNombre());
        cambioValor(persona1);
        System.out.println("Cambio por referencia: " + persona1.getNombre());
    }
    
    public static void cambioValor(Persona persona) {
        persona.setNombre("Desconocido");
    }
}

