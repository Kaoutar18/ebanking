package org.example.ebank.Entity;

import javax.persistence.*;

@Entity
public
class Account {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String accountNumber;
    private Double balance;

    @ManyToOne
    @JoinColumn(name = "client_id")
    private Client client;

    public void setAccountNumber(Object accountNumber) {
    }

    public void setBalance(Object balance) {
    }

    public void setClient(Client client) {
    }

    // getters and setters
}
