package com.burgertraquer.services;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.burgertraquer.models.Burger;
import com.burgertraquer.repositories.BurgerRepository;

@Service
public class BurgerService {

    @Autowired
    private BurgerRepository burgerRepository;

    public List<Burger> allBurgers() {
        return burgerRepository.findAll();
    }

    public Burger createBurger(Burger b) {
        return burgerRepository.save(b);
    }

}
