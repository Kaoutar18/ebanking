package org.example.ebank.Entity;

import javax.persistence.*;

@Entity
public class Agent {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String firstName;
    private String lastName;
    private String email;
    // other agent fields

    @ManyToOne
    @JoinColumn(name = "role_id")
    private Role role;

    // Getters and setters
}
