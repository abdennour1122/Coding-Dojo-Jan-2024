package com.abdennour.hellohuman;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@RestController
public class HellohumanApplication {

	public static void main(String[] args) {
		SpringApplication.run(HellohumanApplication.class, args);
	}
	@RequestMapping("/daikichi/travel/{country}")
    public String index(@PathVariable("country") String country){
      return "congratulations you will soon travel to  "+ country;
    }
    // you can be explicit about the request as well
    @RequestMapping(value="/daikichi/lotto/{id}", method=RequestMethod.GET)
    public String hello(@PathVariable("id") int id){
    	if (id%2==0) {
    		return "You will take a grand journey in the near future, but be weary of tempting offers";
    	}
    	else {
    		return "You have enjoyed the fruits of your labor but now is a great time to spend time with family and friends.";
    	}
      
    }
    

}
