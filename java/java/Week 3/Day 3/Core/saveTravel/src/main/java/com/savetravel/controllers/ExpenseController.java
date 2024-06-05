package com.savetravel.controllers;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.PathVariable;

import com.savetravel.models.Expense;
import com.savetravel.services.ExpenseService;

import jakarta.validation.Valid;

@Controller
public class ExpenseController {

    @Autowired
    private ExpenseService expenseService;

    // Get all expenses
    @GetMapping("/expenses")
    public String index(@ModelAttribute("expense") Expense expense, Model model) {
        List<Expense> allExpense = expenseService.findAll();
        model.addAttribute("allExpense", allExpense);
        return "index.jsp";
    }

    // Create an expense
    @PostMapping("/create")
    public String create(@Valid @ModelAttribute("expense") Expense expense, BindingResult result, Model model) {
        if (result.hasErrors()) {
            List<Expense> allExpense = expenseService.findAll();
            model.addAttribute("allExpense", allExpense);
            return "index.jsp";
        } else {
            expenseService.create(expense);
            return "redirect:/expenses";
        }
    }

    //get edit an expense
    @GetMapping("/edit/{id}")
    public String edit(@PathVariable("id") Long id, Model model) {
        Expense expense = expenseService.findById(id);
        model.addAttribute("expense", expense);
        return "edit.jsp";
    }

    //Put update an expense
    @PutMapping("/update/{id}")
    public String update(@Valid @ModelAttribute("expense") Expense expense, BindingResult result, Model model) {
        if (result.hasErrors()) {
            model.addAttribute("expense", expense);
            return "edit.jsp";
        } else {
            expenseService.update(expense);
            return "redirect:/expenses";
        }
    }

    //delete an expense
    @GetMapping("/delete/{id}")
    public String delete(@PathVariable("id") Long id) {
        expenseService.delete(id);
        return "redirect:/expenses";
    }

    //Show an expense
    @GetMapping("/expense/{id}")
    public String show(@PathVariable("id") Long id, Model model) {
        Expense expense = expenseService.findById(id);
        model.addAttribute("expense", expense);
        return "show.jsp";
    }






}
