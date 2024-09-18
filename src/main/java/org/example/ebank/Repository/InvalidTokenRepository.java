package org.example.ebank.Repository;

import org.example.ebank.Entity.InvalidToken;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface InvalidTokenRepository extends JpaRepository<InvalidToken, Long> {
    Optional<InvalidToken> findByToken(String token);
}
