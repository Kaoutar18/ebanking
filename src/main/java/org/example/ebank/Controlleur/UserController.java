package org.example.ebank.Controlleur;

import org.apache.tomcat.util.net.openssl.ciphers.Authentication;
import org.example.ebank.Entity.User;
import org.example.ebank.Entity.UserLoginRequest;
import org.example.ebank.Repository.UserRepository;
import org.example.ebank.Service.InvalidTokenService;
import org.example.ebank.Service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.time.LocalDateTime;
import java.util.List;

@RestController
@RequestMapping("/api/users")
public class UserController {

    @Autowired
    private UserService userService;
    private    InvalidTokenService invalidTokenService;

    @PostMapping("/login")
    public ResponseEntity<?> login(@RequestBody UserLoginRequest loginRequest) {
        String token = userService.login(loginRequest.getUsername(), loginRequest.getPassword());
        if (token != null) {
            return ResponseEntity.ok(token);
        } else {
            return ResponseEntity.status(401).body("Login failed");
        }
    }
    public void logout(@RequestHeader("Authorization") String token, Authentication authentication) {
        // Extract the token (removing "Bearer " prefix)
        String tokenValue = token.substring(7);

        // Invalidate the token
        // You should extract the expiry date from the token and pass it to the invalidateToken method
        LocalDateTime expiryDate = extractExpiryDateFromToken(tokenValue);

        invalidTokenService.invalidateToken(tokenValue, expiryDate);

        // Perform other logout operations if necessary
    }

    private LocalDateTime extractExpiryDateFromToken(String token) {
        // Logic to extract expiry date from the token
        // This depends on how you generate the token
        // Here, we assume you have a method to decode and extract the expiry date
        return LocalDateTime.now().plusHours(1); // Example implementation
    }
    @Autowired
    private UserRepository userRepository;

    // Endpoint pour récupérer tous les utilisateurs
    @GetMapping
    public ResponseEntity<List<User>> getAllUsers() {
        List<User> users = userRepository.findAll();
        return ResponseEntity.ok(users);
    }

    // Endpoint pour récupérer un utilisateur par son ID
    @GetMapping("/{id}")
    public ResponseEntity<User> getUserById(@PathVariable("id") Long id) {
        User user = userRepository.findById(id).orElse(null);
        if (user == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(user);
    }

    // Endpoint pour créer un nouvel utilisateur
    @PostMapping
    public ResponseEntity<User> createUser(@RequestBody User user) {
        User savedUser = userRepository.save(user);
        return ResponseEntity.status(HttpStatus.CREATED).body(savedUser);
    }

    // Endpoint pour mettre à jour un utilisateur existant
    @PutMapping("/{id}")
    public ResponseEntity<User> updateUser(@PathVariable("id") Long id, @RequestBody User user) {
        if (!userRepository.existsById(id)) {
            return ResponseEntity.notFound().build();
        }
        user.setId(id); // Assurez-vous que l'ID de l'utilisateur à mettre à jour est défini
        User updatedUser = userRepository.save(user);
        return ResponseEntity.ok(updatedUser);
    }

    // Endpoint pour supprimer un utilisateur
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteUser(@PathVariable("id") Long id) {
        if (!userRepository.existsById(id)) {
            return ResponseEntity.notFound().build();
        }
        userRepository.deleteById(id);
        return ResponseEntity.noContent().build();
    }

}
