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
            remove();
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
                last = no;
                last.item = item;
                last.next = null;
                N++;
            }
    }

    public int remove() {
        if (isEmpty())
            return -1;
        first = first.next;
        N--;
        return 0;
    }

    //public void print( )
    //{

    //}

    //public boolean contains( int item)
    //{

    //}

    //return first.item -- para o peek(), caso não esteja vazia
    //if first == null && last == null
    //first = firts.next() -- apagar um elemento
    //first = last = null -- apagar o unico elemento
    //Node no = new Node()
    //clear chamar até acabar, usar while e iterator do nome
    //countais iterators aponta para o primeiro nó, e compara com o item, faz iterator = iterator.next()

    public Node getFirst() {
        return first;
    }

    public void setFirst(Node first) {
        this.first = first;
    }

    public Node getLast() {
        return last;
    }

    public void setLast(Node last) {
        this.last = last;
    }

    public int getN() {
        return N;
    }

    public void setN(int n) {
        N = n;
    }
}
