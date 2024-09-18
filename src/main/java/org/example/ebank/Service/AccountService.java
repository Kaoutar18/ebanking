package org.example.ebank.Service;

import org.example.ebank.Dtos.*;
import org.example.ebank.Dtos.UserDto;
import org.example.ebank.Entity.*;
import org.example.ebank.Repository.*;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
@Transactional
public class AccountService {
    private final AccountRepository accountRepository;
    private final ClientRepository clientRepository;

    public AccountService(AccountRepository accountRepository, ClientRepository clientRepository) {
        this.accountRepository = accountRepository;
        this.clientRepository = clientRepository;
    }

    public Account createAccount(Long clientId, AccountDto accountDto) {
        Client client = clientRepository.findById(clientId).orElseThrow(() -> new RuntimeException("Client not found"));
        Account account = new Account();
        account.setAccountNumber(accountDto.getAccountNumber());
        account.setBalance(accountDto.getBalance());
        account.setClient(client);
        return accountRepository.save(account);
    }

    // Other methods for handling accounts and transactions
}
