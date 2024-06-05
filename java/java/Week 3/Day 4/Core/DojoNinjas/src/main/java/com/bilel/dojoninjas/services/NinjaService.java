package com.bilel.dojoninjas.services;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.bilel.dojoninjas.models.Ninja;
import com.bilel.dojoninjas.repositories.NinjaRepository;

@Service
public class NinjaService {
	
	@Autowired
	private NinjaRepository ninjaRepo ;
	
	
	//Create Ninja
	public Ninja createNinja(Ninja ninja) {
		return ninjaRepo.save(ninja);
	}
	
	//Find All
	public List<Ninja> allNinja(){
		return ninjaRepo.findAll();
	}
	

}
