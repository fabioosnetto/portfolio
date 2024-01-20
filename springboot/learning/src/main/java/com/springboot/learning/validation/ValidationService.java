package com.springboot.learning.validation;
import jakarta.validation.Validation;
import jakarta.validation.Validator;
import jakarta.validation.ValidatorFactory;
import jakarta.validation.ConstraintViolation;

import java.util.Set;

import org.springframework.stereotype.Service;

@Service
public class ValidationService {

    private final Validator validator;

    public ValidationService() {
        ValidatorFactory factory = Validation.buildDefaultValidatorFactory();
        this.validator = factory.getValidator();
    }

    public ValidationResult validate(Object objectToValidate) {
        Set<ConstraintViolation<Object>> violations = validator.validate(objectToValidate);

        if (!violations.isEmpty()) {
            // Handle validation errors
            for (ConstraintViolation<Object> violation : violations) {
                return new ValidationResult(violation.getMessage(), false);
            }
        }
        
        return new ValidationResult("Validation Passed", true);
    }
}
