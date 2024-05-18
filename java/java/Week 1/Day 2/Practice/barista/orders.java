import java.util.ArrayList;
 
private class orders {
       private String name;
       private double total;
       private boolean ready;
       private ArrayList<items> items;
       public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public double getTotal() {
        return total;
    }
    public void setTotal(double total) {
        this.total = total;
    }
    public boolean isReady() {
        return ready;
    }
    public void setReady(boolean ready) {
        this.ready = ready;
    }
    public ArrayList<items> getItems() {
        return items;
    }
    public void setItems(ArrayList<items> items) {
        this.items = items;
    }
    private orders(String name,double total,boolean ready, ArrayList<items> items){
        this.name=name;
        this.total=total;
        this.ready=ready;
        this.items=items;
    }
   private double increment() {
        this.total++;
        return total;
        
    }
    }
    
    
