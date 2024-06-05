package com.bilel.dojoninjas.services;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.bilel.dojoninjas.models.Dojo;
import com.bilel.dojoninjas.repositories.DojoRepository;

@Service
public class DojoService {
	
	// Dependencies injection for DojoRepository 
	@Autowired
	private DojoRepository dojoRepo ;
	
	
	//Create a Dojo 
	public Dojo createDojo(Dojo dojo) {
		return dojoRepo.save(dojo);
	}
	
	//read all 
	public List<Dojo> allDojos(){
		return dojoRepo.findAll();
	}

	//read one
	public Dojo findDojoById(Long id) {
		Optional<Dojo> dojo = dojoRepo.findById(id);
		if(dojo.isPresent()) {
			return dojo.get();
		}else {
			return null;
		}
	}

	// show one dojo
	public Dojo showDojoById(Long id) {
		Optional<Dojo> dojo = dojoRepo.findById(id);
		if(dojo.isPresent()) {
			return dojo.get();
		}else {
			return null;
		}
	}

}
