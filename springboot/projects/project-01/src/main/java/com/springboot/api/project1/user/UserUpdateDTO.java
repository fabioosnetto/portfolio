package com.springboot.api.project1.user;

import jakarta.validation.constraints.NotNull;

public record UserUpdateDTO(
   @NotNull
   Long   id,

   String username,
   String firstName,
   String lastName,
   String city,
   String state,
   String status
) {
}
