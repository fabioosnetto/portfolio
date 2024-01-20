package com.springboot.api.project1.infra;

import org.springframework.http.ResponseEntity;
import org.springframework.validation.FieldError;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

import jakarta.persistence.EntityNotFoundException;

@RestControllerAdvice // listent to each api exception -> this removes the necessity of handling each error with try.catch block on each endpoint
public class exceptionsHandler {
   
   @ExceptionHandler(EntityNotFoundException.class) // handles every not found exception of api
   public ResponseEntity<?> handler404() {
      return ResponseEntity.notFound().build(); // return a not found (404 status) when the endpoint was not found without body
   }

   @ExceptionHandler(MethodArgumentNotValidException.class)
   public ResponseEntity<?> handler400(MethodArgumentNotValidException err) {
      var fields = err.getFieldErrors();

      return ResponseEntity.badRequest().body(fields.stream().map(ErrorData::new).toList()); // return a bad request (400 status) when some endpoint value is incorret providen with a field and message into response body
   }


   // a record to format the errors to be sent to the client side
   public record ErrorData(
      String field,
      String message
   ) {

      public ErrorData(FieldError err) {
         this(err.getField(), err.getDefaultMessage());
      }
   }
}
