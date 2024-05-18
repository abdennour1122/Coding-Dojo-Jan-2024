public class TestOrder {
    public static void main(String[] args) {
        Item item1= new Item("drip coffe", 1.6);
        Item item2= new Item("capuccino", 2.45);
        Item item3= new Item("iced coffe", 2.6);
        Item item4= new Item("mocha", 3.1);


    //order
        Order order1= new Order();
        Order order2= new Order();
        Order order3= new Order("bob");
        Order order4= new Order("sam");



        order1.addItem(item4);
        order1.addItem(item3);

        order2.addItem(item1);
        order2.addItem(item1);
        order2.addItem(item4);

        order3.addItem(item2);
        order3.addItem(item1);

        System.out.println(order3.getStatusMessage());
        order3.setReady(true);
        System.out.println(order3.getStatusMessage());

        System.out.println(order3.getOrderTotal());

        order3.display();

    }
}
