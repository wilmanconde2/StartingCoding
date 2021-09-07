package empleado;

public class Auto {

    private String marca;
    private int tipo;

    public Auto(String marca, int tipo) {
        this.marca = marca;
        this.tipo = tipo;
    }

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public int getTipo() {
        return tipo;
    }

    public void setTipo(int tipo) {
        this.tipo = tipo;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Auto{marca=").append(marca);
        sb.append(", tipo=").append(tipo);
        sb.append('}');
        return sb.toString();
    }

}
