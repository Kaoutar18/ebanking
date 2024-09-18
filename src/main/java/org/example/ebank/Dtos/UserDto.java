package org.example.ebank.Dtos;

public class UserDto {
    private String username;
    private String role;

    public Object getUsername() {
        return username;
    }

    public CharSequence getPassword() {
        return getPassword();
    }

    public Object getRole() {
       return getPassword();
    }
    // getters and setters
}

class ClientDto extends UserDto {
    private String firstName;
    private String lastName;
    // getters and setters
}

class AgentDto extends UserDto {
    private String agentCode;
    // getters and setters
}

class TransactionDto {
    private Double amount;
    private String description;
    private String fromAccount;
    private String toAccount;
    // getters and setters
}
