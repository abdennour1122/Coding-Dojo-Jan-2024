package com.bilel.dojoninjas.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;

import com.bilel.dojoninjas.models.Dojo;
import com.bilel.dojoninjas.services.DojoService;

import jakarta.validation.Valid;

@Controller
public class DojoController {
	
	@Autowired
	private DojoService dojoServ;
	
	
	@GetMapping("/dojos/new")
	public String newDojo(@ModelAttribute("dojo") Dojo dojo) {
		return"newdojo.jsp";
	}
	
	@PostMapping("/processdojo")
	public String createDojo(@Valid @ModelAttribute("dojo")Dojo dojo,BindingResult result) {
		if(result.hasErrors()) {
			return"newdojo.jsp";
		}else {
			dojoServ.createDojo(dojo);
			return"redirect:/dojos/new";
		}
	}

	@GetMapping("/dojos/{id}")
	public String showDojo(@PathVariable("id") Long id, Model model) {
		Dojo dojo = dojoServ.findDojoById(id);
		model.addAttribute("dojo", dojo);
		return "showdojo.jsp";
	}


	

	
	

}
