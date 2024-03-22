
public class Main
{
    public static void main(String[] args)
    {
        Fila fila = new Fila();
        fila.add(10);
        fila.add(20);
        fila.add(30);
        fila.add(40);
        fila.add(50);
        fila.add(60);
        System.out.println("IMPRIMIR FILA:");
        fila.print();
        System.out.println("\n\nFILA CONTEM O VALOR 20:");
        System.out.println(fila.contains(20));
        fila.remove();
        fila.remove();
        System.out.println("\nPRINT DEPOIS DE REMOVER OS 2 PRIMEIROS:");
        fila.print();
        System.out.println("\n\nFILA PEEK,SIZE,ESTÁ VAZIA E CONTEM O VALOR 20");
        System.out.println(fila.peek());
        System.out.println(fila.size());
        System.out.println(fila.isEmpty());
        System.out.println(fila.contains(20));
        fila.clear();
        System.out.println("\nCLEAR + PRINT + PEEK + SIZE");
        fila.print();
        System.out.println(fila.peek());
        System.out.println(fila.size());
    }
}
