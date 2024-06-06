package com.bilel.cars.controllers;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;

import com.bilel.cars.models.Car;
import com.bilel.cars.models.USER;
import com.bilel.cars.services.CarService;
import com.bilel.cars.services.UserService;

import jakarta.servlet.http.HttpSession;
import jakarta.validation.Valid;

// si tu commence par un @restcontroller pour tester avec postman commencer les route par "/api"

@Controller
public class carController {

	@Autowired
	private CarService carServ;

	@Autowired
	private UserService userserv;

	@GetMapping("/cars/new")
	public String newCar(@ModelAttribute("car") Car car ,HttpSession s) {
		Long userId=(Long) s.getAttribute("user_id");
		if(userId==null) {
			return "redirect:/";
		}
		return "new.jsp";
	}

	@PostMapping("/processeCar")
	public String createCar(@Valid @ModelAttribute("car") Car car, BindingResult result, HttpSession s) {
		Long userId = (Long) s.getAttribute("user_id");
		if (result.hasErrors()) {
			return "new.jsp";
		} else {
			USER user = userserv.findUSERByID(userId);

			car.setOwner(user);
			Car newCar = carServ.createCar(car);
			return "redirect:/cars/show/" + newCar.getId();
		}

	}

	@GetMapping("/cars/show/{id}")
	public String showCar(@PathVariable("id") Long id, Model model) {
		Car car = carServ.findCarById(id);
		model.addAttribute("car", car);
		return "show.jsp";
	}

	@GetMapping("/cars")
	public String home(Model model,HttpSession s) {
		Long userId=(Long) s.getAttribute("user_id");
		if(userId==null) {
			return "redirect:/";
		}
		USER user=userserv.findUSERByID(userId)
		List<Car> allCars = carServ.allCars();
		model.addAttribute("allCars", allCars);
		return "home.jsp";
	}

	// Getmapping edit
	@GetMapping("/cars/edit/{id}")
	public String updateCar(@PathVariable("id") Long id, Model model,HttpSession s) {
		Long userId=(Long) s.getAttribute("user_id");
		if(userId==null) {
			return "redirect:/";
		}
		Car car = carServ.findCarById(id);
		model.addAttribute("car", car);
		return "edit.jsp";
	}

	// putmapping edit
	@PutMapping("/updateCar/{id}")
	public String editCar(@Valid @ModelAttribute("car") Car car, BindingResult result, HttpSession s) {
		Long userId = (Long) s.getAttribute("user_id");
		if (result.hasErrors()) {
			return "edit.jsp";
		} else {
			USER user = userserv.findUSERByID(userId);

			car.setOwner(user);
			carServ.updateCar(car);
			return "redirect:/cars";
		}
	}

	// delete
	@DeleteMapping("/cars/delete/{id}")
	public String deleteCar(@PathVariable("id") Long id,HttpSession s) {
		Long userId=(Long) s.getAttribute("user_id");
		if(userId==null) {
			return "redirect:/";
		}
		carServ.deleteCar(id);
		return "redirect:/cars";
	}

}
