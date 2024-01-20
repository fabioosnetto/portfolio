package com.springboot.learning.user;

public enum Gender {
   MALE("M"),
   FEMALE("F");

   private final String abbr;

   Gender(String abbr) {
      this.abbr = abbr;
   }

   public String getAbbr() {
      return this.abbr;
   }
}
