package com.springboot.api.project1.user;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import jakarta.validation.Valid;
import lombok.AllArgsConstructor;
import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Table(name = "users_register") // table of UserEntity used by UserRepository to perform DB actions
@Entity(name = "UserEntity") // Entity name
@Getter // creates getters methods without its declaration
@Setter // creates setters methods without its declaration
@AllArgsConstructor // generates a constructor with attributes and its initialization
@NoArgsConstructor // generates an empty constructor
@EqualsAndHashCode(of = "id") // generates equals() and hashCode() methods to id
public class UserEntity {

   public UserEntity (UserDTO data) {
      this.username  = data.username();
      this.firstName = data.firstName();
      this.lastName  = data.lastName();
      this.city      = data.city();
      this.state     = data.state();
      this.status    = data.status();
   }

   @Id @GeneratedValue(strategy = GenerationType.IDENTITY) // repository intendifies for generating an unique ID for id
   private Long id;
   private String username;

   @Column(name = "first_name")
   private String firstName;

   @Column(name = "last_name")
   private String lastName;

   private String city;
   
   @Column(name = "state_abbr")
   private String state;

   @Column(name = "user_status")
   private String status;

   public void update(@Valid UserUpdateDTO data) {
      if(!data.username().isBlank() && data.username() != null) {
         this.username = data.username();
      }

      if(!data.firstName().isBlank() && data.firstName() != null) {
         this.firstName = data.firstName();
      }

      if(!data.lastName().isBlank() && data.lastName() != null) {
         this.lastName = data.lastName();
      }

      if(!data.city().isBlank() && data.city() != null) {
         this.city = data.city();
      }

      if(!data.state().isBlank() && data.state() != null) {
         this.state = data.state();
      }

      if(!data.status().isBlank() && data.status() != null) {
         this.status = data.status();
      }
   }
}
