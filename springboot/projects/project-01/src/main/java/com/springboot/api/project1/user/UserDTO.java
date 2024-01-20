package com.springboot.api.project1.user;

import jakarta.persistence.Id;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Size;

public record UserDTO(

   @Id
   Long   id,

   @NotBlank
   String username,

   @NotBlank
   String firstName,

   @NotBlank
   String lastName,

   @NotBlank
   String city,

   @NotBlank
   @Size(max = 2, message = "status must have at most 2 characters")
   String state,

   @NotBlank
   @Size(max = 1, message = "status must have at most 1 character")
   String status
) {
}