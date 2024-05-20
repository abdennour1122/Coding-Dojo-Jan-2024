package com.abdennour.hellohuman;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@RestController
public class Hellohuman1Application {

	public static void main(String[] args) {
		SpringApplication.run(Hellohuman1Application.class, args);
	}
	@RequestMapping("/")
    public String hello() {
    	return "Hello human";
    }
	@RequestMapping("/")
	 public String name(@RequestParam(value="name", required=false) String searchQuery){
    	return "Hello "+searchQuery;
    }

}
