import java.util.*;
class Simple{  

    static PriorityQueue<Integer> q = new PriorityQueue<Integer>();
    static HashMap<Integer, String> slot_to_number = new HashMap<Integer, String>();
    static HashMap<String, String> number_to_colour = new HashMap<String, String>();
    static Integer size_of_parking_lot;





    static void fn_park_new_car(String car_number, String car_colour){
        //adding new car
        Integer slot_num=q.poll();
        slot_to_number.put(slot_num, car_number);
        number_to_colour.put(car_number, car_colour);
        System.out.println("Allocated slot number: "+slot_num);

        System.out.println(slot_to_number.size() + " "+ number_to_colour.size());
    }
    static void fn_create_parking_lot(String s){
        int n=Integer.parseInt(s);  
        size_of_parking_lot=n;
        for(int i=0;i<n;i++){
            q.add(i+1);
        }
        // System.out.println("Head value using peek function:" + q.peek());
        // q.poll();
        // System.out.println("Head value using peek function:" + q.peek());

        System.out.println("Created a parking lot with "+n+" slots");
    }
    static void fn_leave(String s){
        int n=Integer.parseInt(s);  
        boolean b = q.contains(n);

        if(n<size_of_parking_lot){
            System.out.print("@@checking slot "+n+ " is occupied or not?: " + !b);
            if(!b){
                q.add(n);
                String car_num=slot_to_number.get(n);
                slot_to_number.remove(n);
                number_to_colour.remove(car_num);
                System.out.println("Slot number "+n+" is free");
                System.out.println("The size of the queue is: " + q.size());
            }
            
        }
        else{
            System.out.println("Slot number is greater than the soze of the parking lot");
        }


    }
    static void fn_registration_numbers_for_cars_with_colour(String s){
        Integer ck=0;
        for (String i : number_to_colour.keySet()) {
            if(number_to_colour.get(i).equals(s) && ck.equals(0)){
                System.out.print(i);
                ck=1;
            }
            else if(number_to_colour.get(i).equals(s) && ck.equals(1))System.out.print(", "+i);
        }
        if(ck==0){
            System.out.println("Not Found");
        }

    }
    static void fn_slot_numbers_for_cars_with_colour(String s){

    }
    static void fn_slot_number_for_registration_number(String s){

    }
    static void fn_status(){
        System.out.println("Slot No.");
        List<Integer> arr = new ArrayList<Integer>();
        List<String> arr2 = new ArrayList<String>();
        for (Integer i : slot_to_number.keySet()) {
            System.out.println(i);
            arr.add(i);
        }
        System.out.println("Registration No");
        for (int i=0;i<arr.size();i++) {
            String r_n=slot_to_number.get(arr.get(i));
            System.out.println(r_n);
            arr2.add(r_n);
        }
        System.out.println("Colour");
        for (int i=0;i<arr2.size();i++) {
            System.out.println(number_to_colour.get(arr2.get(i)));
        }
        

                    

    }
    
    public static void main(String args[]){  
        System.out.println("Hello Java");  
        Scanner sc= new Scanner(System.in);  
        String ck="";

        do{
            System.out.print("\nEnter a string: ");  
            String str= sc.nextLine();           
            String[] words = str.split("\\s+");
            // System.out.print("You have entered: "+str);
            // System.out.print(" words"+ words.length);

            if(words.length==3){//new car is added
                if(q.size()>0)fn_park_new_car(words[1],words[2]);
                else{
                    System.out.println("Sorry, parking lot is full");
                }
            }
            else if(words.length==2){
                String a=words[0];
                String b=words[1];
                // if(a.equals("create_parking_lot")){
                if(a.equals("c")){
                    fn_create_parking_lot(words[1]);
                }
                else if(a.equals("leave")){ //done
                    fn_leave(b);
                }
                else if(a.equals("registration_numbers_for_cars_with_colour")){
                    fn_registration_numbers_for_cars_with_colour(b);
                }
                else if(a.equals("slot_numbers_for_cars_with_colour")){
                    fn_slot_numbers_for_cars_with_colour(b);
                }
                else if(a.equals("slot_number_for_registration_number")){
                    fn_slot_number_for_registration_number(b);
                }
            }
            else if(words.length==1){
                if(words[0].equals("status")){
                    fn_status();
                }
                else if(words[0].equals("exit")){
                    System.exit(0);
                }
                else if(words[0].equals("see")){
                    for (Integer i : slot_to_number.keySet()) {
                        System.out.println("slot: " + i + " number: " + slot_to_number.get(i));
                    }
                    for (String i : number_to_colour.keySet()) {
                        System.out.println("number: " + i + " colour: " + number_to_colour.get(i));
                    }
                    
                }
            }
            
            // for(int i=0;i<words.length;i++){
            //     System.out.print("loop: "+words[i]);
            // }

        }while(ck!="exit");


    
    }  
}  




// 2.create_parking_lot 6
// 3.park KA-01-HH-1234 White
// 2.leave 4
// 1.status
// 2.registration_numbers_for_cars_with_colour White
// 1.exit

// 2.registration_numbers_for_cars_with_colour White
//KA-01-HH-1234, KA-01-HH-9999, KA-01-P-333
// 2.slot_numbers_for_cars_with_colour White
//1, 2, 4
// 2.slot_number_for_registration_number KA-01-HH-3141
//6
// 2.slot_number_for_registration_number MH-04-AY-1111
