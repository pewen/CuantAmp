# CuantAmp

Cuantificando Amplificacion (en twitter)

## Local setup

```bash
git clone https://github.com/pewen/CuantAmp.git
cd CuantAmp
cp .env.local .env
# Set the credentials on .env

# This step will take because it will
# obtain the data for each seed user
./dev-setup
docker-compose up
```

Ahora la UI esta funcionando en [http://localhost:3000](http://localhost:3000) y el backend en [http://localhost:8000/docs](http://localhost:8000/docs)
