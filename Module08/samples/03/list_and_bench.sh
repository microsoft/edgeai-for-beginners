#!/bin/bash
# List available and cached models, then run a quick test
foundry model list
foundry cache list
foundry model run phi-4-mini --verbose
