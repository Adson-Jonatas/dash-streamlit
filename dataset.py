import pandas as pd
import random

data = {
    "aplicacao": [
        random.choice(["Frontend", "Backend", "Mobile", "API"]) for _ in range(45)
    ],
    "sigla": [f"APP{i:02}" for i in range(1, 46)],
    "componente": [
        random.choice([
            "auth-module", "payment-gateway", "user-service", "data-handler", "notification-center",
            "reporting-tool", "integration-api", "scheduler", "caching-layer", "logging-service",
            "security-module", "ml-engine", "data-analytics", "web-socket", "queue-manager"
        ]) for _ in range(45)
    ],
    "vuln_critica": [random.randint(0, 80) for _ in range(45)],
    "vuln_alta": [random.randint(0, 120) for _ in range(45)],
    "vuln_media": [random.randint(0, 75) for _ in range(45)],
    "vuln_baixa": [random.randint(0, 30) for _ in range(45)],
}

# Transformar em DataFrame para visualização (opcional)
df = pd.DataFrame(data)

print(df.to_string())
