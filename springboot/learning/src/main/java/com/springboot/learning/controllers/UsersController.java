package com.springboot.learning.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.springboot.learning.user.UserEntity;
import com.springboot.learning.user.UserRepository;
import com.springboot.learning.user.User_DTO;
import com.springboot.learning.validation.ValidationResult;
import com.springboot.learning.validation.ValidationService;


@RestController
@RequestMapping("/user")
public class UsersController {

   @Autowired
   private UserRepository repository;

   @Autowired
   private ValidationService validation = new ValidationService();
   
   @PostMapping
   public ResponseEntity<String> register(@RequestBody User_DTO data) {
      System.out.println(data);
      System.out.println(data.gender().getAbbr());
      
      // validate data
      ValidationResult result = validation.validate(data);

      // send response to the user
      if(result.getStatus()) {
         repository.save(new UserEntity(data));
         return ResponseEntity.status(200).body("Succesfully registered the user!");
      }

      return ResponseEntity.status(400).body(result.getMsg());
   } 

}
