import java.util.Iterator;
import java.util.LinkedList;
import java.util.NoSuchElementException;
import java.util.Queue;
import java.util.Scanner;
public class Fila {
    private Node first; // mais recente
    private Node last;  // mais antigo
    
    private int N;

    private class Node {
        private int item;
        private Node next;
    }

    public int size( ) {
        return N;
    }

    public boolean isEmpty( ) {
        if((first == null) && (last == null))
            return true;
        return false;
    }

    public int peek( ) {
        if (isEmpty())
            return -1;
        return first.item;
    }

    public void clear( ) {
        int tamanho = N;
        for(int i=0;i<tamanho;i++)
        {
            remove();
        }
    }

    public void add(int item) {
        Node no = new Node();
        if(isEmpty())
        {
            no.item = item;
            no.next = null;
            first = no;
            last = no;
            N++;
        }
        else
            if(N == 1)
            {
               no.next = null;
               no.item = item;
               first.next = no;
               last = no;
               N++;
            }
            else
            {
                last.next = no;
                no.item = item;
                no.next = null;
                last = no;
                N++;
            }
    }

    public int remove() {
        if (isEmpty())
            return -1;
        if (N>1)
        {
            Node temp = new Node();
            temp = first;
            first = first.next;
            temp.next = null;
            N--;
        }
        else
        {
            first = null;
            last = null;
            N--;
        }
        return 0;
    }

    public void print( )
    {
        Node temp = new Node();
        temp = first;
        for (int i=0;i<N;i++)
        {
            System.out.print(temp.item+ " ");
            temp = temp.next;
        }
    }

    public boolean contains(int item)
    {
        Node temp = new Node();
        temp = first;
        int repeticao = 0;
        for (int i=0;i<N;i++)
        {
            if(temp.item == item)
                repeticao = 1;
            temp = temp.next;
        }
        temp = null;
        if (repeticao == 1)
            return true;
        return false;
    }
}
