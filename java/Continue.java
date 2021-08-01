public class Continue {
    public static void main(String[] args) {
        for (var contador = 0 ;contador < 10 ;contador++){
            if (contador % 2 != 0){
                continue;   // salta a la siguiente iteración sin realizar el código restante
            }
            System.out.println("Contador: " + contador);
        }
    }
}
