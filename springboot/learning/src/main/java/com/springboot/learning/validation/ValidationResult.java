package com.springboot.learning.validation;

public class ValidationResult {
   private final String msg;
   private final boolean status;

   public ValidationResult(String msg, boolean status) {
      this.msg = msg;
      this.status = status;
   }

   public String getMsg() {
      return msg;
   }

   public boolean getStatus() {
      return status;
   }
}

