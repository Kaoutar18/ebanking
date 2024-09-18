package org.example.ebank.Entity;

import javax.persistence.*;

@Entity
public class Client {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String firstName;
    private String lastName;
    private String email;
    // other client fields

    @ManyToOne
    @JoinColumn(name = "role_id")
    private Role role;

    // Getters and setters
}
