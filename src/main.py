"""Main entry point for the payments-mcp server."""
from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from platform_sdk import MCPConfig, configure_logging, get_logger

from .payments_mcp_service import PaymentsMcpService

configure_logging()
log = get_logger(__name__)

config = MCPConfig.load()
service = PaymentsMcpService(config=config)

mcp = FastMCP(
    "payments-mcp",
    lifespan=service.lifespan,
    host="0.0.0.0",
    port=config.port,
)

service.register_tools(mcp)


if __name__ == "__main__":
    log.info("mcp_server_starting", transport=config.transport)
    service.run_with_registration(mcp, config.transport)
