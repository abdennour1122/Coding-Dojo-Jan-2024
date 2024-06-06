package com.bilel.cars.repositories;

import java.util.Optional;

import org.springframework.data.repository.CrudRepository;

import com.bilel.cars.models.USER;

public interface UserRepository extends CrudRepository<USER, Long> {
	Optional <USER>findByEmail(String email);

}
