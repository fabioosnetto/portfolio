package com.springboot.learning.controllers;

import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.GetMapping;


@RestController
@RequestMapping("/hello-world")
public class HelloWorld {

   @GetMapping
   public String message() {
      return "Hello Fucking World!";
   }

}
