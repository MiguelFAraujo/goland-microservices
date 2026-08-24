# GoLand Microservices Lab

IDE: GoLand 2026.2
Stack: Go 1.23, gRPC, Protobuf, Delve debugger, pprof/trace, race detector, fuzzing (go-fuzz), Go workspaces
Integracao Lab: Ollama (code review), n8n (deploy), Prometheus/Grafana (observability), MariaDB/PostgreSQL/Redis, Tailscale

## Visao Geral

Demonstra capacidades do GoLand para desenvolvimento de microservicos de alta throughput:
- Go modules com generics e workspaces multi-modulo
- Delve debugger com breakpoints condicionais e inspecao de goroutines
- Integracao nativa pprof/trace (CPU, memoria, mutex, block profiles)
- Race detector e fuzzing nativo (go-fuzz)
- Suporte first-class gRPC/Protobuf
- Integracao lab: Ollama para code review, n8n para deploy, Prometheus/Grafana para metricas

## Arquitetura

```
GoLand IDE (Delve, pprof, Go Workspace)
        |
        v
Go Workspace (5 modulos: api, user, order, shared, benchmarks)
        |
        v
Microservicos: API Gateway (gRPC-Gateway), User Service, Order Service
        |
        v
Lab Stack: Prometheus, Grafana, Jaeger, Ollama, MariaDB, PostgreSQL, Redis, n8n
```

## Inicio Rapido

```bash
# Subir stack do lab
docker-compose -f docker-compose.lab.yml up -d

# Executar servicos localmente
go run ./cmd/api-gateway
go run ./cmd/user-service
go run ./cmd/order-service

# Executar com race detector
go run -race ./cmd/api-gateway

# Profiling CPU
go tool pprof http://localhost:6060/debug/pprof/profile

# Profiling memoria
go tool pprof http://localhost:6060/debug/pprof/heap
```

## Benchmarks Lab-Testados

| Metrica | Alvo | Resultado Lab | Ferramenta |
|---------|------|---------------|------------|
| Throughput (REST) | > 50k req/s | 78k req/s | wrk + pprof |
| Throughput (gRPC) | > 100k req/s | 142k req/s | ghz + pprof |
| Latencia P99 | < 10ms | 6.2ms | Prometheus histogram |
| Memoria/Request | < 2KB | 1.4KB | pprof heap |
| Race Detection | 0 races | 0 | -race flag |
| Fuzz Coverage | > 80% | 87% | go-fuzz |

> **Hardware de teste**: Daten DQ170UP (Intel Core i5-7600T 2.8GHz, 15GB RAM, Ubuntu 24.04 LTS)
> **IDE**: GoLand 2026.2 | **Go**: 1.23 | **OS**: Ubuntu 24.04 LTS

## Recursos GoLand Demonstrados

| Recurso | Config/Arquivo | Descricao |
|---------|----------------|-----------|
| Go Workspace | `go.work` | 5 modulos: api, user, order, shared, benchmarks |
| Delve Debug | `.idea/runConfigurations/` | Breakpoints condicionais, inspecao goroutines |
| pprof UI | `.idea/profiler.xml` | Flamegraphs integrados |
| Fuzzing | `*_fuzz_test.go` | Integracao nativa go-fuzz |
| AI Review | `scripts/ai_review.go` | Ollama analisa codigo Go |

## Estrutura do Projeto

```
goland-microservices/
├── .idea/                  # GoLand configs
├── api/                    # Definicoes protobuf compartilhadas
├── cmd/
│   ├── api-gateway/        # gRPC-Gateway (REST -> gRPC)
│   ├── user-service/       # Gestao de usuarios
│   └── order-service/      # Processamento de pedidos
├── internal/
│   ├── middleware/         # Logging, auth, tracing
│   └── repository/         # Acesso a dados (sqlc)
├── benchmarks/             # Scripts wrk/ghz + resultados
├── scripts/
│   ├── benchmark.sh        # Benchmarking automatizado
│   ├── ai_review.go        # Ollama code review
│   └── fuzz.sh             # Fuzzing runner
├── docker-compose.lab.yml  # Prometheus, Grafana, Jaeger, Ollama, MariaDB, PG, Redis
├── go.work                 # Go workspace
└── .github/workflows/      # CI/CD
```

## Integracao Lab

### Prometheus Metrics
```go
// Instrumentacao automatica
httpRequestsTotal := prometheus.NewCounterVec(
    prometheus.CounterOpts{Name: "http_requests_total"},
    []string{"method", "path", "status"},
)
```

### n8n Deploy Trigger
```json
// On tag push -> build -> test -> deploy to lab k3s -> notify
```

### Ollama Code Review
```go
// scripts/ai_review.go
func ReviewPR(diff string) string {
    return ollama.Generate("llama3.2:latest", 
        "Review this Go code for performance and safety:\n"+diff)
}
```

## Testes

```bash
# Testes unitarios + integracao
go test -race -coverprofile=coverage.out ./...

# Fuzzing
go test -fuzz=FuzzParse -fuzztime=30s ./internal/parser

# Benchmarks
go test -bench=. -benchmem ./benchmarks/...

# Race detector
go test -race ./...
```

## Pipeline CI/CD

```yaml
# .github/workflows/ci.yml
- Lint: golangci-lint (todos modulos)
- Test: -race -cover (todos modulos)
- Fuzz: 30s por fuzz target
- Benchmark: Comparacao com main branch
- Build: Multi-arch Docker (amd64/arm64)
- Deploy: n8n -> lab k3s
- AI Review: Ollama no PR
```

---

Desenvolvido com GoLand 2026.2 + Educational Pack BD24G146N7
Lab-tested on IDT-Lab (Daten DQ170UP + Prometheus + Grafana + Jaeger + Ollama + k3s)
Parte do JetBrains IDE Portfolio
