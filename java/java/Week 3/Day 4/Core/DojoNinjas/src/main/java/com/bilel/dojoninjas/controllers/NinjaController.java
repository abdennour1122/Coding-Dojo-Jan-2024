package com.bilel.dojoninjas.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

import com.bilel.dojoninjas.models.Ninja;
import com.bilel.dojoninjas.services.DojoService;
import com.bilel.dojoninjas.services.NinjaService;

import jakarta.validation.Valid;

@Controller
public class NinjaController {
	
	@Autowired
	private NinjaService ninjaServ;
	
	@Autowired
	private DojoService dojoServ;
	
	//Get Mapping for the form to create a new ninja with the dojo in a select
	@GetMapping("/ninjas/new")
	public String newNinja(@ModelAttribute("ninja") Ninja ninja, Model model) {
		model.addAttribute("dojos", dojoServ.allDojos());
		return "newninja.jsp";
	}

	//post mapping to create a new ninja
	@PostMapping("/processninja")
	public String processNinja(@Valid @ModelAttribute("ninja") Ninja ninja, BindingResult result) {
		if(result.hasErrors()) {
			return "newninja.jsp";
		}else {
			ninjaServ.createNinja(ninja);
			return "redirect:/ninjas/new";
			// return "redirect:/dojos/" + ninja.getDojo().getId();
		}
	}

}
