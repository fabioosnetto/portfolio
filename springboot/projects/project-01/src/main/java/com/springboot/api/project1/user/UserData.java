package com.springboot.api.project1.user;

public record UserData(
   Long   id,
   String username,
   String firstName,
   String lastName,
   String city,
   String state,
   String status
) {

   public UserData(UserEntity data) {
      this(data.getId(), data.getUsername(), data.getFirstName(), data.getLastName(), data.getCity(), data.getState(), data.getStatus());
   }
}
