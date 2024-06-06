package com.bilel.cars.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import com.bilel.cars.models.LoginUser;
import com.bilel.cars.models.USER;
import com.bilel.cars.services.UserService;

import jakarta.servlet.http.HttpSession;
import jakarta.validation.Valid;

@Controller
public class UserController {
	@Autowired
	private UserService userserv;

	@GetMapping("/")
	public String index(Model model) {
		model.addAttribute("newUser", new USER());
		model.addAttribute("newLogin", new LoginUser());
		return "index.jsp";

	}

	@PostMapping("/register")
	public String register(@Valid @ModelAttribute("newUser") USER newUser, BindingResult result, HttpSession session,
			Model model) {
		userserv.register(newUser, result);
		if (result.hasErrors()) {
			model.addAttribute("newLogin", new LoginUser());

			return "index.jsp";
		}
		session.setAttribute("user_id", newUser.getId());
		return "redirect:/cars";

	}

	@PostMapping("/login")
	public String login(@Valid @ModelAttribute("newLogin") LoginUser newLogin, BindingResult result,
			HttpSession session, Model model) {
		USER user = userserv.login(newLogin, result);
		if (result.hasErrors()) {
			model.addAttribute("newUser", new USER());
			return "index.jsp";
		}
		session.setAttribute("user_id", user.getId());
		return "redirect:/cars";
	}

	@RequestMapping("/logout")
	public String logout(HttpSession session) {
		session.invalidate();
		return "redirect:/";

	}
}
