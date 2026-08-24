# GoLand Go Lab - Multi-stage build
FROM ubuntu:24.04 AS builder

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y     build-essential     && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace
COPY . .
# RUN build commands here

FROM ubuntu:24.04 AS runtime
WORKDIR /workspace
COPY --from=builder /workspace/build ./build
COPY --from=builder /workspace/scripts ./scripts
CMD ["/bin/bash"]
