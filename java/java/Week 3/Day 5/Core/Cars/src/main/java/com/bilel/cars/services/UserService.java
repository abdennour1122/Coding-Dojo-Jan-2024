package com.bilel.cars.services;

import java.util.Optional;

import org.mindrot.jbcrypt.BCrypt;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.validation.BindingResult;

import com.bilel.cars.models.LoginUser;
import com.bilel.cars.models.USER;
import com.bilel.cars.repositories.UserRepository;

@Service
public class UserService {
	@Autowired
	private UserRepository USERRep;
	public USER register(USER newUSER,BindingResult result) {
		Optional<USER> opUSER = USERRep.findByEmail(newUSER.getEmail());
		if(opUSER.isPresent()) {
			result.rejectValue("email","registerErrors","Email is already taken!");
		}
		if(!newUSER.getPassword().equals(newUSER.getConfirm())) {
			result.rejectValue("confirmPassword", "registerErrors", "password and confirm dont match");
			
		
		}
		if(result.hasErrors()) {
			return null;
		}else {
			newUSER.setPassword(BCrypt.hashpw(newUSER.getPassword(),BCrypt.gensalt()));
			return USERRep.save(newUSER);
		}
				
	}
	public USER login(LoginUser newLoginUSER, BindingResult result) {
		Optional<USER>opUSER =USERRep.findByEmail(newLoginUSER.getEmail());
		if(!opUSER.isPresent()) {
			result.rejectValue("email", "loginErrors","Invalid credential!");
		}else {
			USER user=opUSER.get();
			//check password
			if(!BCrypt.checkpw(newLoginUSER.getPassword(),user.getPassword())) {
				result.rejectValue("password","loginErrors","Invalid credentials");
				
			}
			if(result.hasErrors()) {
				return null;
			}else {
				return user;
			}
		}
		return null;
		
	}
	public USER findUSERByID(long id) {
		Optional<USER> maybeUSER = USERRep.findById(id);
		if(maybeUSER.isPresent()) {
			return maybeUSER.get();
		}else {
			return null;
		}
		
	}
	
	
	

}
