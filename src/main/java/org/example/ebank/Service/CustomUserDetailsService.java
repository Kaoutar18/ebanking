package org.example.ebank.Service;

import org.example.ebank.Entity.User;
import org.example.ebank.Repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

import java.util.ArrayList;

@Service
public class CustomUserDetailsService implements UserDetailsService {

    @Autowired
    private UserRepository userRepository;

    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        // Recherche de l'utilisateur dans la base de données par son nom d'utilisateur
        User user = userRepository.findByUsername(username);

        // Vérifier si l'utilisateur est null
        if (user == null) {
            throw new UsernameNotFoundException("User not found with username: " + username);
        }

        // Création et retour d'un UserDetails avec les informations de l'utilisateur
        return org.springframework.security.core.userdetails.User.builder()
                .username(user.getUsername())
                .password(user.getPassword())
                .authorities(new ArrayList<>()) // Vous pouvez ajouter les rôles/autorisations ici si nécessaire
                .build();
    }

}
