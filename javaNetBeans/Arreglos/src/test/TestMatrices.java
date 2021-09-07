package test;

public class TestMatrices {

    public static void main(String[] args) {

        int edades[][] = new int[3][3];
        edades[0][2] = 3;
        edades[1][0] = 7;
        edades[2][1] = 5;
        for (int i = 0; i < edades.length; i++) {
            for (int j = 0; j < edades[i].length; j++) {
                System.out.println("Edades " + i + " " + j + ": " + edades[i][j]);

            }

        }
        System.out.println("");

        String frutas[][] = {{"naranja", "limon", "mora"}, {"mango", "pera",
            "fresa"}};
        imprimir(frutas);
    }

    public static void imprimir(Object matriz[][]) {
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                System.out.println("indice " + i + "-" + j + ": " + matriz[i][j]);

            }
        }
    }
}
