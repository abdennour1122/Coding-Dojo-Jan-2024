package com.bilel.cars.services;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.bilel.cars.models.Car;
import com.bilel.cars.repositories.CarRepository;

@Service
public class CarService {
	
	@Autowired
	private CarRepository carRepo;// premiere lettre des variable minuscule
	

	
	//create
	public Car createCar(Car car) {
		System.out.println(car);
		return carRepo.save(car);
	}
	
	//READ ONE 
	public Car findCarById(Long id) {
		Optional<Car> optCar = carRepo.findById(id);
		if(optCar.isPresent()) {
			return optCar.get();
		}
		return null;
	}
	
	//read all 
	public List<Car> allCars(){
		return carRepo.findAll();
	}

	//edit 
	public Car updateCar(Car car) {
		return carRepo.save(car);
	}

	//delete
	public void deleteCar(Long id) {
		carRepo.deleteById(id);
	}

}
