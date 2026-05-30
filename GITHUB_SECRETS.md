# Configuración de GitHub Actions Secrets

El pipeline necesita 3 secrets configurados en GitHub.
Ve a: tu repo → Settings → Secrets and variables → Actions → New repository secret

## Secrets requeridos

### GITHUB_TOKEN
Este lo provee GitHub automáticamente. No necesitas crearlo.
Se usa para hacer login al GitHub Container Registry (GHCR).

### VPS_HOST
La IP pública de tu VPS.
Ejemplo: 65.21.123.45

### VPS_USER
El usuario SSH de tu VPS.
Ejemplo: ubuntu  (en Hetzner suele ser root o el user que crees con Ansible)

### VPS_SSH_KEY
Tu llave SSH privada para conectarte al VPS.

Para generarla (si no tienes una):
  ssh-keygen -t ed25519 -C "github-actions-deploy" -f ~/.ssh/portfolio_deploy

Esto genera dos archivos:
  ~/.ssh/portfolio_deploy        ← llave PRIVADA → va en el secret VPS_SSH_KEY
  ~/.ssh/portfolio_deploy.pub    ← llave PÚBLICA  → va en el VPS en ~/.ssh/authorized_keys

Para copiar la llave privada al secret:
  cat ~/.ssh/portfolio_deploy

Copia todo el contenido incluyendo:
  -----BEGIN OPENSSH PRIVATE KEY-----
  ...
  -----END OPENSSH PRIVATE KEY-----

## Nota sobre el deploy

El job de deploy hace SSH al VPS y corre:
  docker compose pull
  docker compose up -d

Por eso el VPS necesita tener instalado:
  - Docker
  - Docker Compose
  - El proyecto clonado en /opt/portafolio
  - El archivo .env en /opt/portafolio

Todo eso lo configura Ansible automáticamente en la Fase 5.