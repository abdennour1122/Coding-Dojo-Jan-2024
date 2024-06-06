package com.bilel.cars.models;

import java.util.Date;

import org.springframework.format.annotation.DateTimeFormat;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.PrePersist;
import jakarta.persistence.PreUpdate;
import jakarta.persistence.Table;
import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotEmpty;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Size;

@Entity
@Table(name="cars")
public class Car {
	
	@Id
	@GeneratedValue(strategy= GenerationType.IDENTITY)
	private Long id;
	@NotEmpty
	@Size(min=2 , max= 200 , message="Model must be between 2 and 200 characters")
	private String model;
	@NotEmpty
	@Size(min=2 , max= 200 , message="Model must be between 2 and 200 characters")
	private String color;
	@NotNull
	@Min(value = 100, message="Price must be greater than 100")
	private double price;
	@DateTimeFormat(pattern="yyyy-mm-dd")
	private Date releaseDate;
	@Column(updatable=false)
	@DateTimeFormat(pattern="yyyy-mm-dd")
	private Date createdAt;
	@DateTimeFormat(pattern="yyyy-mm-dd")
	private Date updatedAT;
	@ManyToOne (fetch=FetchType.LAZY)
	@JoinColumn(name="user_id")
	private USER owner;
	
    @PrePersist
    protected void onCreate(){
        this.createdAt = new Date();
    }
    @PreUpdate
    protected void onUpdate(){
        this.updatedAT = new Date();
    }
	
	
	
	
	//constructor
	public Car() {
		super();
	}

	//Getters and Setters

	public Long getId() {
		return id;
	}



	public USER getOwner() {
		return owner;
	}
	public void setOwner(USER owner) {
		this.owner = owner;
	}
	public void setId(Long id) {
		this.id = id;
	}



	public String getModel() {
		return model;
	}



	public void setModel(String model) {
		this.model = model;
	}



	public String getColor() {
		return color;
	}



	public void setColor(String color) {
		this.color = color;
	}



	public double getPrice() {
		return price;
	}



	public void setPrice(double price) {
		this.price = price;
	}



	public Date getReleaseDate() {
		return releaseDate;
	}



	public void setReleaseDate(Date releaseDate) {
		this.releaseDate = releaseDate;
	}



	public Date getCreatedAt() {
		return createdAt;
	}



	public void setCreatedAt(Date createdAt) {
		this.createdAt = createdAt;
	}



	public Date getUpdatedAT() {
		return updatedAT;
	}



	public void setUpdatedAT(Date updatedAT) {
		this.updatedAT = updatedAT;
	}
	
	

	
	
	
	
	

}
