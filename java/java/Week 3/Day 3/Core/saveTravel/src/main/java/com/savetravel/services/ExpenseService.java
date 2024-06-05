package com.savetravel.services;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.Optional;

import com.savetravel.models.Expense;
import com.savetravel.repositories.ExpenseRepository;

@Service
public class ExpenseService {
    //injecting the ExpenseRepository
    @Autowired
    private ExpenseRepository expenseRepository;

    //find all expenses
    public List<Expense> findAll() {
        return expenseRepository.findAll();
    }

    //create a new expense
    public Expense create(Expense expense) {
        return expenseRepository.save(expense);
    }

    //update an expense
    public Expense update(Expense expense) {
        return expenseRepository.save(expense);
    }

    //find an expense by id
    public Expense findById(Long id) {
        Optional<Expense> expense = expenseRepository.findById(id);
        if (expense.isPresent()) {
            return expense.get();
        } else {
            return null;
        }
    }

    //delete an expense
    public void delete(Long id) {
        expenseRepository.deleteById(id);
    }

}
