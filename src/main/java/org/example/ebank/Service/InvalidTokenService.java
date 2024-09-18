package org.example.ebank.Service;

import org.example.ebank.Entity.InvalidToken;
import org.example.ebank.Repository.InvalidTokenRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;

@Service
public class InvalidTokenService {

    @Autowired
    private InvalidTokenRepository invalidTokenRepository;

    public void invalidateToken(String token, LocalDateTime expiryDate) {
        InvalidToken invalidToken = new InvalidToken();
        invalidToken.setToken(token);
        invalidToken.setExpiryDate(expiryDate);
        invalidTokenRepository.save(invalidToken);
    }

    public boolean isTokenInvalid(String token) {
        return invalidTokenRepository.findByToken(token).isPresent();
    }
}
