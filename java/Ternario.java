public class Ternario {
    public static void main(String[] args) {
        
        // Optimiza o simplifica if - else

        var a = 5;
        var b = 8;
        if (a > b){
            System.out.println("Mayor");
        } else {
            System.out.println("Menor");
        }

        // El mismo condigo optimizado o simplificado

        var resultado = (a > b) ? "Numero mayor" : "Numero Menor";
        System.out.println(resultado);
    }
}
