from workflow import workflow  # 🏗️ The travel plan workflow

def main():
    """Launch the travel workflow in DevUI."""
    import logging
    """Launch the basic orkflow in DevUI."""
    from agent_framework.devui import serve

    # Setup logging
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    logger = logging.getLogger(__name__)

    logger.info("Starting Podcast Workflow")
    logger.info("Available at: http://localhost:8090")
    logger.info("Entity ID: workflow_basic")

    # Launch server with the workflow
    serve(entities=[workflow], port=8090, auto_open=True)


if __name__ == "__main__":
    main()