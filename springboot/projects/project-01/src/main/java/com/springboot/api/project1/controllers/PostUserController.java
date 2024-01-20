package com.springboot.api.project1.controllers;

import java.util.Comparator;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.util.UriComponentsBuilder;

import com.springboot.api.project1.user.UserDTO;
import com.springboot.api.project1.user.UserData;
import com.springboot.api.project1.user.UserEntity;
import com.springboot.api.project1.user.UserRepository;
import com.springboot.api.project1.user.UserUpdateDTO;

import jakarta.transaction.Transactional;
import jakarta.validation.Valid;
import org.springframework.web.bind.annotation.PutMapping;


@RestController
@RequestMapping("/api/user")
public class PostUserController {

   @Autowired // java dependency injection
   UserRepository repository; // repository extended with JpaRepository that perform actions on database to the providen instance of UserEntity type
   
   @PostMapping // post endpoint
   @Transactional // prevents proccess fails, returning all data to the initial state if proccess fails
   public ResponseEntity<UserData> register(@RequestBody @Valid UserDTO data, UriComponentsBuilder uriBuilder) {
      
      // create an user object with the user DTO
      // save the object using the injected repository
      var userInstance = new UserEntity(data);
      repository.save(userInstance);
      
      // create a path to the saved user and fill the id parameter using the user instance saved
      var uri = uriBuilder.path("/api/user/{id}").buildAndExpand(userInstance.getId()).toUri();

      // return the created status (201) with the access path and the user instance saved (sent on body)
      return ResponseEntity.created(uri).body(new UserData(userInstance));
   }

   @PutMapping
   @Transactional
   public ResponseEntity<UserData> putMethodName(@RequestBody @Valid UserUpdateDTO data) {
      UserEntity userInstance = repository.getReferenceById(data.id());
      userInstance.update(data);
       
      return ResponseEntity.ok(new UserData(userInstance));
   }

   @DeleteMapping("{id}")
   @Transactional
   public ResponseEntity<Void> delete(@PathVariable Long id) {
      repository.deleteById(id);

      return ResponseEntity.noContent().build();
   }


   @GetMapping
   @Transactional
   public ResponseEntity<List<UserData>> getAll() {
      List<UserData> data = repository.findAll().stream().map(UserData::new).sorted(Comparator.comparing(UserData::id)).toList();
      
      return ResponseEntity.ok(data); // ok status with the requested data on response body
   }

   @GetMapping("/{id}")
   @Transactional
   public ResponseEntity<UserData> getByID(@PathVariable Long id) {
      UserData user = new UserData(repository.getReferenceById(id));

      return ResponseEntity.ok(user);
   }
   

}
