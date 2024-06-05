package com.burgertraquer.repositories;


import java.util.List;
import java.util.Optional;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.burgertraquer.models.Burger;


@Repository
public interface BurgerRepository extends CrudRepository<Burger, Long>{
    //? Find All Burger
    List<Burger> findAll();

    //? Find Burger by ID
    Optional<Burger> findById(Long id);

    //? update Burger
    Burger save(Burger burger);
}
