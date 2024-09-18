package org.example.ebank.Service;

import org.example.ebank.Entity.User;
import org.example.ebank.Repository.UserRepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class UserService {
    private UserRepository userRepository;
    public String login(String username, String password) {
        // Logique d'authentification ici
        // Retournez un token JWT si l'authentification est réussie
        if ("your_username".equals(username) && "your_password".equals(password)) {
            return "fake-jwt-token";
        } else {
            return null;
        }
    }

    public List<User> getAllUsers() {
        return userRepository.findAll();
    }

    public User getUserById(Long id) {
        Optional<User> userOptional = userRepository.findById(id);
        return userOptional.orElse(null);
    }

    public User createUser(User user) {
        return userRepository.save(user);
    }

    public User updateUser(Long id, User user) {
        if (userRepository.existsById(id)) {
            user.setId(id); // Make sure the user object has the correct ID
            return userRepository.save(user);
        } else {
            return null;
        }
    }

    public void deleteUser(Long id) {
        userRepository.deleteById(id);
    }
}
