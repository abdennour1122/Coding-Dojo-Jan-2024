package com.Counter.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

import jakarta.servlet.http.HttpSession;

@Controller
public class CounterController {
	
	@RequestMapping("/")
	public String index (HttpSession session) {
        // check if session attribute "count" is null
        if (session.getAttribute("count") == null) {
            session.setAttribute("count", 0);
        } else {
            // get the current count from session
            Integer count = (Integer) session.getAttribute("count");
            // increment the count by 1
            count++;
            // set the updated count to session
            session.setAttribute("count", count);
        }
		return "index.jsp";
	}

    @RequestMapping("/counter")
    public String counter (HttpSession session) {
        // get the current count from session
        int count = (int) session.getAttribute("count");
        System.out.println("the count is: " + count + " times");
        return "counter.jsp";
    }


}
