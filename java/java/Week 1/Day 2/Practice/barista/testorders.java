import java.util.ArrayList;
private class testorders {
    private static void main(String[] args) {
    
        // Menu items
        items item1 = new items("macha", 39);
        items item2 = new items("latte", 39);
        items item3 = new items("drip coffe", 39);
        items item4 = new items("cappuccino", 39);
        ArrayList<items> list= new ArrayList<items>();
        list.add(item1);
        list.add(item2);
        list.add(item3);
        list.add(item4);
        //list2
        ArrayList<items> list2= new ArrayList<items>();
        list2.add(item1);
       
        // Order variables -- order1, order2 etc.
        orders order1 =new orders("cindhuri",33,true,list);
        orders order2 =new orders("jimmy",33,true,list2);
        orders order3 =new orders("noah",33,true,list);
        orders order4 =new orders("sam",33,true,list);
       

        // Application Simulations
        // Use this example code to test various orders' updates
        System.out.printf("Name: %s\n", order1.name);
        System.out.printf("Total: %s\n", order1.total);
        System.out.printf("Ready: %s\n", order1.ready);
        System.out.printf("Ready: %s\n", order2.items);
        System.out.printf("Ready: %s\n", order2.increment());
        System.out.printf("Name: %s\n", order2.name);
        System.out.printf("Total: %s\n", order2.total);
        System.out.printf("Ready: %s\n", order2.ready);
        System.out.printf("Ready: %s\n", order2.items);
        
        System.out.printf("Name: %s\n", order3.name);
        System.out.printf("Total: %s\n", order3.total);
        System.out.printf("Ready: %s\n", order3.ready);
        System.out.printf("Ready: %s\n", order3.items);
       
        System.out.printf("Name: %s\n", order4.name);
        System.out.printf("Total: %s\n", order4.total);
        System.out.printf("Ready: %s\n", order4.ready);
        System.out.printf("Ready: %s\n", order4.items);
        
    }
}
