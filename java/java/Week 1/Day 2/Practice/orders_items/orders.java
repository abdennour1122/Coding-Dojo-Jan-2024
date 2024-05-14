import java.util.ArrayList;
 
 public class orders {
        public String name;
        public double total;
        public boolean ready;
        public ArrayList<items> items;
        public orders(String name,double total,boolean ready, ArrayList<items> items){
        this.name=name;
        this.total=total;
        this.ready=ready;
        this.items=items;
    }
    public double increment() {
        this.total++;
        return total;
        
    }
    }
    
    
