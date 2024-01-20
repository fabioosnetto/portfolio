package com.springboot.learning.user;

import org.hibernate.validator.constraints.br.CPF;

import jakarta.persistence.Enumerated;
import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotBlank;

public record User_DTO(

   @NotBlank
   String username,
   
   int age,

   @Email
   String email,

   @NotBlank
   String phone_number,

   @CPF(message = "Invalid CPF format")
   String cpf,

   @Enumerated
   Gender gender
) {
}