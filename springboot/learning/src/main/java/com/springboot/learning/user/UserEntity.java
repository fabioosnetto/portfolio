package com.springboot.learning.user;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.AllArgsConstructor;
import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Table(name = "users")
@Entity(name = "UserEntity")
@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
@EqualsAndHashCode(of = "id")
public class UserEntity {

   // constructor, called to construct values used to save with repository
   // construct the entity with the DTO data
   // the repository uses this entity
   public UserEntity(User_DTO data) {
      this.username     = data.username();
      this.age          = data.age();
      this.email        = data.email();
      this.phone_number = data.phone_number();
      this.cpf          = data.cpf();
      this.gender       = data.gender().getAbbr();
   }

   @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
   private Long id;
   private String username;
   private int age;
   private String email;
   private String phone_number;
   private String cpf;
   private String gender;
}
