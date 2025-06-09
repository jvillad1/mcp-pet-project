# MCP Servers

A collection of MCP (Model Context Protocol) servers.

## Math Server

A simple math server that provides basic arithmetic operations:
- `add(a, b)` - Add two numbers
- `multiply(a, b)` - Multiply two numbers

## Weather Server

A weather server that provides weather information:
- `get_weather(location)` - Get weather information for a specified location

*Note: Currently returns a mock response for demonstration purposes.*

## Usage

Run the math server:
```bash
python math_server.py
```

Run the weather server:
```bash
python weather_server.py
```

### Transport Protocols

- **Math Server**: Uses `stdio` transport for standard input/output communication
- **Weather Server**: Uses `streamable-http` transport for HTTP-based communication