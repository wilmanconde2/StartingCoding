package operaciones;

public class Caja {
    int alto;
    int ancho;
    int profundo;
    
    public Caja(){
    }
    
    public Caja(int a, int b, int c){
//        this.alto = a;
//        this.ancho = b;
//        this.profundo = c;
//        int resultado = calcularVolumen(this.alto, this.ancho, this.profundo);
//        System.out.println("Volumen de la caja: " + resultado);
    }

    public int calcularVolumen(int a, int b, int c){
        return (a * b * c);
    }
}
