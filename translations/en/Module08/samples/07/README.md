# Foundry Local as API Sample

This sample demonstrates how to use Microsoft Foundry Local as a REST API service without relying on the OpenAI SDK. It showcases direct HTTP integration patterns for maximum control and customization.

## Overview

Based on Microsoft's official Foundry Local patterns, this sample provides:
- Direct REST API integration with FoundryLocalManager
- Custom HTTP client implementation
- Model management and health monitoring
- Streaming and non-streaming response handling
- Production-ready error handling and retry logic

## Prerequisites

1. **Foundry Local Installation**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **Python Dependencies**
   ```bash
   pip install foundry-local-sdk requests asyncio aiohttp
   ```

## Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Your App      │───▶│  REST API Client │───▶│  Foundry Local  │
│                 │    │                  │    │   Service       │
│ - Custom Logic  │    │ - HTTP Requests  │    │ - Model Loading │
│ - Business Rules│    │ - Authentication │    │ - Inference     │
│ - Data Pipeline │    │ - Error Handling │    │ - Health Check  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## Key Features

### 1. **Direct HTTP Integration**
- Pure REST API calls without SDK dependencies
- Custom authentication and headers
- Full control over request/response handling

### 2. **Model Management**
- Dynamic model loading and unloading
- Health monitoring and status checks
- Performance metrics collection

### 3. **Production Patterns**
- Retry mechanisms with exponential backoff
- Circuit breaker for fault tolerance
- Comprehensive logging and monitoring

### 4. **Flexible Response Handling**
- Streaming responses for real-time applications
- Batch processing for high-throughput scenarios
- Custom response parsing and validation

## Usage Examples

### Basic API Integration
```python
from api_client import FoundryAPIClient

# Initialize the API client
client = FoundryAPIClient()

# Simple completion
response = await client.complete(
    prompt="Explain quantum computing",
    model="phi-4-mini",
    max_tokens=500
)
print(response.content)
```

### Streaming Integration
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### Health Monitoring
```python
# Check service health
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```

## File Structure

```
07/
├── README.md              # This documentation
├── requirements.txt       # Python dependencies
├── api_client.py         # Core API client implementation
├── health_monitor.py     # Health checking and monitoring
├── examples/
│   ├── basic_usage.py    # Simple API integration example
│   ├── streaming.py      # Streaming response example
│   ├── batch_processing.py # Batch processing example
│   └── production.py     # Production-ready implementation
└── tests/
    ├── test_api_client.py    # Unit tests for API client
    └── test_integration.py   # Integration tests
```

## Microsoft Foundry Local Integration

This sample follows Microsoft's official patterns:

1. **SDK Integration**: Uses `FoundryLocalManager` for service management
2. **REST Endpoints**: Direct calls to `/v1/chat/completions` and other endpoints
3. **Authentication**: Proper API key handling for local services
4. **Model Management**: Catalog listing, downloading, and loading patterns
5. **Error Handling**: Microsoft-recommended error codes and responses

## Getting Started

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Basic Example**
   ```bash
   python examples/basic_usage.py
   ```

3. **Try Streaming**
   ```bash
   python examples/streaming.py
   ```

4. **Production Setup**
   ```bash
   python examples/production.py
   ```

## Configuration

Environment variables for customization:
- `FOUNDRY_MODEL`: Default model to use (default: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: Request timeout in seconds (default: 30)
- `FOUNDRY_RETRIES`: Number of retry attempts (default: 3)
- `FOUNDRY_LOG_LEVEL`: Logging level (default: "INFO")

## Best Practices

1. **Connection Management**: Reuse HTTP connections for better performance
2. **Error Handling**: Implement proper retry logic with exponential backoff
3. **Resource Monitoring**: Track model memory usage and performance
4. **Security**: Use proper authentication even for local services
5. **Testing**: Include both unit and integration tests

## Troubleshooting

### Common Issues

**Service Not Running**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**Model Loading Issues**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**Connection Errors**
- Verify Foundry Local is running on correct port
- Check firewall settings
- Ensure proper authentication headers

## Performance Optimization

1. **Connection Pooling**: Use session objects for multiple requests
2. **Async Operations**: Leverage asyncio for concurrent requests
3. **Caching**: Cache model responses where appropriate
4. **Monitoring**: Track response times and adjust timeouts

## Learning Outcomes

After completing this sample, you will understand:
- Direct REST API integration with Foundry Local
- Custom HTTP client implementation patterns
- Production-ready error handling and monitoring
- Microsoft Foundry Local service architecture
- Performance optimization techniques for local AI services

## Next Steps

- Explore Sample 08: Windows 11 Chat Application
- Try Sample 09: Multi-Agent Orchestration
- Learn Sample 10: Foundry Local as Tools Integration

---

