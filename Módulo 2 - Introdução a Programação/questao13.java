public class CadastroProduto {

    ArrayList cadastroProduto = new ArrayList();

    private String nome;
    private String modelo;
    private String tamanho;
    private double preco;

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        cadastroProduto.add(nome);
        this.nome = nome;
    }

    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        cadastroProduto.add(modelo);
        this.modelo = modelo;
    }

    public String getTamanho() {
        return tamanho;
    }

    public void setTamanho(String tamanho) {
        cadastroProduto.add(tamanho);
        this.tamanho = tamanho;
    }

    public double getPreco() {
        return preco;
    }

    public void setPreco(double preco) {
        cadastroProduto.add(preco);
        this.preco = preco;
    }
}

    public static void main(String[] args) {
        Scanner dados = new Scanner(System.in);
        Scanner dados1 = new Scanner(System.in);
        Scanner dados2 = new Scanner(System.in);
        Scanner dados3 = new Scanner(System.in);

        CadastroProduto c1 = new CadastroProduto();

        String nome = "";
        String modelo = "";
        String tamanho = "";
        double preco = 0;

        System.out.println("Opçoes\n 1-Cadastrar produto\n 2-Remover produto\n 3-Verificar produto\n 4-Dinheiro\n");
        int numopc = 0;
        System.out.print("nº: ");

        numopc = dados.nextInt();

        while (numopc == 1) {

            switch (numopc) {

                case 1:
                    System.out.println("Nome do produto: ");
                    nome = dados1.nextLine();
                    c1.setNome(nome);

                    System.out.println("Modelo do produto: ");
                    modelo = dados2.nextLine();
                    c1.setModelo(modelo);

                    System.out.println("Tamanho do produto: ");
                    tamanho = dados3.nextLine();
                    c1.setTamanho(tamanho);

                    System.out.println("Preço do produto: ");
                    preco = dados.nextDouble();
                    c1.setPreco(preco);

                    System.out.println("\n Cadastrar mais produtos?\n  1-Sim\n  0-Não\n");
                    numopc = dados.nextInt();
                    break;

                case 2:
                    break;

            }


        }
        System.out.println(c1.cadastroProduto.toString());
    }

}
