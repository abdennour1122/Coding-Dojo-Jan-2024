package com.burgertraquer.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import java.util.List;
import com.burgertraquer.models.Burger;
import com.burgertraquer.services.BurgerService;

import jakarta.validation.Valid;

@Controller
public class BurgerController {

    @Autowired
    private BurgerService burgerService;

    @GetMapping("/")
    public String index(@ModelAttribute("burger") Burger burger, Model model){
        List<Burger> burgers = burgerService.allBurgers();
        model.addAttribute("burgers", burgers);
        return "index.jsp";
    }

    @PostMapping("/create")
    public String create(@Valid @ModelAttribute("burger") Burger burger, BindingResult result, Model model){
        if(result.hasErrors()){
            model.addAttribute("burgers", burgerService.allBurgers());
            return "index.jsp";
        } else {
            burgerService.createBurger(burger);
            return "redirect:/";
        }
    }







}