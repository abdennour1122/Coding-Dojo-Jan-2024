package com.burgertraquer.models;

import java.util.Date;

import org.springframework.format.annotation.DateTimeFormat;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.PrePersist;
import jakarta.persistence.PreUpdate;
import jakarta.persistence.Table;
import jakarta.validation.constraints.Max;
import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotEmpty;
import jakarta.validation.constraints.NotNull;


@Entity
@Table(name = "burgers")
public class Burger {

    //! Attributes
    //? ID
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    //? Burger Name
    @NotEmpty (message = "Burger name is required")
    private String burgerName;
    //? Restaurant Name
    @NotEmpty (message = "Restaurant name is required")
    private String restaurantName;
    //? Rating
    @NotNull
    @Min(value=0 , message = "Rating must be between 0 and 5")
    @Max(value=5 , message = "Rating must be between 0 and 5")
    private int rating;
    //? Notes
    @NotEmpty (message = "Notes are required")
    private String notes;
    //? Created At & Updated At
    @Column(updatable = false)
    @DateTimeFormat(pattern = "yyyy-MM-dd")
    private Date createdAt;
    @DateTimeFormat(pattern = "yyyy-MM-dd")
    private Date updatedAt;
    
    //! Constructors
    public Burger() {
    }
    public Burger(String burgerName, String restaurantName, int rating, String notes) {
        this.burgerName = burgerName;
        this.restaurantName = restaurantName;
        this.rating = rating;
        this.notes = notes;
    }
    // Getters & Setters
    @PrePersist
    protected void onCreate() {
        this.createdAt = new Date();
    }
    @PreUpdate
    protected void onUpdate() {
        this.updatedAt = new Date();
    }
    public Long getId() {
        return id;
    }
    public void setId(Long id) {
        this.id = id;
    }
    public String getBurgerName() {
        return burgerName;
    }
    public void setBurgerName(String burgerName) {
        this.burgerName = burgerName;
    }
    public String getRestaurantName() {
        return restaurantName;
    }
    public void setRestaurantName(String restaurantName) {
        this.restaurantName = restaurantName;
    }
    public int getRating() {
        return rating;
    }
    public void setRating(int rating) {
        this.rating = rating;
    }
    public String getNotes() {
        return notes;
    }
    public void setNotes(String notes) {
        this.notes = notes;
    }
    public Date getCreatedAt() {
        return createdAt;
    }
    public void setCreatedAt(Date createdAt) {
        this.createdAt = createdAt;
    }
    public Date getUpdatedAt() {
        return updatedAt;
    }
    public void setUpdatedAt(Date updatedAt) {
        this.updatedAt = updatedAt;
    }
    


}
