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
            first = no;
            last = no;
            first.item = item;
            first.next = null;
            last.next = null;
            last.item = item;
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
            temp = first.next;
            first = first.next;
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
        for (int i=0;i<N;i++)
        {
            if(temp.item == item)
                return true;
            temp = temp.next;
        }
        return false;
    }
}
