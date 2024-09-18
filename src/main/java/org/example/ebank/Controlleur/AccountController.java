package org.example.ebank.Controlleur;

import org.example.ebank.Dtos.AccountDto;
import org.example.ebank.Entity.Account;
import org.example.ebank.Service.AccountService;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/accounts")
public class AccountController {
    private final AccountService accountService;

    public AccountController(AccountService accountService) {
        this.accountService = accountService;
    }

    @PostMapping("/create")
    public Account createAccount(@RequestParam Long clientId, @RequestBody AccountDto accountDto) {
        return accountService.createAccount(clientId, accountDto);
    }

    // Other endpoints for accounts and transactions
}
