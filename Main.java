
public class Main
{
    public static void main(String[] args)
    {
        Fila fila = new Fila();
        fila.add(1);
        fila.add(2);
        fila.add(3);
        fila.add(4);
        fila.clear();
        System.out.println(fila.size());
        if(fila.isEmpty())
            System.out.println("Lista vazia.");
        else
            System.out.println("Lista não está vazia.");
        
    }
}
